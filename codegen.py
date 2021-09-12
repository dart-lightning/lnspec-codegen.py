#! /usr/bin/env python3
import argparse
import sys
import pyln.proto.message
from pyln.proto.message.fundamental_types import FundamentalHexType, IntegerType
from lnspec_codegen.langs import PythonGenerator, JavascriptGenerator, DartGenerator


code_generators = {
    "js": JavascriptGenerator(),
    "py": PythonGenerator(),
    "dart": DartGenerator(),
}


def configure_cmd_args():
    """TODO doc it"""
    parser = argparse.ArgumentParser(
        description="Generate routines to translate message to/from Lightning wire format"
    )
    parser.add_argument("--output", "-o", help="Where to direct output")
    parser.add_argument("--preamble", help="Prepend this file to the output")
    parser.add_argument("--postamble", help="Append this file to the output")
    parser.add_argument(
        "--language", help="Create routines for this language", default="js"
    )
    parser.add_argument(
        "--spec", help="Use these spec CSV files", action="append", default=[]
    )
    parser.add_argument("types", nargs="*", help="Only extract these tags")
    return parser


def run_generator(args, output_file):
    # Using default=['../specs/bolt4.csv', '../specs/bolt12.csv'] does not work, since it appends.
    if len(args.spec) == 0:
        args.spec = ["specs/bolt4.csv", "specs/bolt12.csv"]

    csv_lines = []
    for spec_file in args.spec:
        with open(spec_file, "r") as f:
            csv_lines += f.read().split()

    ns = pyln.proto.message.MessageNamespace()

    # Old version of pyln.proto are missing modern fundamental types.
    if "utf8" not in ns.fundamentaltypes:
        ns.fundamentaltypes["utf8"] = IntegerType("utf8", 1, "B")
    if "point32" not in ns.fundamentaltypes:
        ns.fundamentaltypes["point32"] = FundamentalHexType("point32", 32)
    if "bip340sig" not in ns.fundamentaltypes:
        ns.fundamentaltypes["bip340sig"] = FundamentalHexType("bip340sig", 32)

    ns.load_csv(csv_lines)
    # If they don't specify, generate all
    if len(args.types) == 0:
        args.types = (
            list(ns.tlvtypes.keys())
            + list(ns.subtypes.keys())
            + list(ns.messagetypes.keys())
        )

    generator = code_generators[args.language]
    generator.generate(output_file, ns, args.types)


if __name__ == "__main__":
    parser = configure_cmd_args()
    args = parser.parse_args()

    ofile = None
    if args.output is None:
        ofile = sys.stdout
    else:
        ofile = open(args.output, "wt")

    if args.preamble:
        with open(args.preamble, "r") as f:
            ofile.write(f.read())

    run_generator(args, ofile)

    if args.postamble:
        with open(args.postamble, "r") as f:
            ofile.write(f.read())
