from antlr4 import *
from finalLexer import finalLexer
from finalParser import finalParser
from finalVisitor_interpreter_edition import finalVisitor


# TODO code in like a IDLE in python to run block by block or line by line
def run_code(code, variables=None):
    if variables is None:
        variables = {}
    code = "int main(){ %s }" % code
    print(code)
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

    print(f_visitor.variables)

    f_visitor.variables = variables

    print(f_visitor.variables)


    f_visitor.visit(f_context)

    return [f_visitor.result, f_visitor.variables]


for i in run_code('int a=10;write(a);read(int,a);write(a);')[0]:
    print(i, end='')
