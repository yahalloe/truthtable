### ⚡ Requirements
- python 3.

## 🚀 How to Use

### 📃 Input Syntax

1. **Variable Names**:
   - The logical variables are represented by single uppercase letters, specifically `P` and `Q`.
   - You can only use `P` and `Q` as variable names in the current implementation.

2. **Logical Operators**:
   - The following logical operators are supported:
     - `and`: Represents the logical conjunction (AND).
     - `or`: Represents the logical disjunction (OR).
     - `not`: Represents the logical negation (NOT).
	 - `->`: WARNING!: If you want to use this symbol, you need to translate it with `not` and `or` i.e. `P -> Q == not P or Q`

3. **Expression Format**:
   - Users can construct logical expressions using the variables and operators listed above.
   - Expressions must be written in a way that respects the standard logical syntax:
     - Each logical operator should be separated from operands (variables and boolean values) by spaces.
     - For example: 
       - Valid expressions: 
         - `P and Q`
         - `P or not Q`
         - `P and Q and not P`
         - `not P or Q`
     - Invalid expressions (will cause errors):
         - `PandQ` (missing spaces)
         - `P&Q` (using incorrect operator)
         - `notP orQ` (missing spaces)
4. **Examples**:
   - Here are some example expressions that users might enter:
     - `P and Q`: Evaluates to `True` if both `P` and `Q` are `True`.
     - `not P`: Evaluates to `True` if `P` is `False`.
     - `P or Q`: Evaluates to `True` if at least one of `P` or `Q` is `True`.
     - `P and Q and not Q`: Evaluates to `True` only when `P` is `True` and `Q` is `False`.
     - `(P or Q) and not P`: Evaluates to `True` if `Q` is `True` and `P` is `False`.

### Purpose:

The purpose of this code is to generate and print a truth table for logical expressions with two variables, `P` and `Q`, using basic logical operations (`and`, `or`, and `not`). The program evaluates user input expressions and generates the corresponding truth table.

---

### 1. **Imports**

```python
import itertools
```

The `itertools` module is imported to generate all possible combinations of truth values (`True` and `False`) for the variables `P` and `Q`. Specifically, we use the `itertools.product()` function, which creates Cartesian products.

```python
import itertools
```

The `sys` module is imported to read the expressions via a file.

---

### 2. **Logical Operation Functions**

```python
def logical_and(p, q):
    return p and q

def logical_or(p, q):
    return p or q

def logical_not(p):
    return not p
```

These are custom functions that simulate basic logical operations:

- `logical_and(p, q)`: Returns `True` if both `p` and `q` are `True`, otherwise returns `False`.
- `logical_or(p, q)`: Returns `True` if either `p` or `q` is `True`, otherwise returns `False`.
- `logical_not(p)`: Returns the negation of `p` (`True` becomes `False`, and `False` becomes `True`).

These functions are used in place of Python’s built-in logical operators to ensure the logic of the truth table is computed manually.

---

### 3. **Expression Evaluation**

```python
def evaluate_expression(variables, combination, expression):
```

This function takes three arguments:

- `variables`: A list of logical variables (`P` and `Q` in this case).
- `combination`: A tuple representing one combination of truth values for the variables (e.g., `(True, False)`).
- `expression`: The logical expression input by the user (e.g., `P and Q`).

#### a. **Context Creation**

```python
context = dict(zip(variables, combination))
```

The `context` dictionary maps variables to their corresponding truth values. For example, if the variables are `["P", "Q"]` and the combination is `(True, False)`, the `context` will be `{"P": True, "Q": False}`.

#### b. **Replacing Logical Operators**

```python
expression = expression.replace("and", " and ")
expression = expression.replace("or", " or ")
expression = expression.replace("not", " not ")
```

This ensures that logical operators (`and`, `or`, and `not`) have proper spacing so they can be evaluated later. If operators in the user's expression are not properly spaced, this step ensures they are formatted correctly.

#### c. **Substituting Variables**

