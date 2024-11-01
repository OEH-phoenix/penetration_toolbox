from setuptools import setup

setup(
    name='pinger',
    version='1.0',
    description='Simple Ping Tool',
    py_modules=['pinger'],
    install_requires=['scapy'],
    entry_points={
        'console_scripts': [
            'pinger=pinger:ping_host',
        ],
    },
)
