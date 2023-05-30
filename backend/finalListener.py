# Generated from final.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .finalParser import finalParser
else:
    from finalParser import finalParser

# This class defines a complete listener for a parse tree produced by finalParser.
class finalListener(ParseTreeListener):

    # Enter a parse tree produced by finalParser#prog.
    def enterProg(self, ctx:finalParser.ProgContext):
        pass

    # Exit a parse tree produced by finalParser#prog.
    def exitProg(self, ctx:finalParser.ProgContext):
        pass


    # Enter a parse tree produced by finalParser#declaration.
    def enterDeclaration(self, ctx:finalParser.DeclarationContext):
        pass

    # Exit a parse tree produced by finalParser#declaration.
    def exitDeclaration(self, ctx:finalParser.DeclarationContext):
        pass


    # Enter a parse tree produced by finalParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:finalParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by finalParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:finalParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by finalParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:finalParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by finalParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:finalParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by finalParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:finalParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by finalParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:finalParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by finalParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:finalParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by finalParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:finalParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by finalParser#parameterList.
    def enterParameterList(self, ctx:finalParser.ParameterListContext):
        pass

    # Exit a parse tree produced by finalParser#parameterList.
    def exitParameterList(self, ctx:finalParser.ParameterListContext):
        pass


    # Enter a parse tree produced by finalParser#parameter.
    def enterParameter(self, ctx:finalParser.ParameterContext):
        pass

    # Exit a parse tree produced by finalParser#parameter.
    def exitParameter(self, ctx:finalParser.ParameterContext):
        pass


    # Enter a parse tree produced by finalParser#compoundStatement.
    def enterCompoundStatement(self, ctx:finalParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by finalParser#compoundStatement.
    def exitCompoundStatement(self, ctx:finalParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by finalParser#statement.
    def enterStatement(self, ctx:finalParser.StatementContext):
        pass

    # Exit a parse tree produced by finalParser#statement.
    def exitStatement(self, ctx:finalParser.StatementContext):
        pass


    # Enter a parse tree produced by finalParser#expressionStatement.
    def enterExpressionStatement(self, ctx:finalParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by finalParser#expressionStatement.
    def exitExpressionStatement(self, ctx:finalParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by finalParser#if_soStatement.
    def enterIf_soStatement(self, ctx:finalParser.If_soStatementContext):
        pass

    # Exit a parse tree produced by finalParser#if_soStatement.
    def exitIf_soStatement(self, ctx:finalParser.If_soStatementContext):
        pass


    # Enter a parse tree produced by finalParser#untilStatement.
    def enterUntilStatement(self, ctx:finalParser.UntilStatementContext):
        pass

    # Exit a parse tree produced by finalParser#untilStatement.
    def exitUntilStatement(self, ctx:finalParser.UntilStatementContext):
        pass


    # Enter a parse tree produced by finalParser#loopStatement.
    def enterLoopStatement(self, ctx:finalParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by finalParser#loopStatement.
    def exitLoopStatement(self, ctx:finalParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by finalParser#selectorStatement.
    def enterSelectorStatement(self, ctx:finalParser.SelectorStatementContext):
        pass

    # Exit a parse tree produced by finalParser#selectorStatement.
    def exitSelectorStatement(self, ctx:finalParser.SelectorStatementContext):
        pass


    # Enter a parse tree produced by finalParser#selectStatement.
    def enterSelectStatement(self, ctx:finalParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by finalParser#selectStatement.
    def exitSelectStatement(self, ctx:finalParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by finalParser#otherStatement.
    def enterOtherStatement(self, ctx:finalParser.OtherStatementContext):
        pass

    # Exit a parse tree produced by finalParser#otherStatement.
    def exitOtherStatement(self, ctx:finalParser.OtherStatementContext):
        pass


    # Enter a parse tree produced by finalParser#returnStatement.
    def enterReturnStatement(self, ctx:finalParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by finalParser#returnStatement.
    def exitReturnStatement(self, ctx:finalParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by finalParser#readStatement.
    def enterReadStatement(self, ctx:finalParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by finalParser#readStatement.
    def exitReadStatement(self, ctx:finalParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by finalParser#writeStatement.
    def enterWriteStatement(self, ctx:finalParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by finalParser#writeStatement.
    def exitWriteStatement(self, ctx:finalParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by finalParser#expression.
    def enterExpression(self, ctx:finalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#expression.
    def exitExpression(self, ctx:finalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:finalParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:finalParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:finalParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:finalParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:finalParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:finalParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#equalityExpression.
    def enterEqualityExpression(self, ctx:finalParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#equalityExpression.
    def exitEqualityExpression(self, ctx:finalParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#relationalExpression.
    def enterRelationalExpression(self, ctx:finalParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#relationalExpression.
    def exitRelationalExpression(self, ctx:finalParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:finalParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:finalParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:finalParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:finalParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#unaryExpression.
    def enterUnaryExpression(self, ctx:finalParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#unaryExpression.
    def exitUnaryExpression(self, ctx:finalParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by finalParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:finalParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by finalParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:finalParser.PrimaryExpressionContext):
        pass



del finalParser