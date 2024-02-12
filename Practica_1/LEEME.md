# Huffman's Algorithm for File Compression and Decompression

## Description
This project implements Huffman's algorithm for compressing and decompressing files. Huffman's algorithm is a widely used algorithm for lossless data compression. It creates variable-length codes for data based on their frequency of occurrence, resulting in more efficient storage.

## Table of Contents
1. [Directory_description](#directory_description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Running_Tests](#running_tests)

## Directory Description
This project is organized with the following structure:

- **huf**: Shell script to run Huffman's algorithm and compress or decompress a file.

- **ejecutar.sh**: Shell script to run a set of tests and validate the correction of our project.

- **src/huffman/**: A directory containing all python scripts needed in Huffman's file compression and decompression algorithm.

  - **auxiliaryFunctions.py**: Houses additional functions used to support various aspects of the project.

  - **bitArray.py**: Houses a class to deal with bytes and their binary representation.

  - **generic_tree.py**: Contains the implementation of a generic tree data structure.

  - **huf.py**: The main script for interacting with Huffman's algorithm. Handles compression and decompression functionalities.

  - **huffman.py**: Implements Huffman's algorithm for file compression and decompression.

- **test/**: A directory containing all sample test files and scripts for validating the functionality of the Huffman algorithm.

  - **test.py**: A script for running various tests on the project.

  - **test_files/**: A directory containing all test files.
    - **test0.txt**
    - **test1.txt**
    - **test2.txt**
    - **test3.txt**
    - **test4.txt**
  
  - **time_test/**: A directory containing the necessary scripts to run a time analysis of Huffman's alogrithm.

    - **timeFunctions.py**: Includes functions for measuring and analyzing the runtime performance of the algorithm.

    - **plot.gp**: A gnuplot script to plot the results of the time analysis.

These files and directories collectively form the core components of the Huffman's Algorithm project. The `test` directory contains sample text files that can be used for testing the compression and decompression processes.

## Usage

### Compression
To compress a file using Huffman's algorithm, run the following command:
```bash
./huf  -c input.txt
```

### Decompression
To decompress a file using Huffman's algorithm, run the following command:
```bash
./huf -d input.text.huf
```

## Running Tests
As mentioned before, this project includes automated tests to ensure the correctness of the implementation. The test execution is streamlined through a shell script named `ejecutar.sh`.

### Prerequisites
Before running the tests, ensure that you have the necessary permissions to execute the `ejectuar.sh` script. You can grant execution permission using the following command:
```bash
chmod u+x ejectuar.sh
```
