# Competitive-Snippet

[![CircleCI](https://circleci.com/gh/wotsushi/competitive-snippet.svg?style=svg)](https://circleci.com/gh/wotsushi/competitive-snippet)
[![codecov](https://codecov.io/gh/wotsushi/competitive-snippet/branch/master/graph/badge.svg)](https://codecov.io/gh/wotsushi/competitive-snippet)

VSCode's snippets for competitive programming

## Requirement

[Pipenv](https://github.com/pypa/pipenv/)

## Installation

```bash
$ git clone git@github.com:wotsushi/competitive-snippet.git
$ cd competitive-snippet
$ pipenv install
```

## Pull Testcase

```bash
$ pipenv run pull SNIPPET_NAME PROBLEM_ID_OF_AOJ
```

Example:

```bash
$ pipenv run pull readi64 ITP1_1_B
```

## Run Test

```bash
$ pipenv run test [-s SNIPPET_NAME]
```

If `-s` is not specified, run tests of all the snippets.

Example1: Run tests of readi64 snippet

```bash
$ pipenv run test -s readi64
```

Example2: Run tests of all the snipets

```bash
$ pipenv run test -s readi64
```

## Build

```bash
$ pipenv run build
```

The built snippet files are located in `competitive-snippet/json/`.
