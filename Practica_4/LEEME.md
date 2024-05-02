# Dynamic programming and recursive algorithms to determine the best newspaper page coverage

## Description
Given a text file containing the dimensions of a newspaper page and a set of articles with their origin coordinates, height, and width, our goal is to determine the combination of articles that covers the maximum area of the page possible. The algorithms employed for this task are a recursive algorithm which systematically explores all different combinations of articles to find the optimal arrangement, and an iterative algorithm designed by following a Dynamic Programming pattern.

## Table of Contents
1. [Directory Description](#directory-description)
2. [Installation](#installation)
3. [Install Dependencies](#install-dependencies)
4. [Usage](#usage)
5. [Running Tests](#running-tests)

## Directory Description
This project is organized with the following structure:

- **buscaLP**: Shell script to run the linear programming algorithm.

- **buscaRyP**: Shell script to run branch and prune algorithm.

- **ejecutar.sh**: streamlines the process of running tests for the newspaper page coverage tool. By executing this script, all tests located in the test/ directory will be automatically executed. This facilitates quick and efficient testing of the functionality and correctness of the tool.

- **src/**: A directory containing all python scripts needed in our backtracking algorithm.
- **test/**: A directory containing all sample test files and scripts for validating the functionality of our solution.
- **svg/**: Upon running the newspaper page coverage tool, SVG files will be generated and stored in this directory. Each SVG file corresponds to a visual representation of the newspaper page with all articles included.
  

These files and directories collectively form the core components of the Newspaper Page Coverage project. The `test` directory contains sample text files that can be used for testing our algorithm.

## Installation
This project requires Python 3.9 or higher. To check your Python version, run:
```bash
python --version
```

## Install Dependencies

Firstly, we have to create a empty environment. To do so, run the following script:
```bash
pip install virtualenv
python<version> -m venv <virtual-environment-name>
source <virtual-environment-name>/bin/activate
```

Now, we can install the necessary dependencies to run this project by running this command:
```bash
pip install -r requirements.txt
```

## Usage
To find the optimal arrangement of articles using the branch and prune algorithm, run the following command:
```bash
./buscaRyP input.txt output.txt
```

To find the optimal arrangement of articles using the linear programming algorithm, run the following command:
```bash
./buscaLP input.txt output.txt
```

## Running Tests
As mentioned before, this project includes automated tests to ensure the correctness of the implementation. The test execution is streamlined through a shell script named `ejecutar.sh`.


### Prerequisites
Before running the tests, ensure that you have the necessary permissions to execute the `ejectuar.sh` script. You can grant execution permission using the following command:
```bash
chmod u+x ejectuar.sh
```
