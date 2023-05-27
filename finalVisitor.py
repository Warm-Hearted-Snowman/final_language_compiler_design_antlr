# Generated from final.g4 by ANTLR 4.9.2
from antlr4 import *

import finalFunctions
from finalParser import finalParser


# This class defines a complete generic visitor for a parse tree produced by finalParser.

class finalVisitor(ParseTreeVisitor):

    def __init__(self):
        self.variables = {}

    # Visit a parse tree produced by finalParser#prog.
    def visitProg(self, ctx: finalParser.ProgContext):
        result = []
        for declaration in ctx.declaration():
            result.append(self.visit(declaration))
        print('\n\n' + str(self.variables))
        return (result)

    # Visit a parse tree produced by finalParser#declaration.
    def visitDeclaration(self, ctx: finalParser.DeclarationContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by finalParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx: finalParser.VariableDeclarationContext):
        type_specifier = self.visit(ctx.typeSpecifier())
        variable_declarators = []
        for variable_declarator in ctx.variableDeclarator():
            variable_declarators.append(self.visitVariableDeclarator(variable_declarator))
        for variable, value in variable_declarators:
            self.variables[variable] = {"type": type_specifier, "value": value}
        return (type_specifier, variable_declarators)

    # Visit a parse tree produced by finalParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx: finalParser.VariableDeclaratorContext):
        variable_name = ctx.ID().getText()
        expression = None
        if ctx.expression():
            expression = self.visit(ctx.expression())
        return (variable_name, expression)

    # Visit a parse tree produced by finalParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx: finalParser.TypeSpecifierContext):
        return ctx.getText()

    # Visit a parse tree produced by finalParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx: finalParser.FunctionDeclarationContext):
        type_specifier = self.visit(ctx.typeSpecifier())
        function_name = ctx.ID().getText()
        parameter_list = []
        if ctx.parameterList():
            parameter_list = self.visit(ctx.parameterList())
        compound_statement = self.visit(ctx.compoundStatement())
        return (type_specifier, function_name, parameter_list, compound_statement)

    # Visit a parse tree produced by finalParser#parameterList.
    def visitParameterList(self, ctx: finalParser.ParameterListContext):
        parameters = []
        for parameter in ctx.parameter():
            parameters.append(self.visit(parameter))
        return (parameters)

    # Visit a parse tree produced by finalParser#parameter.
    def visitParameter(self, ctx: finalParser.ParameterContext):
        type_specifier = self.visit(ctx.typeSpecifier())
        parameter_name = ctx.ID().getText()
        return (type_specifier, parameter_name)

    # Visit a parse tree produced by finalParser#compoundStatement.
    def visitCompoundStatement(self, ctx: finalParser.CompoundStatementContext):
        statements = []
        for statement in ctx.statement():
            statements.append(self.visit(statement))
        return (statements)

    # Visit a parse tree produced by finalParser#statement.
    def visitStatement(self, ctx: finalParser.StatementContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by finalParser#expressionStatement.
    def visitExpressionStatement(self, ctx: finalParser.ExpressionStatementContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        return None

    # Visit a parse tree produced by finalParser#if_soStatement.
    def visitIf_soStatement(self, ctx: finalParser.If_soStatementContext):
        condition = self.visit(ctx.expression())
        if condition:
            so_statement = self.visit(ctx.statement(0))
        else_statement = None
        if ctx.statement(1):
            else_statement = self.visit(ctx.statement(1))

    # Visit a parse tree produced by finalParser#untilStatement.
    def visitUntilStatement(self, ctx: finalParser.UntilStatementContext):
        condition = self.visit(ctx.expression())
        statement = None
        while condition:
            statement = self.visit(ctx.statement())
            condition = self.visit(ctx.expression())

        return ("until", condition, statement)

    # Visit a parse tree produced by finalParser#loopStatement.
    def visitLoopStatement(self, ctx: finalParser.LoopStatementContext):
        global flag
        init_expression = None
        if ctx.expression(0):
            init_expression = self.visit(ctx.expression(0))
        condition = None
        if ctx.expression(1):
            condition = self.visit(ctx.expression(1))
        update_expression = None
        if ctx.expression(2):
            flag = True
        compound_statement = None
        while flag and condition:
            compound_statement = self.visit(ctx.compoundStatement())
            update_expression = self.visit(ctx.expression(2))
            condition = self.visit(ctx.expression(1))
        return ("loop", init_expression, condition, update_expression, compound_statement)

    # Visit a parse tree produced by finalParser#selectorStatement.
    def visitSelectorStatement(self, ctx: finalParser.SelectorStatementContext):
        expression = self.visit(ctx.expression())
        select_statements = []
        for select_statement in ctx.selectStatement():
            select_expression = self.visit(select_statement.expression())
            select_statement_body = self.visit(select_statement.statement())
            select_statements.append((select_expression, select_statement_body))
        other_statement = None
        if ctx.otherStatement():
            other_statement = self.visit(ctx.otherStatement().statement())
        return ("selector", expression, select_statements, other_statement)

    # Visit a parse tree produced by finalParser#selectStatement.
    def visitSelectStatement(self, ctx: finalParser.SelectStatementContext):
        expression = self.visit(ctx.expression())
        statement = self.visit(ctx.statement())
        return (expression, statement)

    # Visit a parse tree produced by finalParser#otherStatement.
    def visitOtherStatement(self, ctx: finalParser.OtherStatementContext):
        return self.visit(ctx.statement())

    # Visit a parse tree produced by finalParser#returnStatement.
    def visitReturnStatement(self, ctx: finalParser.ReturnStatementContext):
        if ctx.expression():
            return ("return", self.visit(ctx.expression()))
        return ("return", None)

    # Visit a parse tree produced by finalParser#readStatement.
    def visitReadStatement(self, ctx: finalParser.ReadStatementContext):
        type_specifier = self.visit(ctx.typeSpecifier())
        variable_name = ctx.ID().getText()
        if self.variables.get(variable_name, -1) != -1:
            if type_specifier == 'int' and self.variables[variable_name]['type'] == 'int':
                new_value = int(input())
                self.variables[variable_name]['value'] = [new_value, 'int']
            elif type_specifier == 'int' and self.variables[variable_name]['type'] == 'float':
                new_value = float(input())
                self.variables[variable_name]['value'] = [new_value, 'float']
            elif type_specifier == 'float' and self.variables[variable_name]['type'] == 'float':
                new_value = float(input())
                self.variables[variable_name]['value'] = [new_value, 'float']
            else:
                raise Exception(f"{variable_name} with {self.variables[variable_name]['type']} not fit with {type_specifier} ")
        else:
            raise Exception(f'No variable with \'{variable_name}\' identified.')

        return ("read", type_specifier, variable_name)

    # Visit a parse tree produced by finalParser#writeStatement.
    def visitWriteStatement(self, ctx: finalParser.WriteStatementContext):
        expressions = []
        for expression in ctx.expression():
            final_state = self.visit(expression)
            expressions.append(final_state)
            if final_state == bool():
                print(final_state)
            elif final_state[1] == 'id':
                try:
                    print(self.variables[final_state[0]]['value'][0], end=' ')
                except:
                    print(self.variables[final_state[0]]['value'], end=' ')
            else:
                print(final_state[0], end=' ')
        print()
        return ("write", expressions)

    # Visit a parse tree produced by finalParser#expression.
    def visitExpression(self, ctx: finalParser.ExpressionContext):
        return self.visit(ctx.assignmentExpression())

    # Visit a parse tree produced by finalParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx: finalParser.AssignmentExpressionContext):
        if ctx.ASSIGN():
            left_expression = self.visit(ctx.logicalOrExpression())
            right_expression = self.visit(ctx.assignmentExpression()[0])
            if self.variables.get(left_expression[0], -1) != -1:
                if left_expression[1]=='id' and right_expression[1]=='id':
                    self.variables[left_expression[0]]['value'] = self.variables[right_expression[0]]['value']
                    return
                elif self.variables[left_expression[0]]["type"] == right_expression[1]:
                    self.variables[left_expression[0]]['value'] = right_expression
                    return
                else:
                    raise Exception('Type Error')
            else:
                raise Exception(f'No variable with \'{left_expression[0]}\' identified.')
        return self.visit(ctx.logicalOrExpression())

    # Visit a parse tree produced by finalParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx: finalParser.LogicalOrExpressionContext):
        if ctx.OR():
            left_expression = self.visit(ctx.logicalAndExpression()[0])
            right_expression = self.visit(ctx.logicalAndExpression()[1])
            return ("logical_or", left_expression, right_expression)
        return self.visit(ctx.logicalAndExpression()[0])

    # Visit a parse tree produced by finalParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx: finalParser.LogicalAndExpressionContext):
        if ctx.AND():
            left_expression = self.visit(ctx.equalityExpression()[0])
            right_expression = self.visit(ctx.equalityExpression()[1])
            return ("logical_and", left_expression, right_expression)
        return self.visit(ctx.equalityExpression()[0])

    # Visit a parse tree produced by finalParser#equalityExpression.
    def visitEqualityExpression(self, ctx: finalParser.EqualityExpressionContext):
        if ctx.EQ():
            left_expression = self.visit(ctx.relationalExpression()[0])
            right_expression = self.visit(ctx.relationalExpression()[1])
            return ("equality", left_expression, right_expression)
        elif ctx.NEQ():
            left_expression = self.visit(ctx.relationalExpression()[0])
            right_expression = self.visit(ctx.relationalExpression()[1])
            return ("inequality", left_expression, right_expression)
        return self.visit(ctx.relationalExpression()[0])

    # Visit a parse tree produced by finalParser#relationalExpression.
    def visitRelationalExpression(self, ctx: finalParser.RelationalExpressionContext):
        if ctx.LT():
            left_expression = self.visit(ctx.additiveExpression()[0])
            right_expression = self.visit(ctx.additiveExpression()[1])
            print(left_expression, right_expression)
            print(self.variables)
            if self.variables.get(left_expression[0], -1) != -1 and self.variables.get(right_expression[0], -1) != -1:
                if (self.variables[left_expression[0]]['type'] != 'string' and self.variables[
                    left_expression[0]]['type'] != 'char') and (
                        self.variables[right_expression[0]]['type'] != 'string' and self.variables[
                    right_expression[0]]['type'] != 'char'):
                    return float(self.variables[left_expression[0]]['value'][0]) < float(
                        self.variables[right_expression[0]]['value'][0])
                else:
                    raise Exception('Type error')
            else:
                raise Exception(f'No variable with \'{left_expression[0]}\' or \'{right_expression[0]}\'')
        elif ctx.GT():
            left_expression = self.visit(ctx.additiveExpression()[0])
            right_expression = self.visit(ctx.additiveExpression()[1])
            if self.variables.get(left_expression[0], -1) != -1 and self.variables.get(right_expression[0], -1) != -1:
                if (self.variables[left_expression[0]]['type'] != 'string' and self.variables[
                    left_expression[0]]['type'] != 'char') and (
                        self.variables[right_expression[0]]['type'] != 'string' and self.variables[
                    right_expression[0]]['type'] != 'char'):
                    return float(self.variables[left_expression[0]]['value'][0]) > float(
                        self.variables[right_expression[0]]['value'][0])
                else:
                    raise Exception('Type error')
            else:
                raise Exception(f'No variable with \'{left_expression[0]}\' or \'{right_expression[0]}\'')
        elif ctx.LTE():
            left_expression = self.visit(ctx.additiveExpression()[0])
            right_expression = self.visit(ctx.additiveExpression()[1])
            if self.variables.get(left_expression[0], -1) != -1 and self.variables.get(right_expression[0], -1) != -1:
                if (self.variables[left_expression[0]]['type'] != 'string' and self.variables[
                    left_expression[0]]['type'] != 'char') and (
                        self.variables[right_expression[0]]['type'] != 'string' and self.variables[
                    right_expression[0]]['type'] != 'char'):
                    return float(self.variables[left_expression[0]]['value'][0]) <= float(
                        self.variables[right_expression[0]]['value'][0])
                else:
                    raise Exception('Type error')
            else:
                raise Exception(f'No variable with \'{left_expression[0]}\' or \'{right_expression[0]}\'')
        elif ctx.GTE():
            left_expression = self.visit(ctx.additiveExpression()[0])
            right_expression = self.visit(ctx.additiveExpression()[1])
            if self.variables.get(left_expression[0], -1) != -1 and self.variables.get(right_expression[0], -1) != -1:
                if (self.variables[left_expression[0]]['type'] != 'string' and self.variables[
                    left_expression[0]]['type'] != 'char') and (
                        self.variables[right_expression[0]]['type'] != 'string' and self.variables[
                    right_expression[0]]['type'] != 'char'):
                    return float(self.variables[left_expression[0]]['value'][0]) >= float(
                        self.variables[right_expression[0]]['value'][0])
                else:
                    raise Exception('Type error')
            else:
                raise Exception(f'No variable with \'{left_expression[0]}\' or \'{right_expression[0]}\'')
        return self.visit(ctx.additiveExpression()[0])

    # Visit a parse tree produced by finalParser#additiveExpression.
    def visitAdditiveExpression(self, ctx: finalParser.AdditiveExpressionContext):
        if ctx.PLUS():
            left_expression = self.visit(ctx.multiplicativeExpression()[0])
            right_expression = self.visit(ctx.multiplicativeExpression()[1])
            # return ("addition", left_expression, right_expression)
            return left_expression + right_expression
        elif ctx.MINUS():
            left_expression = self.visit(ctx.multiplicativeExpression()[0])
            right_expression = self.visit(ctx.multiplicativeExpression()[1])
            print(("subtraction", left_expression, right_expression))
            return ("subtraction", left_expression, right_expression)
        return self.visit(ctx.multiplicativeExpression()[0])

    # Visit a parse tree produced by finalParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx: finalParser.MultiplicativeExpressionContext):
        if ctx.MULT():
            left_expression = self.visit(ctx.unaryExpression()[0])
            right_expression = self.visit(ctx.unaryExpression()[1])
            return ("multiplication", left_expression, right_expression)
        elif ctx.DIV():
            left_expression = self.visit(ctx.unaryExpression()[0])
            right_expression = self.visit(ctx.unaryExpression()[1])
            return ("division", left_expression, right_expression)
        elif ctx.MOD():
            left_expression = self.visit(ctx.unaryExpression()[0])
            right_expression = self.visit(ctx.unaryExpression()[1])
            return ("modulus", left_expression, right_expression)
        elif ctx.MULTASGN():
            left_expression = self.visit(ctx.unaryExpression()[0])
            right_expression = self.visit(ctx.unaryExpression()[1])
            if self.variables.get(left_expression[0], -1) != -1:
                if left_expression[1] == 'id' and right_expression[1] == 'id':
                    self.variables[left_expression[0]]['value'][0] *= self.variables[right_expression[0]]['value'][0]
                    return
                elif self.variables[left_expression[0]]["type"] == right_expression[1]:
                    self.variables[left_expression[0]]['value'][0] *= right_expression[0]
                    return
                else:
                    raise Exception('Type Error')
            else:
                raise Exception(f'No variable with \'{left_expression[0]}\' identified.')
            return ("multiplication_assignment", left_expression, right_expression)
        elif ctx.ADDASGN():
            left_expression = self.visit(ctx.unaryExpression()[0])
            right_expression = self.visit(ctx.unaryExpression()[1])
            return ("addition_assignment", left_expression, right_expression)
        elif ctx.SUBASGN():
            left_expression = self.visit(ctx.unaryExpression()[0])
            right_expression = self.visit(ctx.unaryExpression()[1])
            return ("subtraction_assignment", left_expression, right_expression)
        return self.visit(ctx.unaryExpression()[0])

    # Visit a parse tree produced by finalParser#unaryExpression.
    def visitUnaryExpression(self, ctx: finalParser.UnaryExpressionContext):
        if ctx.MINUS():
            expression = self.visit(ctx.unaryExpression())
            return ("negation", expression)
        elif ctx.NOT():
            expression = self.visit(ctx.unaryExpression())
            return ("logical_not", expression)
        elif ctx.INC():
            expression = self.visit(ctx.primaryExpression())
            self.variables[expression[0]]['value'][0] += 1
            return ("increment", expression)
        elif ctx.DEC():
            expression = self.visit(ctx.primaryExpression())
            return ("decrement", expression)
        return self.visit(ctx.primaryExpression())

    # Visit a parse tree produced by finalParser#primaryExpression.
    def visitPrimaryExpression(self, ctx: finalParser.PrimaryExpressionContext):
        if ctx.INT():
            return [int(ctx.INT().getText()), 'int']
        elif ctx.FLOAT():
            return [float(ctx.FLOAT().getText()), 'float']
        elif ctx.CHAR():
            return [str(ctx.CHAR().getText()), 'char']
        elif ctx.STRING():
            return [str(ctx.STRING().getText()), 'string']
        elif ctx.ID():
            return [ctx.ID().getText(), 'id']
        elif ctx.expression():
            return self.visit(ctx.expression())
        return None
