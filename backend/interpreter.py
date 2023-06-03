from antlr4 import *
from backend.finalLexer import finalLexer
from backend.finalParser import finalParser
from backend.finalVisitor_interpreter_edition import finalVisitor


def run_code(code, variables=None):
    if variables is None:
        variables = {}
    code = "int main(){ %s }" % code

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

    f_visitor.variables = variables

    f_visitor.visit(f_context)

    return [f_visitor.result, f_visitor.variables]
