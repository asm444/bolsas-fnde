from setuptools import setup, find_packages

setup(
    name='bolsasfnde',
    version='0.1',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'bolsasfnde = bolsasfnde.__main__:main',
        ],
    },
)