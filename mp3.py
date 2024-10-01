import itertools

# Custom logical operation functions
def logical_and(p, q):
    return p and q

def logical_or(p, q):
    return p or q

def logical_not(p):
    return not p

def logical_implies(p, q):
    return not p or q  # p -> q is equivalent to ¬p ∨ q

# Function to evaluate the logical expression based on variables and their values
def evaluate_expression(P, Q, expression):
    # Replace variables with their corresponding values
    expression = expression.replace('P', str(P))
    expression = expression.replace('Q', str(Q))
    
    # Replace logical operators with function calls
    expression = expression.replace('and', ' and ')
    expression = expression.replace('or', ' or ')
    expression = expression.replace('not', ' not ')
    expression = expression.replace('->', ' implies ')
    
    # Define a dictionary to map logical operations
    def implies(p, q):
        return logical_implies(p, q)
    
    # Create a safe environment with our custom logical functions
    safe_env = {
        'and': logical_and,
        'or': logical_or,
        'not': logical_not,
        'implies': implies
    }
    
    # Evaluate the expression
    try:
        # Evaluate using Python's eval with our safe environment
        result = eval(expression, {"__builtins__": None}, safe_env)
    except Exception as e:
        result = f"Error: {e}"
    
    return result

# Function to generate and print the truth table
def generate_truth_table():
    try:
        # Hard-coded variables and logical expression
        variables = ['P', 'Q']
        expression = input("Enter the logical expression involving P and Q (e.g., P and Q and not P): ")

        if not expression:
            raise ValueError("Expression cannot be empty.")

        # Generate all combinations of truth values for the variables
        combinations = list(itertools.product([True, False], repeat=len(variables)))

        # Print the table header
        header = " | ".join(variables) + " | Result"
        print(header)
        print("-" * len(header))

        # Evaluate the expression for each combination and print the result
        for combination in combinations:
            P, Q = combination
            result = evaluate_expression(P, Q, expression)
            row = " | ".join(map(str, combination)) + " | " + str(result)
            print(row)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to generate the truth table
generate_truth_table()
