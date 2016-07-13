"""Setup script for the MineSweeper package.

Author: Yuhuang Hu
Email : duguyue100@gmail.com
"""

from setuptools import setup

classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Science/Research
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.5
Topic :: Utilities
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Scientific/Engineering :: Visualization
Topic :: Software Development :: Libraries :: Python Modules
License :: OSI Approved :: MIT License
"""

try:
    from minesweeper import __about__
    about = __about__.__dict__
except ImportError:
    about = dict()
    exec(open("minesweeper/__about__.py").read(), about)

setup(
    name='minesweeper',
    version=about["__version__"],

    author=about["__author__"],
    author_email=about["__author_email__"],

    url=about["__url__"],
    download_url=about["__download_url__"],

    packages=["minesweeper"],
    package_data={"minesweeper": ["imgs/*.*"]},
    scripts=["scripts/ms-gui.py"],

    classifiers=list(filter(None, classifiers.split('\n'))),
    description="A python Minesweeper with interfaces for \
                 Reinforcement Learning."
)
