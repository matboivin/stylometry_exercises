"""Setup stylometer."""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = ["matplotlib", "nltk"]

setuptools.setup(name="stylometer",
                 version="1.0.0",
                 author="mboivin",
                 author_email="mboivin@student.42.fr",
                 description="Determine authorship in Python.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://gitlab.com/mboivin/stylometry_exercises",
                 packages=setuptools.find_packages(),
                 install_requires=requirements,
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "Operating System :: OS Independent",
                 ],
                 python_requires=">=3.9",
                 entry_points={
                     "console_scripts":
                     ["stylometer=stylometer.main:entrypoint"]
                 })
