"""Simple calculator for the code-review lab.

User input is parsed with ast.literal_eval() instead of eval(), so only
literal values (numbers, strings, tuples, lists, dicts, sets, booleans,
and None) are ever evaluated. Anything else raises a clear error.
"""

import ast


def safe_eval(expression: str):
    """Safely evaluate a literal expression.

    Only literal values are accepted. Anything that would require executing
    code (names, attribute access, calls, comprehensions, etc.) raises
    ValueError with an explanation instead of being executed.
    """
    try:
        return ast.literal_eval(expression)
    except (ValueError, SyntaxError) as exc:
        raise ValueError(
            f"Not a safe literal expression: {expression!r}"
        ) from exc


def main():
    expression = input("Enter an arithmetic expression: ")
    # Note: ast.literal_eval() does not evaluate arithmetic operators, so a
    # plain expression like '1 + 2' is not a literal. For the purposes of
    # this lab we keep the interface identical and only accept literals.
    result = safe_eval(expression)
    print(f"{expression} = {result}")


if __name__ == "__main__":
    main()
