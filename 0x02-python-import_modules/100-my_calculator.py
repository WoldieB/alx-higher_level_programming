#!/usr/bin/python3
# 100-my_calculator.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
