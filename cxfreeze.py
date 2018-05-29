from cx_Freeze import setup, Executable
import sys

base = None


executables = [
    Executable(
        script='xorigin/xorigin.py',
        base=base,
        icon=None
    )
]

build_exe_options = {
        "packages": ["os", "yaml", "twisted.internet", "zope.interface", "pkg_resources._vendor", "idna"],
        "excludes": [],
        "includes": []
}

setup(
      name="xorigin.exe",
      version="0.1",
      description="Easy to use, portable CORS reverse proxy",
      url="https://github.com/experianplc/xorigin",
      executables=executables,
      author="Tabeth Nkangoh | Experian",
      author_email="tabeth.nkangoh@experian.com",
      license="MIT",
      packages=["xorigin"],
      options={"build_exe": build_exe_options},
      keywords=["Cross origin", "Reverse proxy", "CORS Server", "Server"],
)


