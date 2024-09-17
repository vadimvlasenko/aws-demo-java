import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="hello_api",
    version="0.0.1",
    description="An example CDK Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "hello_api"},
    packages=setuptools.find_packages(where="hello_api"),
    install_requires=[
        "aws-cdk-lib==2.0.0",
        "constructs>=10.0.0,<11.0.0"
    ],
    python_requires=">=3.6",
)
