
import re

TOKEN_SPEC = [
    ("NUMBER",    r"\d+(\.\d+)?"),
    ("LET",       r"\blet\b"),
    ("PRINT",     r"\bprint\b"),
    ("IDENTIFIER",r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("EQUALS",    r"="),
    ("PLUS",      r"\+"),
    ("MINUS",     r"-"),
    ("MULTIPLY",  r"\*"),
    ("DIVIDE",    r"/"),
    ("LPAREN",    r"\("),
    ("RPAREN",    r"\)"),
    ("SEMICOLON", r";"),
    ("SKIP",      r"[ \t\n]+"),
    ("MISMATCH",  r"."),
]

TOKEN_REGEX = "|".join(
    f"(?P<{name}>{pattern})"
    for name, pattern in TOKEN_SPEC
)


def tokenize(source):
    tokens = []

    for match in re.finditer(TOKEN_REGEX, source):
        kind = match.lastgroup
        value = match.group()

        if kind == "SKIP":
            continue

        if kind == "MISMATCH":
            raise SyntaxError(
                f"Unexpected character: {value}"
            )

        tokens.append((kind, value))

    return tokens


if __name__ == "__main__":
    code = "let x = 10 + 20; print(x);"

    for token in tokenize(code):
        print(token)
