import os
from codecs import open

from setuptools import find_packages, setup

# Based on https://github.com/pypa/sampleproject/blob/main/setup.py
# and https://python-packaging-user-guide.readthedocs.org/

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
long_description_content_type = "text/markdown"

VERSION = '1.0.0'

setup(
    name="json-test-runner",
    version=VERSION,
    description="create json report with unittest",
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    url="https://github.com/easyhutu/json-test-runner",
    author="easyhutu",
    author_email="1711621009@qq.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Software Development :: Testing",
        "Typing :: Typed",
    ],
    project_urls={
        "Documentation": "https://docs.mitmproxy.org/stable/",
        "Source": "https://github.com/easyhutu/mitmproxy-ban/",
        "Tracker": "https://github.com/easyhutu/mitmproxy-ban/issues/",
    },
    packages=find_packages(
        include=[
            "jsontestrunner",
            "jsontestrunner.*",
        ]
    ),
    entry_points={
        "console_scripts": [
            "jtr = jsontestrunner.__main__:main",
        ]
    },
    python_requires=">=3.6",
    # https://packaging.python.org/en/latest/discussions/install-requires-vs-requirements/#install-requires
    # It is not considered best practice to use install_requires to pin dependencies to specific versions.
)