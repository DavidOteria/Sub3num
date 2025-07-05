from setuptools import setup, find_packages

setup(
    name="sub3num",
    version="0.1.0",
    description="Modular subdomain enumeration library for OSINT",
    author="DavidOteria",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "dnspython"
    ],
    python_requires=">=3.10",
)