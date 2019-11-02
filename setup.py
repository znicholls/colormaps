import versioneer
from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

NAME = "ipcc-wg1-colormaps"
SHORT_DESCRIPTION = "Colour maps used in IPCC WG1"
KEYWORDS = ["ipcc", "wg1", "color", "colour", "maps"]
AUTHORS = [
    ("ozgeyelekci", "email"),
]
URL = "https://github.com/IPCC-WG1/colormaps"
PROJECT_URLS = {
    "Bug Reports": "https://github.com/IPCC-WG1/colormaps/issues",
    # "Documentation": "https://ipcc-wg1-colormaps.readthedocs.io/en/latest",
    "Source": "https://github.com/IPCC-WG1/colormaps",
}
README = "README.rst"

SOURCE_DIR = "src"

# LICENSE = "3-Clause BSD License"
CLASSIFIERS = [
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    # "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
]

REQUIREMENTS_INSTALL = ["pandas", "xlrd"]
REQUIREMENTS_NOTEBOOKS = ["matplotlib", "notebook"]
REQUIREMENTS_TESTS = [
    "codecov",
    "nbval",
    "pytest>=4.0,<5.0",
    "pytest-console-scripts",
    "pytest-cov",
]
REQUIREMENTS_DOCS = [
    "sphinx",
    "sphinx_rtd_theme",
]
REQUIREMENTS_DEPLOY = ["setuptools>=38.6.0", "twine>=1.11.0", "wheel>=0.31.0"]
REQUIREMENTS_DEV = (
    ["black", "bandit", "coverage", "flake8", "isort"]
    + REQUIREMENTS_NOTEBOOKS
    + REQUIREMENTS_TESTS
    + REQUIREMENTS_DOCS
    + REQUIREMENTS_DEPLOY
)


REQUIREMENTS_EXTRAS = {
    "notebooks": REQUIREMENTS_NOTEBOOKS,
    "docs": REQUIREMENTS_DOCS,
    "tests": REQUIREMENTS_TESTS,
    "deploy": REQUIREMENTS_DEPLOY,
    "dev": REQUIREMENTS_DEV,
}

# Get the long description from the README file
with open(README, "r") as f:
    README_LINES = ["IPCC WG1 Color Maps", "===================", ""]
    add_line = False
    for line in f:
        if line.strip() == ".. sec-begin-long-description":
            add_line = True
        elif line.strip() == ".. sec-end-long-description":
            break
        elif add_line:
            README_LINES.append(line.strip())

if len(README_LINES) < 3:
    raise RuntimeError("Insufficient description given")


class IPCCWG1ColorMapsTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        pytest.main(self.test_args)


CMDCLASS = versioneer.get_cmdclass()
CMDCLASS.update({"test": IPCCWG1ColorMapsTest})

setup(
    name=NAME,
    version=versioneer.get_version(),
    description=SHORT_DESCRIPTION,
    long_description="\n".join(README_LINES),
    long_description_content_type="text/x-rst",
    keywords=KEYWORDS,
    author=", ".join([author[0] for author in AUTHORS]),
    author_email=", ".join([author[1] for author in AUTHORS]),
    url=URL,
    project_urls=PROJECT_URLS,
    # license=LICENSE,
    classifiers=CLASSIFIERS,
    packages=find_packages(SOURCE_DIR),
    package_dir={"": SOURCE_DIR},
    install_requires=REQUIREMENTS_INSTALL,
    extras_require=REQUIREMENTS_EXTRAS,
    cmdclass=CMDCLASS,
)