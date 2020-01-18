import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

about: dict = {}
with open(os.path.join(here, "woodworkbase", "__VERSION__.py")) as f:
    exec(f.read(), about)

setup(
    name="woodworkbase",
    version=about["__version__"],
    description="Backend API for woodworkbase project.",
    url="https://github.com/5uper5hoot/woodworkbase",
    author="Peter Schutt",
    author_email="peter_schutt@bigpond.com",
    license=None,
    packages=find_packages(
        include=["woodworkbase", "woodworkbase.*"]
    ),
    zip_safe=False,
    install_requires=[],
)