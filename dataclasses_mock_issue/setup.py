import setuptools

setuptools.setup(
    name="sample",
    version="0.0.1",
    author="Subhayan Bhattacharya",
    author_email="subhayan.here@gmail.com",
    description="Test package to test the issues with dataclasses during mocking",
    package_dir={"": "src"},
    packages=["sample"],
    install_requires=["flask_restful"],
    python_requires=">=3.7",
)
