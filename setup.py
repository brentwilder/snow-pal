from distutils.core import setup, Command


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name="snow-pal",
    packages=[""],
    version="0.1",
    description="Snow inspired palettes for your everyday plots",
    author="Brent Wilder",
    author_email="brentwilder@boisestate.edu",
    url="https://github.com/brentwilder/snow-pal",
    keywords=["snow", "plot", "winter", "graph"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
    cmdclass={'test': PyTest},
    long_description=" Snow-pal is a fast and easy-to-use color palette dictionary based on real life photos from great winter locations.\
        Try snow-pal and create cool snow figures to share with your colleagues. Snow-pal is compatible with Python 2.7x and 3.4+."
)