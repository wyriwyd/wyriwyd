[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Build Status](https://travis-ci.com/wyriwyd/wyriwyd.svg?branch=master)](https://travis-ci.com/wyriwyd/wyriwyd)
[![codecov](https://codecov.io/gh/wyriwyd/wyriwyd/branch/master/graph/badge.svg)](https://codecov.io/gh/wyriwyd/wyriwyd)
[![Collaborations Workshop 2019](https://img.shields.io/badge/developed%20at-CollabW19-red.svg)](https://software.ac.uk/cw19)


# WYRIWYD: What You Run Is What You Doc

*Generate maintainable tutorials quickly*

(A hackday project from the Software Sustainability
Institute
[Collaborations Workshop 2019](https://software.ac.uk/cw19).)

![The wyriwyd dragon logo](wyriwyd-dragon.png)

## Introduction

Tutorials and how-to guides are a key component of software
documentation. While many tools exist for automatic generation of API
reference material, tutorials can be intimidating to set up and easily
fall behind software changes. WYRIWYD is intended to help novice
software developers build and maintain tutorials for simple
command-line programs.

## Workflow

The main components of WYRIWYD are:

- A wizard which creates a bare-bones tutorial by watching the
  developer use their own code in a shell.

- A markdown file convention which allows users to comfortably insert
  further comments and make corrections/updates as the code changes.

- A testing utility which verifies that the tutorial is correct for
  the current code version. If continuous integration (e.g. Travis CI)
  is used, this test can be added to the repository hooks for futher
  peace of mind.

## Installation
```
pip install git+https://github.com/wyriwyd/wyriwyd.git#egg=wyriwyd
```

## Usage
To generate markdown documentation, run the `wyriwydzard` command.
After entering the name of the document to generate, keep entering your commands in the prompt. A bare-bones tutorial will be
generated in markdown, which you can expand with explanations of the commands.

To test existing markdown documentation, just run the `wyriwyd-test` command over the markdown file.  Note if the commands in the documentation assume you will be in a given directory, then you should `cd` there first.
```bash
cd examples/
wyriwyd-test sample.md
```
And if everything is ok, you should see:
```output
Everything looks ok!!
```

For more support on the testing tool, use `--help`
```bash
wyriwyd-test --help
```
```output
usage: wyriwyd-test [-h] [-r] [-e EMPTY] infile

positional arguments:
  infile                The path to the input markdown file

optional arguments:
  -h, --help            show this help message and exit
  -r, --raise-error     Raise an exception at the first error
  -e EMPTY, --empty EMPTY
                        If the Markdown file contains commands without a
                        following output, and the command when runs produces
                        output, treat this as an error
```

## Incuding into continuous integration:
We even run the command itself over this README:
* https://github.com/wyriwyd/wyriwyd/blob/master/.travis.yml

There's also an example project at https://github.com/wyriwyd/wyriwyd-live-demo
