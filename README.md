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

lnspec-gen.py is a code generator tool, and it is inspired by the tools provided by @rustyrussell. He provided a collection of tools
to generate all the lightning specifications from a CSV file. This tool is an abstract of these tools provided to help the people to 
avoid to start from scratch each time.

What you are waiting for? Start to implement your code generator class for your favorite language. See [the discussion](https://github.com/dart-lightning/lnspec-codegen.py/discussions/3) to see what language
it is already taken and where, so you can help to develop it.

This tool is full inspired by the [bolt12 library](https://github.com/rustyrussell/bolt12) implementation, 
where the code generator it is used to generate js and python code.

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


