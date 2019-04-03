# WYRIWYD: What You Run Is What You Document

*Generate maintainable tutorials quickly*

(A hackday project from the Software Sustainability
Institute
[Collaborations Workshop 2019](https://software.ac.uk/cw19).)

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

