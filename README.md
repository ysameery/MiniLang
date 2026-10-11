# MiniLang — Mini Programming Language

A lightweight programming language implementation built with Python to explore compiler design, syntax analysis, interpretation, and code optimization.

## Overview

MiniLang is an educational language project that processes a custom programming language through lexical analysis, parsing, semantic validation, intermediate code generation, and interpretation. It also includes a basic constant-folding optimizer.

The project demonstrates how source code can be transformed into a structured representation, validated, optimized, and executed.

## Features

- **Lexical Analysis:** Converts source code into tokens using regular expressions.
- **Syntax Analysis:** Parses tokens using a recursive-descent parser.
- **Abstract Syntax Tree (AST):** Represents expressions and statements as a structured tree.
- **Semantic Analysis:** Checks variable declarations and detects duplicate declarations.
- **Interpreter:** Evaluates arithmetic expressions and executes supported statements.
- **Intermediate Code Generation:** Produces three-address code for supported expressions.
- **Constant Folding:** Simplifies arithmetic expressions containing constants.
- **Command-Line Interface:** Runs `.mini` source files and provides options to inspect compiler stages.

## Technology Stack

- Python 3
- Regular Expressions
- Recursive-Descent Parsing
- Abstract Syntax Trees
- Compiler Design Fundamentals

## Architecture

```text
MiniLang Source (.mini)
          |
          v
   Lexical Analyzer
          |
          v
       Parser
          |
          v
    Abstract Syntax Tree
          |
          v
  Semantic Analyzer
          |
          v
  Constant-Folding Optimizer
          |
          v
 Intermediate Code Generator
          |
          v
      Interpreter
          |
          v
     Program Output
```

The current implementation uses an AST for interpretation and intermediate-code generation. The interpreter executes the supported language constructs directly.

## Project Structure

```text
MiniLang/
├── main.py
├── src/
│   ├── lexer.py
│   ├── parser.py
│   ├── semantic.py
│   ├── interpreter.py
│   ├── codegen.py
│   └── optimizer.py
├── examples/
│   └── hello.mini
├── tests/
├── docs/
├── README.md
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3 installed on your system
- Git

### 1. Clone the repository

```bash
git clone https://github.com/ysameery/MiniLang.git
cd MiniLang
```

### 2. Run the example program

```bash
python3 main.py examples/hello.mini
```

### 3. Inspect compiler stages

Display tokens:

```bash
python3 main.py examples/hello.mini --tokens
```

Display the AST:

```bash
python3 main.py examples/hello.mini --ast
```

Display three-address code:

```bash
python3 main.py examples/hello.mini --ir
```

Display tokens, AST, and intermediate code together:

```bash
python3 main.py examples/hello.mini --tokens --ast --ir
```

Run without constant-folding optimization:

```bash
python3 main.py examples/hello.mini --no-opt --ir
```

## Example Program

Create a file named `examples/hello.mini` containing:

```text
let x = 10 + 20 * 2;
let y = (5 + 5) * 3;

print(x);
print(y);
```

Expected program output:

```text
50
30
```

The multiplication is evaluated before addition, and parentheses control expression precedence.

## Example Intermediate Representation

For the expression:

```text
let result = 10 + 20 * 2;
print(result);
```

The optimized intermediate code is expected to resemble:

```text
result = 50
PRINT result
```

## Current Limitations

- The language currently supports numeric expressions, variable declarations, and print statements.
- Conditional statements, loops, functions, and user-defined types are not implemented yet.
- The semantic analyzer currently uses a simple symbol table and does not implement a full type system or nested scopes.
- Intermediate code is generated as a textual representation; native machine-code generation is not implemented.
- Automated test coverage is a work in progress.

## Future Improvements

- Add conditional statements and loops.
- Improve syntax and semantic error reporting.
- Introduce automated unit tests.
- Add more compiler optimizations.
- Expand the grammar and language documentation.
- Explore bytecode or native-code generation.

## Learning Objectives

This project explores the fundamental stages of a language implementation, including tokenization, recursive-descent parsing, AST construction, semantic validation, interpretation, intermediate representations, and optimization.

## Author

**Sameer Kumar**

GitHub: [@ysameery](https://github.com/ysameery)

---

*MiniLang is an educational project developed to explore programming language implementation and compiler design.*