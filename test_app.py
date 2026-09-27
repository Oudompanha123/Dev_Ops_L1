#!/usr/bin/env python3
"""Small test application created by assistant.

Run with: python test_app.py [args...]
"""

import sys


def main():
    print("Hello from test_app!")
    if len(sys.argv) > 1:
        print("Args:", " ".join(sys.argv[1:]))


if __name__ == "__main__":
    main()
