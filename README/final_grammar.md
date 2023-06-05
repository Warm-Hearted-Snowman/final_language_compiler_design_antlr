## final.g4

This file represents the grammar used in the project.

### Grammar Tokens:

- `WS`: Whitespace token that includes spaces, tabs, carriage returns, and newlines.
- `PLUS`: Addition operator.
- `MINUS`: Subtraction operator.
- `MULT`: Multiplication operator.
- `DIV`: Division operator.
- `MOD`: Modulo operator.
- `ASSIGN`: Assignment operator.
- `MULTASGN`: Multiplication assignment operator.
- `ADDASGN`: Addition assignment operator.
- `SUBASGN`: Subtraction assignment operator.
- `DIVASGN`: Division assignment operator.
- `EQ`: Equality comparison operator.
- `NEQ`: Inequality comparison operator.
- `LT`: Less than comparison operator.
- `GT`: Greater than comparison operator.
- `LTE`: Less than or equal to comparison operator.
- `GTE`: Greater than or equal to comparison operator.
- `AND`: Logical AND operator.
- `OR`: Logical OR operator.
- `NOT`: Logical NOT operator.
- `INC`: Increment operator.
- `DEC`: Decrement operator.
- `LPAREN`: Left parenthesis.
- `RPAREN`: Right parenthesis.
- `LBRACE`: Left brace.
- `RBRACE`: Right brace.
- `LBRACK`: Left bracket.
- `RBRACK`: Right bracket.
- `SEMICOLON`: Semicolon.
- `COMMA`: Comma.
- `FORAND`: Bitwise AND operator.
- `IF`: Keyword 'if' for conditional statements.
- `SO`: Keyword 'so' for 'if' statement blocks.
- `ELSE`: Keyword 'else' for 'else' statement blocks.
- `UNTIL`: Keyword 'until' for loop conditions.
- `LOOP`: Keyword 'loop' for loop statements.
- `DO`: Keyword 'do' for loop blocks.
- `RETURN`: Keyword 'return' for returning values from functions.
- `INT_TYPE`: Keyword 'int' for integer type.
- `FLOAT_TYPE`: Keyword 'float' for floating-point type.
- `CHAR_TYPE`: Keyword 'char' for character type.
- `SELECTOR`: Keyword 'selector' for selector statements.
- `SELECT`: Keyword 'select' for select statements.
- `OTHER`: Keyword 'other' for other statements.
- `COLON`: Colon for statement blocks.
- `READ`: Keyword 'read' for input statements.
- `WRITE`: Keyword 'write' for output statements.
- `BREAK`: Keyword 'break' for breaking out of loops.

### Grammar Rules:

- `prog`: Represents the program, consisting of multiple declarations.
- `declaration`: Represents a variable or function declaration.
- `variableDeclaration`: Represents the declaration of variables.
- `variableDeclarator`: Represents the declaration of a single variable, optionally assigned an expression.
- `typeSpecifier`: Represents the type of a variable (int, float, or char).
- `functionDeclaration`: Represents the declaration of a function.
- `parameterList`: Represents a list of function parameters.
- `parameter`: Represents a single function parameter.
- `compoundStatement`: Represents a block of statements enclosed in braces.
- `statement`: Represents a single statement.
- `expressionStatement`: Represents an expression followed by a semicolon.
- `if_soStatement`: Represents an if statement with an optional else statement.
- `untilStatement`: Represents a loop until a condition is true.
- `loopStatement`: Represents a loop with optional initialization, condition, and increment expressions.
- `selectorStatement`: Represents a selector statement with multiple select statements and an optional other statement.
- `selectStatement`: Represents a select statement with a select

 expression and a statement.
- `otherStatement`: Represents the other statement in a selector statement.
- `returnStatement`: Represents a return statement with an optional expression.
- `readStatement`: Represents a read statement for input.
- `writeStatement`: Represents a write statement for output.
- `expression`: Represents an assignment expression.
- `assignmentExpression`: Represents an assignment expression with optional multiple assignments.
- `logicalOrExpression`: Represents a logical OR expression.
- `logicalAndExpression`: Represents a logical AND expression.
- `equalityExpression`: Represents an equality expression with optional multiple equality comparisons.
- `relationalExpression`: Represents a relational expression with optional multiple relational comparisons.
- `additiveExpression`: Represents an additive expression with optional multiple addition or subtraction operations.
- `multiplicativeExpression`: Represents a multiplicative expression with optional multiple multiplication, division, or modulo operations.
- `unaryExpression`: Represents a unary expression, such as increment, decrement, positive, negative, or logical NOT.
- `primaryExpression`: Represents a primary expression, such as a number, character, string, identifier, or sub-expression.

### Grammar Tokens:

- `INT`: Represents an integer value.
- `FLOAT`: Represents a floating-point value.
- `STRING`: Represents a string value.
- `CHAR`: Represents a character value.
- `ID`: Represents an identifier.