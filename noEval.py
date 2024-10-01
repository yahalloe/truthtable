import itertools

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
    
    for token in tokens:
        if token not in valid_variables and token not in valid_operators and token not in ["True", "False"]:
            return False
    return True

# Function to evaluate the expression based on tokens
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
    
    # Now, split the expression and manually evaluate it
    tokens = expression.split()

    # Manually evaluate the tokens considering logical precedence
    result = None
    prev_op = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token == "True" or token == "False":
            value = token == "True"
            
            if result is None:
                result = value
            else:
                if prev_op == "and":
                    result = logical_and(result, value)
                elif prev_op == "or":
                    result = logical_or(result, value)
        
        elif token == "not":
            next_token = tokens[i + 1]
            value = next_token == "True"
            result = logical_not(value)
            i += 1  # Skip the next token as it's already handled

        elif token == "and" or token == "or":
            prev_op = token
        
        i += 1

    return result

# Function to generate and print the truth table for two variables
def generate_truth_table():
    # Fixed variables: P and Q
    variables = ["P", "Q"]
    
    while True:
        expression = input("Enter the logical expression (e.g., P and Q and not P): ")
        
        # Check if the expression contains the '->' operator
        if "->" in expression:
            print("Error: Please translate '->' into 'not' and 'or'. For example, 'P -> Q' should be written as 'not P or Q'.\nrefer to the docs: https://yahallo.me/docs")
            continue  # Prompt user again if expression contains '->'
        
        # Validate the expression
        if not validate_expression(expression):
            print("Error: Invalid expression. Please use only P, Q, and valid logical operators (and, or, not).\nrefer to the docs: https://yahallo.me/docs")
            continue  # Prompt user again if expression is invalid
        
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
        break  # Exit the loop if the expression is valid

# Run the function to generate the truth table
generate_truth_table()

