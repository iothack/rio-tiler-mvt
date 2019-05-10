"""Setup for rio-tiler-mvt."""

from setuptools.extension import Extension
from setuptools import setup, find_packages
from Cython.Build import cythonize

import numpy

# Runtime requirements.
inst_reqs = ["numpy", "vtzero"]

vt = "vector-tile-base @ git+https://github.com/mapbox/vector-tile-base"
extra_reqs = {
    "test": [vt, "rio-tiler", "pytest", "pytest-cov"],
    "dev": [vt, "rio-tiler", "pytest", "pytest-cov", "pre-commit"],
}

ext_options = {"include_dirs": [numpy.get_include()]}
ext_modules = cythonize(
    [
        Extension(
            "rio_tiler_mvt.mvt",
            ["rio_tiler_mvt/mvt.pyx"],
            **ext_options
        )
    ]
)

setup(
    name="rio-tiler-mvt",
    version="0.0.1b",
    description=u"""A rio-tiler plugin to encode tile array to MVT""",
    python_requires=">=3",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    keywords="COG MVT mapbox vectortile GIS",
    author=u"Vincent Sarago",
    author_email="vincent@developmentseed.org",
    url="https://github.com/cogeotiff/rio-tiler-mvt",
    license="BSD",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=inst_reqs,
    extras_require=extra_reqs,
    ext_modules=ext_modules,
)