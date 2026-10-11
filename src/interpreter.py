
from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer


class Interpreter:
    def __init__(self):
        self.variables = {}

    def execute(self, node):
        node_type = node[0]

        if node_type == "PROGRAM":
            for statement in node[1]:
                self.execute(statement)

        elif node_type == "LET":
            name = node[1]
            value = self.evaluate(node[2])
            self.variables[name] = value

        elif node_type == "PRINT":
            value = self.evaluate(node[1])
            print(value)

    def evaluate(self, node):
        node_type = node[0]

        if node_type == "NUMBER":
            return node[1]

        elif node_type == "VARIABLE":
            name = node[1]
            return self.variables[name]

        elif node_type == "BINOP":
            operator = node[1]
            left = self.evaluate(node[2])
            right = self.evaluate(node[3])

            if operator == "+":
                return left + right
            elif operator == "-":
                return left - right
            elif operator == "*":
                return left * right
            elif operator == "/":
                if right == 0:
                    raise ZeroDivisionError(
                        "Cannot divide by zero"
                    )
                return left / right

        raise ValueError(f"Unknown expression: {node}")


if __name__ == "__main__":
    source = """
    let x = 10;
    let y = 20;
    let result = x + y * 2;
    print(result);
    print((10 + 5) * 2);
    """

    tokens = tokenize(source)
    ast = Parser(tokens).parse()

    # Validate the program before executing it.
    SemanticAnalyzer().analyze(ast)

    interpreter = Interpreter()
    interpreter.execute(ast)
