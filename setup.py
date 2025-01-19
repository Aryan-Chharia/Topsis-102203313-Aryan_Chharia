from setuptools import setup, find_packages

setup(
    name="Topsis_102203313_Aryan_Chharia",  # Changed to underscore
    version="1.0.0",
    author="Aryan Chharia",
    author_email="aryan.chharia@gmail.com",
    description="A Python package for TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
    ],
    entry_points={
        "console_scripts": [
            "topsis-aryan=Topsis_102203313_Aryan_Chharia.main:main",
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)