```python
for var, val in context.items():
    expression = expression.replace(var, str(val))
```

This loop replaces the variables (`P` and `Q`) in the expression with their corresponding truth values from the `context` dictionary. For example, if the expression is `P and Q` and `context` is `{"P": True, "Q": False}`, the expression becomes `True and False`.

#### d. **Manual Evaluation of Tokens**

```python
tokens = expression.split()
```

The expression is split into individual tokens (components) to be evaluated manually. For example, the expression `True and False` becomes `['True', 'and', 'False']`.

#### e. **Logical Evaluation Loop**

The program iterates through each token to compute the final result based on logical operations:

- If the token is `"True"` or `"False"`, it updates the `result` accordingly.
- If the token is a logical operator (`and` or `or`), it stores the operator and applies it to the next truth value.

---

### 4. **Generating the Truth Table**

```python
def generate_truth_table():
```

This function generates and prints the truth table based on user input.

#### a. **User Input**

```python
variables = ["P", "Q"]
expression = input("Enter the logical expression (e.g., P and Q and not P): ")
```

The user is prompted to enter a logical expression involving `P` and `Q`.

#### b. **Generating All Combinations of Truth Values**

```python
combinations = list(itertools.product([True, False], repeat=len(variables)))
```

The `itertools.product([True, False], repeat=2)` function generates all possible combinations of truth values for `P` and `Q`. Since there are two variables, it generates four combinations:

- `(True, True)`
- `(True, False)`
- `(False, True)`
- `(False, False)`

#### c. **Printing the Table Header**

```python
header = " | ".join(variables) + " | Result"
print(header)
print("-" * len(header))
```

The header of the truth table is printed, showing the variables `P`, `Q`, and the result. A separator line is also printed for formatting.

#### d. **Evaluating and Printing Each Row**

```python
for combination in combinations:
    result = evaluate_expression(variables, combination, expression)
    row = " | ".join(map(str, combination)) + " | " + str(result)
    print(row)
```

For each combination of truth values, the `evaluate_expression()` function is called to compute the result. The result is printed along with the corresponding truth values for `P` and `Q`.

---

### 5. **Running the Program**

```python
generate_truth_table()
```

This line starts the program by calling the `generate_truth_table()` function, which handles input, computation, and output.

---

### Example Output:

If the user enters the expression `P and Q or not P`, the truth table might look like this:

```
P | Q | Result
----------------
True | True | True
True | False | True
False | True | True
False | False | False
```

- When `P` is `True` and `Q` is `True`, the result is `True and True or not True`, which evaluates to `True`.
- When `P` is `False` and `Q` is `False`, the result is `False and False or not False`, which evaluates to `False`.

## Error handling

#### `validate_expression` Function

##### Description

The `validate_expression` function validates a logical expression by ensuring it contains only the allowed variables and operators, as well as checking for proper syntax. This function verifies that the expression begins and ends correctly and maintains a valid structure throughout.

##### Function Signature

python

Copy code

`def validate_expression(expression: str) -> bool:`

##### Parameters

- **expression** (str): A string representing the logical expression to be validated. This expression can include the variables `P` and `Q`, the logical operators `and`, `or`, `not`, and the boolean values `True` and `False`.

##### Returns

- **bool**: Returns `True` if the expression is valid (i.e., it contains only the allowed variables and operators), and `False` if it is invalid.

##### Valid Inputs

The following inputs are considered valid:

- Variables:
    - `P`
    - `Q`
- Logical Operators:
    - `and`
    - `or`
    - `not`
- Boolean Values:
    - `True`
    - `False`

##### Invalid Inputs

The function will return `False` for any of the following scenarios:

- The expression contains unsupported variable names (e.g., `R`, `S`).
- The expression includes unsupported logical operators (e.g., `&`, `|`).
- The expression has improperly formatted components (e.g., missing spaces between tokens).
- The expression is empty or contains only whitespace.
- The expression starts with an operator instead of a variable or `not`.
- An operator is placed immediately after another operator.
- The expression ends with an operator.
