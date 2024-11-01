from setuptools import setup

setup(
    name='portscanner',
    version='1.0',
    description='Simple Port Scanner',
    py_modules=['portscanner'],
    install_requires=['python-nmap'],
    entry_points={
        'console_scripts': [
            'portscanner=portscanner:scan_ports',
        ],
    },
)
