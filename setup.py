from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

with open(here / "requirements.txt") as fp:
    install_requires = fp.read().strip().split("\n")
install_requires = [p.strip() for p in install_requires]

setup(
    name="korpus-processor",
    version="0.1.0",
    author="seopbo, doohae",
    author_email="bsk0130@gmail.com, rick7213@gmail.com",
    description="Framework of pre-processors for Korean open-sourced corpus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="NLP LM KO Data",
    license="Apache",
    url="https://github.com/lassl/korpus-processor",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=install_requires,  # External packages as dependencies
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
