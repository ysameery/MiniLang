
import argparse
import sys
from pathlib import Path

# Allow imports from the src directory
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer
from interpreter import Interpreter
from codegen import CodeGenerator
from optimizer import Optimizer


def run_program(source, show_tokens=False,
                show_ast=False, show_ir=False,
                optimize=True):

    # Phase 1: Lexical analysis
    tokens = tokenize(source)

    if show_tokens:
        print("\n=== TOKENS ===")
        for token in tokens:
            print(token)

    # Phase 2: Syntax analysis
    ast = Parser(tokens).parse()

    if show_ast:
        print("\n=== ORIGINAL AST ===")
        print(ast)

    # Phase 3: Semantic analysis
    SemanticAnalyzer().analyze(ast)

    # Phase 4: Optimization
    if optimize:
        ast = Optimizer().optimize(ast)

    if show_ast and optimize:
        print("\n=== OPTIMIZED AST ===")
        print(ast)

    # Phase 5: Intermediate code generation
    if show_ir:
        generator = CodeGenerator()
        instructions = generator.generate(ast)

        print("\n=== THREE-ADDRESS CODE ===")
        for instruction in instructions:
            print(instruction)

    # Phase 6: Execution
    print("\n=== PROGRAM OUTPUT ===")
    interpreter = Interpreter()
    interpreter.execute(ast)


def main():
    parser = argparse.ArgumentParser(
        description="MiniLang compiler and interpreter"
    )

    parser.add_argument(
        "file",
        help="Path to a .mini source file"
    )

    parser.add_argument(
        "--tokens",
        action="store_true",
        help="Display tokens"
    )

    parser.add_argument(
        "--ast",
        action="store_true",
        help="Display the syntax tree"
    )

    parser.add_argument(
        "--ir",
        action="store_true",
        help="Display three-address code"
    )

    parser.add_argument(
        "--no-opt",
        action="store_true",
        help="Disable constant folding"
    )

    args = parser.parse_args()

    file_path = Path(args.file)

    try:
        source = file_path.read_text(encoding="utf-8")

        run_program(
            source,
            show_tokens=args.tokens,
            show_ast=args.ast,
            show_ir=args.ir,
            optimize=not args.no_opt
        )

    except (SyntaxError, NameError, ZeroDivisionError,
            ValueError) as error:
        print(f"\nMiniLang error: {error}", file=sys.stderr)
        sys.exit(1)

    except OSError as error:
        print(f"\nFile error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
