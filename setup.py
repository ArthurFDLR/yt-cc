from pathlib import Path
import re
from setuptools import setup, find_packages


def get_version(file_path: Path):
    with open(file_path, "r") as file:
        file_content = file.read()

    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", file_content, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="yt-cc",
    version=get_version(Path.cwd() / "yt_cc" / "__init__.py"),
    packages=find_packages(),
    install_requires=[
        "jsonschema",
        "pandas",
    ],
    author="Arthur Findelair",
    author_email="arthfind@gmail.com",
    description="Parse JSON3 Youtube Closed Captions",
    license="MIT",
    url="https://github.com/ArthurFDLR/yt-cc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)
