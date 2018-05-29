<p align="center">
  <img src="https://github.com/experianplc/xorigin/raw/master/media/logo.jpg">
</p>
  
# Basic Overview
Generally Cross-origin resource sharing (CORS) is something that you *don't* want
as unrestricted sharing of resources across domains is something that can pose a
security risk. However for a plethora of reasons you do want to enable CORS
as the same-origin policy is something that may be too restrictive, depending on
the use case. 

For those times where you want CORS to be enabled, **xorigin** can allow you to
quickly test an endpoint that is not setup to CORS in a CORS fashion.


# Usage
Right now use it by filling out `config.yaml` with the appropriate options (See configuration)
and running the server, e.g. `python xorigin`. Alternatively, you can unzip the
latest [release](https://github.com/experianplc/xorigin/releases) and run `xorigin.exe` 
after filling out `config.yaml` and putting it in the same directory as `xorigin.exe`.


# Configuration
`config.yaml` has a few options:

`SERVER_PORT`: The port you want the server to use (e.g. host localhost, port 8000).

`ENDPOINT_URL`: The full url of the endpoint, excluding the protocol (e.g. google.com).

`ENDPOINT_PORT`: The port of the endpoint (e.g. 80).

`HEADERS`: Any headers you want the server to include when proxying. By default this 
includes headers for aiding with cross origin requests.
