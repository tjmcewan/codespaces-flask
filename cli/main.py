"""
[changeme]
"""

import sys


def main(input_path):
    # called directly by the flask app
    """
    [Read the input file and return a list of output files]
    """

    with open(input_path, encoding="utf-8") as f:
        lines = f.readlines()  # read the file
    print(lines)

    return ["Octocat.png", "Octocat.png"]  # test output


if __name__ == "__main__":
    # called when run from the command line

    if len(sys.argv) < 2:
        print("Please provide a filepath.")
        sys.exit(1)

    filepath = sys.argv[1]
    main(filepath)
