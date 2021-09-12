# lnspec-gen.py

A [lightning network spec](https://github.com/lightningnetwork/lightning-rfc) generator written in python as an experiment.

## Table of Content

- Introduction
- How use it
- How to build
- How to support new languages
- Conclusion
- License

## Introduction

## How to use it

To avoid stupid dependencies recursion performed by pip, we use poetry to pull all the dependencies in the project, so you need to install it.

After that you can use the make to perform the following operation:

- make ARGS='-o tmp.py': to generate all the spec in a file called tmp.py, try make ARGS='--help' to receive help.
- make check: To run the integration testing, but there is nothings to run yet.

## How to build

- poetry install, and after that see "How to run section".

## How to support new languages

TODO see later

## Conclusion

Nothings to conclude here.

## License

TODO


