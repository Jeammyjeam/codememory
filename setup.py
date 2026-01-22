from setuptools import setup, find_packages

setup(
    name="codememory",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI Code Review Assistant with Context Memory",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/codememory",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "gitpython>=3.1.40",
        "click>=8.1.7",
        "rich>=13.7.0",
        "pyyaml>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            "codememory=codememory.__main__:main",
        ],
    },
)
