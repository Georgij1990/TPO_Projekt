import Operations
import re


def validate_string(test_string):
    pattern = '^\d+(\.\d+)?$'
    result = re.match(pattern, test_string)
    if result:
        return True
    else:
        return False


def add_transaction(transact_history, expression):
    if len(transact_history) == 5:
        transact_history.append(expression)
        del transact_history[0]
    else:
        transact_history.append(expression)


def eval_expression(expression):
    if '+' in expression:
        parts = expression.split('+')
        if len(parts) != 2:
            raise ValueError("Invalid expression format.")
        if not validate_string(parts[0].strip()) or not validate_string(parts[1].strip()):
            raise ValueError("Not a number")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        return Operations.add(num1, num2)
    elif '-' in expression:
        parts = expression.split('-')
        if len(parts) != 2:
            raise ValueError("Invalid expression format.")
        if not validate_string(parts[0].strip()) or not validate_string(parts[1].strip()):
            raise ValueError("Not a number")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        return Operations.subtract(num1, num2)
    elif '*' in expression:
        parts = expression.split('*')
        if len(parts) != 2:
            raise ValueError("Invalid expression format.")
        if not validate_string(parts[0].strip()) or not validate_string(parts[1].strip()):
            raise ValueError("Not a number")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        return Operations.multiply(num1, num2)
    elif '/' in expression:
        parts = expression.split('/')
        if len(parts) != 2:
            raise ValueError("Invalid expression format.")
        if not validate_string(parts[0].strip()) or not validate_string(parts[1].strip()):
            raise ValueError("Not a number")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        return Operations.divide(num1, num2)
    elif '^' in expression:
        parts = expression.split('^')
        if len(parts) != 2:
            raise ValueError("Invalid expression format.")
        if not validate_string(parts[0].strip()) or not validate_string(parts[1].strip()):
            raise ValueError("Not a number")
        num1 = float(parts[0].strip())
        num2 = float(parts[1].strip())
        return Operations.power(num1, num2)
    elif '%' in expression:
        parts = expression.split('%')
        if len(parts) != 1:
            raise ValueError("Invalid expression format.")
        if not validate_string(parts[0].strip()):
            raise ValueError("Not a number")
        num1 = float(parts[0].strip())
        return Operations.percent(num1)
    elif '!' in expression:
        parts = expression.split('!')
        if expression.count('!') != 1 or expression[-1] != '!':
            raise ValueError("Invalid expression format.")
        if not validate_string(parts[0].strip()):
            raise ValueError("Not a number")
        num = float(parts[0].strip())
        if num < 0:
            raise ValueError("Factorial of a negative number is not defined.")
        return Operations.factorial(num)
    elif 'sqrt' in expression:
        if expression[:4] != 'sqrt' or len(expression) < 6 or expression[4] != '(' or expression[-1] != ')':
            raise ValueError("Invalid expression format.")
        part = expression[5:-1].strip()
        if not validate_string(part):
            raise ValueError("Not a number")
        num = float(part)
        if num < 0:
            raise ValueError("Square root of a negative number is not defined.")
        return Operations.square_root(num)
    elif 'sin' in expression:
        if expression[:3] != 'sin' or len(expression) < 5 or expression[3] != '(' or expression[-1] != ')':
            raise ValueError("Invalid expression format.")
        part = expression[4:-1].strip()
        if not validate_string(part):
            raise ValueError("Not a number")
        num = float(part)
        return Operations.sin_angle(num)
    elif 'cos' in expression:
        if expression[:3] != 'cos' or len(expression) < 5 or expression[3] != '(' or expression[-1] != ')':
            raise ValueError("Invalid expression format.")
        part = expression[4:-1].strip()
        if not validate_string(part):
            raise ValueError("Not a number")
        num = float(part)
        return Operations.cos_angle(num)
    elif expression.startswith('tg'):
        if expression[:2] != 'tg' or len(expression) < 4 or expression[2] != '(' or expression[-1] != ')':
            raise ValueError("Invalid expression format.")
        part = expression[3:-1].strip()
        if not validate_string(part):
            raise ValueError("Not a number")
        num = float(part)
        return Operations.tan_angle(num)
    elif expression.startswith('ctg'):
        if expression[:3] != 'ctg' or len(expression) < 5 or expression[3] != '(' or expression[-1] != ')':
            raise ValueError("Invalid expression format.")
        part = expression[4:-1].strip()
        if not validate_string(part):
            raise ValueError("Not a number")
        num = float(part)
        return Operations.ctg_angle(num)
    else:
        raise ValueError("Unsupported operation or invalid format.")
