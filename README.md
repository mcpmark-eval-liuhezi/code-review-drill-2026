# code-review-drill-2026

Hands-on lab repo for practicing the GitHub pull-request review flow (deliberately unsafe calculator code).

## Background

The "read an expression from the user and pass it straight into `eval()`" habit is a real, recurring footgun in Python code on GitHub — not just a textbook example. Searching GitHub's code search for the classic pattern (`eval(input(` in Python files) returns tens of thousands of hits. Two real repositories that show up in those search results:

1. **[RUB-NDS/PRET](https://github.com/RUB-NDS/PRET)** — Printer Exploitation Toolkit. The file [`pjl.py`](https://github.com/RUB-NDS/PRET/blob/a04bd04b5490ea6a88d11951a55997113f526b77/pjl.py) appears in code search results for the `eval(input(` pattern in Python.
2. **[joaoperfig/GRaNDPapA](https://github.com/joaoperfig/GRaNDPapA)** — Generator of Rad Names from Decent Paper Acronyms. The file [`main.py`](https://github.com/joaoperfig/GRaNDPapA/blob/23fc0dccaf314a43ccc33443947eeb69e787816b/main.py) appears in the same code search results.

The reason `eval()` is dangerous here: it executes arbitrary Python. If the input string is attacker-controlled, `eval()` gives the attacker the ability to run code with your privileges — reading files, making network connections, or worse. Later in this session we'll review a pull request that replaces it with a safe parse.

## What's in this repo

- `calculator.py` on the default branch (`main`) — the *intentionally unsafe* version we will review.
- The branch `fix/safe-input-validation` contains the fixed version, opened as a pull request into `main`.

## Lab flow

1. Read `calculator.py` on `main` and spot the problem.
2. Open the pull request and read the diff.
3. Walk through the review (inline comment + summary) as an example of real reviewer behavior.
4. Discuss the follow-up issue on regression tests.
5. Merge the pull request live during the session.
