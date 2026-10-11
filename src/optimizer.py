
from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer
from codegen import CodeGenerator


class Optimizer:
    def optimize(self, node):
        node_type = node[0]

        # Optimize every statement in the program
        if node_type == "PROGRAM":
            return (
                "PROGRAM",
                [self.optimize(s) for s in node[1]]
            )

        # Optimize variable declarations
        elif node_type == "LET":
            return (
                "LET",
                node[1],
                self.optimize(node[2])
            )

        # Optimize print statements
        elif node_type == "PRINT":
            return (
                "PRINT",
                self.optimize(node[1])
            )

        # Optimize arithmetic expressions
        elif node_type == "BINOP":
            operator = node[1]
            left = self.optimize(node[2])
            right = self.optimize(node[3])

            # Fold expressions containing two numbers
            if left[0] == "NUMBER" and right[0] == "NUMBER":
                a = left[1]
                b = right[1]

                if operator == "+":
                    result = a + b

                elif operator == "-":
                    result = a - b

                elif operator == "*":
                    result = a * b

                elif operator == "/":
                    # Keep division by zero for runtime handling
                    if b == 0:
                        return (
                            "BINOP", operator, left, right
                        )

                    result = a / b

                else:
                    return (
                        "BINOP", operator, left, right
                    )

                # Keep integer arithmetic as integers
                if operator != "/" and isinstance(result, int):
                    return ("NUMBER", result)

                return ("NUMBER", result)

            # Keep expressions that cannot be folded
            return ("BINOP", operator, left, right)

        # Numbers and variables remain unchanged
        return node


if __name__ == "__main__":
    source = """
    let x = 10 + 20 * 2;
    let y = (5 + 5) * 3;
    print(x);
    print(y);
    """

    # 1. Lexical analysis
    tokens = tokenize(source)

    # 2. Syntax analysis
    parser = Parser(tokens)
    ast = parser.parse()

    # 3. Semantic analysis
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)

    # 4. Optimize the AST
    optimizer = Optimizer()
    optimized_ast = optimizer.optimize(ast)

    # 5. Display optimized AST
    print("===== OPTIMIZED AST =====")
    print(optimized_ast)

    # 6. Generate optimized three-address code
    generator = CodeGenerator()
    optimized_code = generator.generate(optimized_ast)

    print("\n===== OPTIMIZED THREE-ADDRESS CODE =====")
    for instruction in optimized_code:
        print(instruction)
