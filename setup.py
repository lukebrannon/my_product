from setuptools import setup, find_packages

version = "1.0.0"

setup(
    name="my-package",
    version=version,
    description="An example Plone add-on",
    long_description=(open("README.txt").read() + "\n" +
                      open("CHANGES.txt").read()),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
    ],
    keywords="",
    author="",
    author_email="",
    url="",
    license="GPL",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
    ],
    extras_require={"test": [
        "plone.app.testing",
        "plone.app.robotframework",
        "robotsuite",
        "robotframework-selenium2library",
    ]},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """
)