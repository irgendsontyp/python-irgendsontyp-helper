from setuptools import setup, find_packages
import irgendsontyp.helpers

setup(name = "irgendsontyp-helpers",
      version = irgendsontyp.helpers.__version__,
      description = "Sweet helper utilities of all kinds.",
      author = "irgendsontyp",
      url = "https://github.com/irgendsontyp/python-irgendsontyp-helpers.git",
      packages = find_packages()
     )
