import setuptools

# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
with open("README", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='my_minipack',
    version="1.0.0",
    author="ayzapata",
    author_email="ayzapata@student.42.fr",
    description="How to create a package in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    requires_python=">=3.7",
    url="None",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
