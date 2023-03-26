# setup.py
from setuptools import setup, find_packages

setup(
    name='plsp',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # 依存関係のあるパッケージをここに記述します。
    ],
    entry_points={
        'console_scripts': [
            'plsp = plsp.plsp:main',
        ],
    },
)