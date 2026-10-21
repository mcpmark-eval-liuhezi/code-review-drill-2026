"""Deliberately unsafe calculator used for a code-review lab.

WARNING: this file is intentionally bad. Do not copy this pattern.
"""


def main():
    expression = input("Enter an arithmetic expression: ")
    # BAD: passes raw user input straight into eval()
    result = eval(expression)
    print(f"{expression} = {result}")


if __name__ == "__main__":
    main()
