
[![Python Support](https://img.shields.io/pypi/pyversions/cfg_load.svg)](https://pypi.org/project/cfg_load/)
[![Documentation Status](https://readthedocs.org/projects/cfg_load/badge/?version=latest)](http://cfg-load.readthedocs.io/en/latest/)
[![Build Status](https://travis-ci.org/MartinThoma/cfg_load.svg?branch=master)](https://travis-ci.org/MartinThoma/cfg_load)
[![Coverage Status](https://coveralls.io/repos/github/MartinThoma/cfg_load/badge.svg?branch=master)](https://coveralls.io/github/MartinThoma/cfg_load?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

##### Thanks to https://github.com/MartinThoma/cfg_load best practices

## Installation
* The recommended way to run test_scrape is run the 'scrapescript.py' which is inside the /scraper folder


## Usage

`test_scrape` is intended to be used as a library, or as example for TDD Django


## Features

* Run the script and it will take time to download 500 csv files.
* You load your config file and have it access the LSTM for training.

Not there now, but planned fo the future:

* TODO PATHing setup, location preferences etc.
* TODO Update script for jupyternotebook, python3 and colab imports due to deprications since 2018 when first written
* FIXME  test_clean function needs SOURCE and FILENAME objects to search for themselves, if exists pass, else create.


## In Development

* Add coverage tests
  Check tests with `tox`.
