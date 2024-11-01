from setuptools import setup

setup(
    name='brute_force',
    version='1.0',
    description='Simple Brute Force Login Tool',
    py_modules=['brute_force'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'brute_force=brute_force:brute_force_login',
        ],
    },
)
