from setuptools import setup, find_packages

setup(
    name="ode",
    version="0.1.0",
    description="A Python package to download KEGG and HMDB data",
    author="Xiaotao Shen",
    author_email="xiaotao.shen@outlook.com",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
