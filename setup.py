from setuptools import setup, find_packages

setup(
    name="phpmap",
    version="1.0.0",
    author="mqz0211",
    description="A PHP vulnerability scanner and exploitation toolkit.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/mqz0211/phpmap",
    packages=find_packages(),
    py_modules=["phpmap"],
    install_requires=[
        "requests>=2.25.0"
    ],
    entry_points={
        "console_scripts": [
            "phpmap=phpmap:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security",
    ],
    python_requires='>=3.6',
)
