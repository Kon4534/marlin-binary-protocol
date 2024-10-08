import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="marlin_binary_protocol",
    version="0.0.7",
    author="Charles Willis",
    author_email="charleswillis3@users.noreply.github.com",
    description="Transfer files with Marlin 2.0 firmware using Marlin Binary Protocol Mark II",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/charleswillis3/marlin-binary-protocol",
    packages=setuptools.find_packages(),
    install_requires=["heatshrink2>=0.12", "pyserial>=3.4", "backports.time_perf_counter; python_version >= '3.11'"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.6, >=3.11',
)
