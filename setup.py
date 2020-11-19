import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="elegant_io",
    version="0.0.1",
    author="Jiaying Wang",
    author_email="jiaying@sjzu.edu.cn",
    description="An elegant io package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jiayingwang/elegant_io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)