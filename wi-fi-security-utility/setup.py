from setuptools import setup, find_packages

setup(
    name="wi-fi-security-utility",
    version="1.0.0",
    description="Ethical Wi-Fi security testing toolkit",
    author="Security Researcher",
    packages=find_packages(),
    install_requires=[
        "scapy>=2.5.0",
        "pycryptodome>=3.15.0",
        "colorama>=0.4.6",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "wifi-scanner=src.scanner:main",
        ],
    },
)