from cx_Freeze import setup, Executable

executables = [
    Executable('xorigin/xorigin.py')
]

setup(name="xorigin",
      version="0.1",
      description="Easy to use, portable CORS reverse proxy",
      executables=executables,
      author="Tabeth Nkangoh | Experian",
      author_email="tabeth.nkangoh@experian.com",
      license="MIT",
      keywords=["Cross origin", "Reverse proxy", "CORS Server", "Server"])


