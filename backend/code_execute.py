from antlr4 import *
import os
import sys

# Import necessary modules
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from backend.finalLexer import finalLexer
from backend.finalParser import finalParser
from backend.finalVisitor import finalVisitor


def code_execute(code):
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