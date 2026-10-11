cat > README.md <<'EOF'
# MiniLang — Mini Programming Language

MiniLang is a small programming language implementation built
to explore compiler design and programming language concepts.

## Features

- Lexical analysis and tokenization
- Recursive-descent syntax parser
- Abstract Syntax Tree (AST)
- Semantic analysis and symbol table
- Arithmetic expression interpreter
- Three-address code generation
- Constant folding optimization

## Technologies

- Python 3
- Regular expressions
- Compiler design
- Abstract Syntax Trees

## Project Structure

    MiniLang/
    ├── main.py
    ├── src/
    ├── examples/
    ├── tests/
    ├── docs/
    └── README.md

## Getting Started

Clone the repository and enter the project directory.

    git clone YOUR_REPOSITORY_URL
    cd MiniLang

Run an example program:

    python3 main.py examples/hello.mini

Display intermediate code:

    python3 main.py examples/hello.mini --ir

Display tokens:

    python3 main.py examples/hello.mini --tokens

## Example

    let x = 10 + 20 * 2;
    print(x);

Output:

    50

## Learning Objectives

This project explores tokenization, parsing, semantic
validation, interpretation, intermediate representation
and basic compiler optimization.

## Future Improvements

- Conditional statements and loops
- Improved syntax error reporting
- Automated unit tests
- Additional optimization techniques
EOF