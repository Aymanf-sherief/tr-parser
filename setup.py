"""This module contains the setup configuration for the tf-parser package"""
import pathlib

import setuptools

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
install_requires = (here / 'requirements.txt').read_text(encoding='utf-8').splitlines()

setuptools.setup(
    name="tf-parser",
    version=0.1,
    author='Ayman Sherief',
    description="Trufla parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aymanf-sherief/tr-parser",
    packages=setuptools.find_namespace_packages(include=["*"]),

    python_requires='>=3.8',

    install_requires=install_requires,

    setup_requires=[
        'pytest-runner',
        'pytest-pylint'
    ],

    entry_points={
        'console_scripts': [
            'tr-parser=tr.tool:parser_tool',
        ],
    },
)
