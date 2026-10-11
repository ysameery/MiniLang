
from lexer import tokenize


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ("EOF", "")

    def eat(self, expected):
        token = self.current()

        if token[0] != expected:
            raise SyntaxError(
                f"Expected {expected}, got {token[1]}"
            )

        self.pos += 1
        return token

    # program -> statement*
    def parse(self):
        statements = []

        while self.current()[0] != "EOF":
            statements.append(self.statement())

        return ("PROGRAM", statements)

    # statement -> let ID = expression ;
    #            | print ( expression ) ;
    def statement(self):
        if self.current()[0] == "LET":
            self.eat("LET")
            name = self.eat("IDENTIFIER")[1]
            self.eat("EQUALS")
            value = self.expression()
            self.eat("SEMICOLON")

            return ("LET", name, value)

        elif self.current()[0] == "PRINT":
            self.eat("PRINT")
            self.eat("LPAREN")
            value = self.expression()
            self.eat("RPAREN")
            self.eat("SEMICOLON")

            return ("PRINT", value)

        else:
            raise SyntaxError(
                f"Invalid statement: {self.current()[1]}"
            )

    # expression -> term (('+' | '-') term)*
    def expression(self):
        node = self.term()

        while self.current()[0] in ("PLUS", "MINUS"):
            operator = self.current()[1]
            self.pos += 1
            right = self.term()

            node = ("BINOP", operator, node, right)

        return node

    # term -> factor (('*' | '/') factor)*
    def term(self):
        node = self.factor()

        while self.current()[0] in ("MULTIPLY", "DIVIDE"):
            operator = self.current()[1]
            self.pos += 1
            right = self.factor()

            node = ("BINOP", operator, node, right)

        return node

    # factor -> NUMBER | IDENTIFIER | ( expression )
    def factor(self):
        kind, value = self.current()

        if kind == "NUMBER":
            self.pos += 1

            if "." in value:
                return ("NUMBER", float(value))

            return ("NUMBER", int(value))

        elif kind == "IDENTIFIER":
            self.pos += 1
            return ("VARIABLE", value)

        elif kind == "LPAREN":
            self.eat("LPAREN")
            node = self.expression()
            self.eat("RPAREN")
            return node

        else:
            raise SyntaxError(
                f"Invalid expression: {value}"
            )


if __name__ == "__main__":
    source = """
    let x = 10;
    let y = 20;
    let result = x + y * 2;
    print(result);
    """

    tokens = tokenize(source)
    parser = Parser(tokens)
    ast = parser.parse()

    print("Abstract Syntax Tree:")
    print(ast)
