import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statsWaveletFiltr-Tiarles",
    version="0.0.1",
    author="Tiarles Guterres",
    author_email="tiarlesmoralles@hotmail..com",
    description="A statistical signal processing package",
    long_description=("A package that construct an interface " +
        "for filtering wavelet coefficients (by PyWavelets) " + 
        "with statistical methods"),
    long_description_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)