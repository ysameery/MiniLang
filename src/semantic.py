
from parser import Parser
from lexer import tokenize


class SemanticAnalyzer:
    def __init__(self):
        # Symbol table stores declared variables.
        self.symbol_table = {}

    def analyze(self, node):
        node_type = node[0]

        if node_type == "PROGRAM":
            for statement in node[1]:
                self.analyze(statement)

        elif node_type == "LET":
            name = node[1]
            value = node[2]

            # Check the value before declaring the variable.
            self.analyze(value)

            if name in self.symbol_table:
                raise NameError(
                    f"Variable '{name}' is already declared"
                )

            self.symbol_table[name] = "number"

        elif node_type == "PRINT":
            self.analyze(node[1])

        elif node_type == "BINOP":
            self.analyze(node[2])
            self.analyze(node[3])

        elif node_type == "VARIABLE":
            name = node[1]

            if name not in self.symbol_table:
                raise NameError(
                    f"Variable '{name}' is not declared"
                )

        elif node_type == "NUMBER":
            pass

        else:
            raise ValueError(
                f"Unknown AST node: {node_type}"
            )

        return self.symbol_table


if __name__ == "__main__":
    source = """
    let x = 10;
    let y = 20;
    let result = x + y * 2;
    print(result);
    """

    tokens = tokenize(source)
    ast = Parser(tokens).parse()

    analyzer = SemanticAnalyzer()
    symbols = analyzer.analyze(ast)

    print("Semantic analysis successful!")
    print("Symbol Table:", symbols)
