"""Setup to install make importable packages."""

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

import plantstuff as pkg


setup(
    name=pkg.__name__,
    version=pkg.__version__,
    description=pkg.__doc__,
    long_description=__doc__,
    author=pkg.__author__,
    author_email=pkg.__author_email__,
    install_requires=[
        'fabric',
        'pyquery',
        'requests',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
    url=pkg.__url__,
    package_dir=pkg.__pkgdir__,
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    include_package_data=True,
)
