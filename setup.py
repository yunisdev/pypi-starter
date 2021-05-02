import setuptools
from myp import MYPReader

with open("README.md","r") as fh:
    long_description = fh.read()

myp = MYPReader()

setuptools.setup(
    name=myp.get_data("name"),
    version=myp.get_data("version"),
    author=myp.get_data("author"),
    author_email=myp.get_data("author_email"),
    description=myp.get_data("description"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=myp.get_data("url"),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Natural Language :: English"
    ],
    install_requires=myp.get_dependencies("prod"),
    setup_requires=myp.get_dependencies("prod"),
    python_requires='>=3.6'
)