import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfminer3k",
    version="1.3.4",
    author="Serhat Can",
    author_email="author@example.com",
    description="Forked from original pdfminer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/canserhat77/pdfminer3k",
    download_url="https://github.com/canserhat77/pdfminer3k/archive/v1.3.4.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[     
          'ply',
      ],
    python_requires='>=3.6',
)