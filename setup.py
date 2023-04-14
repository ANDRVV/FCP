from setuptools import setup
import os, codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.2"
DESCRIPTION = 'FCP is a protocol used to route on "channels" and send or receive data.'

setup(
    name = "protofcp",
    version = VERSION,
    url = "https://github.com/ANDRVV/FCP",
    author = "Andrea Vaccaro",
    description = DESCRIPTION,
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages = ["protofcp"],
    license = "Apache 2.0",
    keywords = ["python", "socket", "protocol", "proto", "channel", "scapy", "packet"],
    install_requires = ["scapy"],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]
    )