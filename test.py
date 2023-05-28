from antlr4 import *
from finalLexer import finalLexer
from finalParser import finalParser
from finalVisitor import finalVisitor


# TODO code in like a IDLE in python to run block by block or line by line
def main():
    # Create an input stream from the input source
    with open('cef.txt', 'r') as f:
        code = f.read()

    input_stream = InputStream(code)
    # input_stream = InputStream("int fact *= start;")

    # Create a lexer
    f_lexer = finalLexer(input_stream)

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(f_lexer)

    # Create a parser
    f_parser = finalParser(token_stream)

    f_context = f_parser.prog()

    f_visitor = finalVisitor()

    f_visitor.visit(f_context)


if __name__ == '__main__':
    main()
