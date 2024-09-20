from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wuodan",
    version="0.1.0",
    packages=['wuodan'],  
    include_package_data=True,
    install_requires=[
        "tqdm",
        "psutil"
    ],
    entry_points={
        "console_scripts": [
            "wuodan=wuodan.wuodan:main",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
