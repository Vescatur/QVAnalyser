# QVAnalyser
This tool analysis the performance of tools for quantitative verification. It is part of the master thesis of Ivan Hop. We use analyser to refer to QVAnalyser.

# Installation
The analyser is supported on Ubunutu 20. The tool should work on other Linux distributions. We recommend to use WSL in case you are on Windows.

## Dependencies
The analyser requires python 3.10 to run. We used python version 3.10.4. This page describes how to install it on Ubuntu 20 https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/

## Tools
The analyser requires the tools to be installed. They do not need to be added to the path variable. We instead use a relative path. They have to be installed in "./Resources/Tools". The analyser will give an error message if a tool has been incorrectly installed.

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
python3 RunTestBenchmark.py

# Credits

This tool has been based on the work of Tim Quatmann, Michaela Klauck and Matthias Volk. The work of Tim Quatmann and Michaela Klauck can be found on.
https://gist.github.com/MOOOWOOO/3cf91616c9f3bbc3d1339adfc707b08a
