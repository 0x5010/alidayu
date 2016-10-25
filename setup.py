# -*- coding: utf-8 -*-
__editor__ = 0x5010
import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup


def read(fname):
    """
    定义一个read方法，用来读取目录下的长描述
    我们一般是将README文件中的内容读取出来作为长描述，这个会在PyPI中你这个包的页面上展现出来，
    你也可以不用这个方法，自己手动写内容即可，
    PyPI上支持.rst格式的文件。暂不支持.md格式的文件，<BR>.rst文件PyPI会自动把它转为HTML形式显示在你包的信息页面上。
    """
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = "alidayu"
PACKAGES = [
    "alidayu",
    "alidayu.api",
    "alidayu.api.rest",
]
DESCRIPTION = "阿里大于的python接口库，兼容python2和python3."
LONG_DESCRIPTION = ""  # read("README.rst")
KEYWORDS = "alidayu python package"
AUTHOR = "0x5010"
AUTHOR_EMAIL = "0xh4cker@email.com"
URL = "https://github.com/0x5010/alidayu"
VERSION = "1.0.2"
LICENSE = ""


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True,
)


