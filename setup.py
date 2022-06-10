import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crunchy_api",
    version="0.0.1",
    author="Mia Chono",
    description="A Python API for Crunchyroll (beta).",
    license="MIT",
    url="https://github.com/mia-chono/crunchy_api",
    install_requires=[
        "requests",
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
)
