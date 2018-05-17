# Copyright (c) Experian

"""
This is a minimal reverse-proxy that is to be used
with APIs that do not support CORS by default.
It is not intended for production use,
and ideally should be swapped out for an equivalent
reverse proxy using Nginx, Apache, IIS or similar.

Run this example with:
    $ python xorigin.py

Alternatively (in Windows) you can run it by executing
    xorigin.exe

Then visit http://localhost:{{SERVER_PORT}}/ in your web browser.
"""

from twisted.internet import reactor
from twisted.web.proxy import ReverseProxyResource
from twisted.web import server
from twisted.python import log
from sys import stdout
import yaml

config = yaml.safe_load(open('config.yaml'))

port = config['SERVER_PORT']
endpoint_url = config['ENDPOINT_URL']
endpoint_port = config['ENDPOINT_PORT']
headers = config['HEADERS']

class CORSResource(ReverseProxyResource):
    def __init__(host, port, path, reactor):
        ReverseProxyResource.__init__(host, port, path, reactor)

    def getChild(self, name, request):
        for header in headers.keys():
            request.setHeader(header, headers[header])

        # For CORS preflight OPTION request anything between 200 - 299 is acceptable.
        # We use 204 as are not actually sending any content in this case.
        if request.method == 'OPTIONS':
            request.setResponseCode(204, "No Content")
            request.write("")

        return ReverseProxyResource.getChild(self, name, request)

if __name__ == "__main__":
    site = server.Site(CORSResource(endpoint_url, endpoint_port, ''))
    log.startLogging(stdout)
    reactor.listenTCP(port, site)
    reactor.run()
