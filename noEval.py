import itertools
import sys

# Custom logical operation functions
def logical_and(p, q):
    return p and q

def logical_or(p, q):
    return p or q

def logical_not(p):
    return not p

# Function to validate the expression
def validate_expression(expression):
    valid_variables = {"P", "Q"}
    valid_operators = {"and", "or", "not"}
    
    tokens = expression.split()
    
    # Check for valid start
    if not tokens or tokens[0] not in valid_variables and tokens[0] != "not":
        return False

    # Variable to track if the last token was an operator
    last_token_was_operator = True
    
    for token in tokens:
        # Check if token is valid
        if token not in valid_variables and token not in valid_operators and token not in ["True", "False"]:
            return False
        
        # Check for operator placement
        if token in valid_operators:
            # An operator cannot follow another operator
            if last_token_was_operator:
                return False
            last_token_was_operator = True  # Current token is an operator
        else:
            last_token_was_operator = False  # Current token is not an operator
    
    # An expression cannot end with an operator
    if last_token_was_operator:
        return False

    return True# Function to evaluate the expression based on tokens
def evaluate_expression(variables, combination, expression):
    # Create a dictionary of variable values
    context = dict(zip(variables, combination))
    
    # Replace logical operators with spaces to avoid issues with substitution
    expression = expression.replace("and", " and ")
    expression = expression.replace("or", " or ")
    expression = expression.replace("not", " not ")
    
    # Replace variable names with their truth values
    for var, val in context.items():
        expression = expression.replace(var, str(val))
    
    # Now, split the expression into tokens for manual evaluation
    tokens = expression.split()

    # Manually evaluate the tokens, respecting operator precedence
    # Step 1: Handle all 'not' operations first
    i = 0
    while i < len(tokens):
        if tokens[i] == "not":
            # Apply 'not' to the next value
            value = tokens[i + 1] == "True"
            tokens[i] = str(logical_not(value))  # Replace 'not' with the result
            tokens.pop(i + 1)  # Remove the next token as it's been handled
        else:
            i += 1

    # Step 2: Handle all 'and' operations
    i = 0
    while i < len(tokens):
        if tokens[i] == "and":
            # Apply 'and' to the previous and next values
            left = tokens[i - 1] == "True"
            right = tokens[i + 1] == "True"
            tokens[i - 1] = str(logical_and(left, right))  # Replace left operand with result
            tokens.pop(i)  # Remove 'and'
            tokens.pop(i)  # Remove the right operand
        else:
            i += 1

    # Step 3: Handle all 'or' operations
    i = 0
    while i < len(tokens):
        if tokens[i] == "or":
            # Apply 'or' to the previous and next values
            left = tokens[i - 1] == "True"
            right = tokens[i + 1] == "True"
            tokens[i - 1] = str(logical_or(left, right))  # Replace left operand with result
            tokens.pop(i)  # Remove 'or'
            tokens.pop(i)  # Remove the right operand
        else:
            i += 1

    # The final result is the last remaining token
    return tokens[0] == "True"

# Function to generate and print the truth table for two variables
def generate_truth_table():
    # Fixed variables: P and Q
    variables = ["P", "Q"]
    
    expression = sys.stdin.read().strip()
    
    # Check if the expression contains the '->' operator
    if "->" in expression:
        print("Error: Please translate '->' into 'not' and 'or'. For example, 'P -> Q' should be written as 'not P or Q'.\nRefer to the docs: https://yahallo.me/docs")
        return
    
    # Validate the expression
    if not validate_expression(expression):
        print("Error: Invalid expression. Please use only P, Q, and valid logical operators (and, or, not).\nRefer to the docs: https://yahallo.me/docs")
        return
    
    # Generate all combinations of truth values for P and Q
    combinations = list(itertools.product([True, False], repeat=len(variables)))

    # Print the table header (variables and result)
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))

    # Compute and print the truth table for each combination of variable values
    for combination in combinations:
        result = evaluate_expression(variables, combination, expression)
        row = " | ".join(map(str, combination)) + " | " + str(result)
        print(row)


# Run the function to generate the truth table
generate_truth_table() 