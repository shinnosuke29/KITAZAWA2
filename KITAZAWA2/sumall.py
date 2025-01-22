#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# (c) 2025 Shinnosuke

import sys

def sum_all():
    total = 0
    for line in sys.stdin:
        try:
            total += int(line.strip())
        except ValueError:
            print(f"Invalid input: {line.strip()}", file=sys.stderr)
            sys.exit(1)
    print(total)

if __name__ == "__main__":
    sum_all()
