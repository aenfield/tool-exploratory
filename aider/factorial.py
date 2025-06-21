#!/usr/bin/env python3
import sys

def factorial(n):
    """Return factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {n} is {factorial(n)}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
