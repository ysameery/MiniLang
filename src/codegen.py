
from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer


class CodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def generate(self, node):
        node_type = node[0]

        if node_type == "PROGRAM":
            for statement in node[1]:
                self.generate(statement)

        elif node_type == "LET":
            name = node[1]
            value = self.generate_expression(node[2])
            self.code.append(f"{name} = {value}")

        elif node_type == "PRINT":
            value = self.generate_expression(node[1])
            self.code.append(f"PRINT {value}")

        return self.code

    def generate_expression(self, node):
        node_type = node[0]

        if node_type == "NUMBER":
            return str(node[1])

        elif node_type == "VARIABLE":
            return node[1]

        elif node_type == "BINOP":
            operator = node[1]
            left = self.generate_expression(node[2])
            right = self.generate_expression(node[3])

            temp = self.new_temp()

            self.code.append(
                f"{temp} = {left} {operator} {right}"
            )

            return temp

        raise ValueError(f"Unknown expression: {node}")


if __name__ == "__main__":
    source = """
    let x = 10;
    let y = 20;
    let result = x + y * 2;
    print(result);
    """

    tokens = tokenize(source)
    ast = Parser(tokens).parse()

    # Validate before generating code.
    SemanticAnalyzer().analyze(ast)

    generator = CodeGenerator()
    intermediate_code = generator.generate(ast)

    print("Three-Address Code:")
    for instruction in intermediate_code:
        print(instruction)
