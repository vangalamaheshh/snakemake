__author__ = "Johannes Köster"
__copyright__ = "Copyright 2015, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from setuptools.command.test import test as TestCommand
import sys


if sys.version_info < (3, 3):
    print("At least Python 3.3 is required.\n", file=sys.stderr)
    exit(1)


try:
    from setuptools import setup
except ImportError:
    print("Please install setuptools before installing snakemake.",
          file=sys.stderr)
    exit(1)


# load version info
exec(open("snakemake/version.py").read())


class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])


setup(
    name='snakemake',
    version=__version__,
    author='Johannes Köster',
    author_email='johannes.koester@tu-dortmund.de',
    description=
    'Build systems like GNU Make are frequently used to create complicated '
    'workflows, e.g. in bioinformatics. This project aims to reduce the '
    'complexity of creating workflows by providing a clean and modern domain '
    'specific language (DSL) in python style, together with a fast and '
    'comfortable execution environment.',
    zip_safe=False,
    license='MIT',
    url='https://bitbucket.org/johanneskoester/snakemake',
    packages=['snakemake'],
    entry_points={
        "console_scripts":
        ["snakemake = snakemake:main",
         "snakemake-bash-completion = snakemake:bash_completion"]
    },
    package_data={'': ['*.css', '*.sh', '*.html']},
    tests_require=['nose>=1.3'],
    cmdclass={'test': NoseTestCommand},
    classifiers=
    ["Development Status :: 5 - Production/Stable", "Environment :: Console",
     "Intended Audience :: Science/Research",
     "License :: OSI Approved :: MIT License", "Natural Language :: English",
     "Programming Language :: Python :: 3",
     "Topic :: Scientific/Engineering :: Bio-Informatics"])
