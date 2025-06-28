from setuptools import setup, find_packages

setup(
    name="notes-app",
    version="0.1.0",
    description="A CLI tool for adding and reviewing notes",
    author="Your Name",
    py_modules=["main", "db", "utils"],
    install_requires=[
        "rich>=10.0.0",
    ],
    entry_points={
        "console_scripts": [
            "notes=main:main",
        ],
    },
    python_requires=">=3.7",
) 