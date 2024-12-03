from setuptools import setup, find_packages

setup(
    name="FileIntegrityChecker",
    version="1.0.0",
    description="A Python-based file integrity checker that verifies the integrity of files using SHA-256 hashes.",
    author="Mustcode",
    author_email="codermustafa411@gmail.com",
    url="https://github.com/MustcodeQ/FileIntegrityChecker", 
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        
    ],
    entry_points={
        "console_scripts": [
            "file_scanner=src.file_scanner:main",
            "file_checker=src.file_checker:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
