from setuptools import setup, find_packages
import irgendsontyphelpers

setup(name = "irgendsontyp-helpers",
      version = irgendsontyphelpers.__version__,
      description = "Sweet helper utilities of all kinds.",
      author = "irgendsontyp",
      url = "https://github.com/irgendsontyp/python-irgendsontyp-helpers.git",
      packages = find_packages()
     )
