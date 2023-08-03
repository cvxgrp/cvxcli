# cvxcli

[![PyPI version](https://badge.fury.io/py/cvxcli.svg)](https://badge.fury.io/py/cvxcli)
[![Apache 2.0 License](https://img.shields.io/badge/License-APACHEv2-brightgreen.svg)](https://github.com/cvxgrp/cvxcli/blob/master/LICENSE)
[![PyPI download month](https://img.shields.io/pypi/dm/cvxcli.svg)](https://pypi.python.org/pypi/cvxcli/)
[![Coverage Status](https://coveralls.io/repos/github/cvxgrp/simulator/badge.png?branch=main)](https://coveralls.io/github/cvxgrp/cvxcli?branch=main)

We demonstrate how to deploy to simple command line apps using pipx.

## Install pipx

The current way to deploy apps is to use [pipx](https://pypa.github.io/pipx/).
The tool creates a virtual environment for each app.

For the installation of pipx please refer to the [pipx documentation](https://pypa.github.io/pipx/installation/).

## Install cvxcli with pipx

cvxcli has been deployed to PyPI like any other Python package. It could be
installed via pip but we advise against that.

cvxcli is not exactly a package you should use as a dependency in your own code.
cvxcli is the home for two apps that are meant to be used from the command line.
So please install via pipx

```bash
pipx cvxcli
```

This command will create a virtual environment for cvxcli and install the package
into that environment.

Please note that you **do not need poetry** to be installed on your machine.

## Using the apps

## Uninstall cvxcli with pipx
