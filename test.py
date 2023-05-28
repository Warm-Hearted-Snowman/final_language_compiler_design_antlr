from antlr4 import *
from finalLexer import finalLexer
from finalParser import finalParser
from finalListener import finalListener
from finalVisitor import finalVisitor


class MyListener(finalListener):
    def enterVariableDeclaration(self, ctx):
        # Implement your logic for entering variable declaration
        type_specifier = ctx.typeSpecifier().getText()
        variable_declarators = ctx.variableDeclarator()

        for variable_declarator in variable_declarators:
            variable_id = variable_declarator.ID().getText()
            expression = variable_declarator.expression()
            if expression:
                value = self.visitExpression(expression)
                # Perform the necessary actions with the variable id and value
            else:
                pass
        # Handle variable declaration without an assignment

    def enterFunctionDeclaration(self, ctx):
        # Implement your logic for entering function declaration
        type_specifier = ctx.typeSpecifier().getText()
        function_id = ctx.ID().getText()
        parameter_list = ctx.parameterList()
        compound_statement = ctx.compoundStatement()

        # Process the function declaration

    def enterCompoundStatement(self, ctx):
        # Implement your logic for entering compound statement
        statements = ctx.statement()

        for statement in statements:
            self.visitStatement(statement)

    def enterIf_soStatement(self, ctx):
        # Implement your logic for entering if-so statement
        expression = ctx.expression()
        statement = ctx.statement(0)
        else_statement = ctx.statement(1) if ctx.ELSE() else None

        # Process the if-so statement

    def enterUntilStatement(self, ctx):
        # Implement your logic for entering until statement
        expression = ctx.expression()
        statement = ctx.statement()

        # Process the until statement

    def enterLoopStatement(self, ctx):
        # Implement your logic for entering loop statement
        expressions = ctx.expression()
        statement = ctx.statement()

        # Process the loop statement

    def enterSelectorStatement(self, ctx):
        # Implement your logic for entering selector statement
        expression = ctx.expression()
        select_statements = ctx.selectStatement()
        other_statement = ctx.otherStatement()

        # Process the selector statement

    def enterSelectStatement(self, ctx):
        # Implement your logic for entering select statement
        expression = ctx.expression()
        statement = ctx.statement()

        # Process the select statement

    def enterOtherStatement(self, ctx):
        # Implement your logic for entering other statement
        statement = ctx.statement()

        # Process the other statement

    def enterReturnStatement(self, ctx):
        # Implement your logic for entering return statement
        expression = ctx.expression()

        # Process the return statement

    def enterReadStatement(self, ctx):
        # Implement your logic for entering read statement
        type_specifier = ctx.typeSpecifier().getText()
        variable_id = ctx.ID().getText()

        # Process the read statement

    def enterWriteStatement(self, ctx):
        # Implement your logic for entering write statement
        expressions = ctx.expression()

        # Process the write statement

    def enterExpressionStatement(self, ctx):
        # Implement your logic for entering expression statement
        expression = ctx.expression()

        if expression:
            self.visitExpression(expression)

    def enterAssignmentExpression(self, ctx):
        # Implement your logic for entering assignment expression
        left = self.visitLogicalOrExpression(ctx.logicalOrExpression(0))
        right = self.visitLogicalOrExpression(ctx.logicalOrExpression(1))

        # Process the assignment expression

    def enterLogicalOrExpression(self, ctx):
        # Implement your logic for entering logical OR expression
        left = self.visitLogicalAndExpression(ctx.logicalAndExpression(0))
        right = self.visitLogicalAndExpression(ctx.logicalAndExpression(1))

        # Process the logical OR expression

    def enterLogicalAndExpression(self, ctx):
        # Implement your logic for entering logical AND expression
        left = self.visitEqualityExpression(ctx.equalityExpression(0))
        right = self.visitEqualityExpression(ctx.equalityExpression(1))

        # Process the logical AND expression

    def enterEqualityExpression(self, ctx):
        # Implement your logic for entering equality expression
        left = self.visitRelationalExpression(ctx.relationalExpression(0))
        right = self.visitRelationalExpression(ctx.relationalExpression(1))
        operator = ctx.getChild(1).getText()

        # Process the equality expression

    def enterRelationalExpression(self, ctx):
        # Implement your logic for entering relational expression
        left = self.visitAdditiveExpression(ctx.additiveExpression(0))
        right = self.visitAdditiveExpression(ctx.additiveExpression(1))
        operator = ctx.getChild(1).getText()

        # Process the relational expression

    def enterAdditiveExpression(self, ctx):
        # Implement your logic for entering additive expression
        left = self.visitMultiplicativeExpression(ctx.multiplicativeExpression(0))
        right = self.visitMultiplicativeExpression(ctx.multiplicativeExpression(1))
        operator = ctx.getChild(1).getText()

        # Process the additive expression

    def enterMultiplicativeExpression(self, ctx):
        # Implement your logic for entering multiplicative expression
        left = self.visitUnaryExpression(ctx.unaryExpression(0))
        right = self.visitUnaryExpression(ctx.unaryExpression(1))
        operator = ctx.getChild(1).getText()

        # Process the multiplicative expression

    def enterUnaryExpression(self, ctx):
        # Implement your logic for entering unary expression
        if ctx.getChildCount() == 2:
            operator = ctx.getChild(0).getText()
            operand = self.visitUnaryExpression(ctx.unaryExpression())

            # Process unary operator and operand

        else:
            self.visitPrimaryExpression(ctx.primaryExpression())

    def enterPrimaryExpression(self, ctx):
        # Implement your logic for entering primary expression
        if ctx.INT():
            value = int(ctx.INT().getText())
            # Process integer value

        elif ctx.FLOAT():
            value = float(ctx.FLOAT().getText())
            # Process float value

        elif ctx.CHAR():
            value = ctx.CHAR().getText()
            # Process character value

        elif ctx.STRING():
            value = ctx.STRING().getText()
            # Process string value

        elif ctx.ID():
            variable_id = ctx.ID().getText()
            # Process identifier

        elif ctx.expression():
            self.visitExpression(ctx.expression())
            # Process expression within parentheses


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

    d = f_visitor.visit(f_context)

    # print(d)
    #
    # # Create a listener/visitor
    # listener = MyListener()
    #
    # # Set the listener/visitor on the parser
    # f_parser.addParseListener(listener)

    # Start the parsing process at the "prog" rule
    # tree = f_parser.prog()
    tree = f_parser.prog()

    # Perform actions based on the parsed input
    # ... implement your actions in YourExprListener class

    # Optionally, print the parse tree for debugging
    # print(tree.toStringTree(ruleNames=f_parser.ruleNames))


if __name__ == '__main__':
    main()
