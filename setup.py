from setuptools import setup, find_packages

setup(
    name="notes-app-cli",
    version="0.1.0",
    description="A CLI tool for adding and reviewing notes",
    author="Tejaaswini",
    py_modules=["main", "db", "utils", "notes_semantic_db"],
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