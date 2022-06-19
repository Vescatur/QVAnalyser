# QVAnalyser
This tool analysis the performance of tools for quantitative verification. It is part of the master thesis of Ivan Hop.

# Installation
The tool has been tested on Ubunutu 20. It should also work on other Linux distributions. We recommend to use WSL in case you are on Windows.

## Dependencies
The analyser requires python 3.10 to run. We used python version 3.10.4. This page describes how to install it on Ubuntu 20 https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/

The analyser requires matplotlib and numpy. Use the following commands to install them

sudo apt-get install python3-distutils
https://stackoverflow.com/questions/69503329/pip-is-not-working-for-python-3-10-on-ubuntu/69527217#69527217
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
python3.10 -m pip install matplotlib

The xelatex package to generate graphs
https://tex.stackexchange.com/questions/179778/xelatex-under-ubuntu

## Tools
The tool requires other the tools to be installed. They do not need to be added to the path variable. We instead use a relative path. They have to be installed in "./Resources/Tools". The analyser will give an error message if a tool has been incorrectly installed.

Modest can be downloaded on the following page.
https://www.modestchecker.net/Downloads/
We used version v3.1.190-g35b359a78 which can be downloaded here.
https://www.modestchecker.net/Downloads/Modest-Toolset-v3.1.190-g35b359a78-linux-x64.zip

Instructions to install Storm are on.
https://www.stormchecker.org/documentation/obtain-storm/build.html

# Run

To start the application use the following commands or the file run.sh.

git pull

cd "Starter"

export PYTHONPATH="../"

python3.10 RunTestBenchmark.py

# Credits

This tool has been based on the tool for QComp made by Tim Quatmann and Michaela Klauck. It can be found on.
https://zenodo.org/record/3965313#.Yqb-lGBByUk

The integration with Storm and plots have been based of work by Matthias Volk

The gitignore is from:
https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a

The Jani models are from the quantitative verification benchmark set which can be found here:
https://qcomp.org/benchmarks/

# License

https://creativecommons.org/licenses/by/4.0/legalcode