#!/usr/bin/python3
# 2-args.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
