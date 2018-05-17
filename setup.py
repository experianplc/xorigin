from setuptools import setup
setup(name="xorigin",
      version="0.1",
      description="Easy to use, portable CORS reverse proxy",
      url="https://github.com/experianplc/xorigin",
      author="Tabeth Nkangoh | Experian",
      author_email="tabeth.nkangoh@experian.com",
      license="MIT",
      packages=["xorigin"],
      keywords=["Cross origin", "Reverse proxy", "CORS Server", "Server"],
      install_requires=[
            "twisted>=16.0.0"
      ])
