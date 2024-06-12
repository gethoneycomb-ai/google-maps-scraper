from setuptools import setup, find_packages

# Define library metadata
NAME = "honeycomb_gmaps"
VERSION = "0.1.0"
AUTHOR = "Jorge C"
AUTHOR_EMAIL = "jorge@example.com"
DESCRIPTION = "This is a short doc"

# Dependencies (listed in requirements.txt)
# (you don't need to specify them here)

# Read requirements from requirements.txt
with open("requirements.txt", "r") as f:
  requirements = f.readlines()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    packages=find_packages(exclude=["tests*"]),  # Look for packages in src
    install_requires=requirements,  # Use requirements from requirements.txt
)
