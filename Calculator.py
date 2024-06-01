import Calculate
from pynput import keyboard
import sys

results = []
transact_history = Calculate.get_transact_history()
current_index = -1


def run_calculator():
    listener = keyboard.Listener(on_press=navigate_on_history)
    listener.start()
    while True:
        print(
            """
        Available operations:
        1. Add: <number> + <number>; Subtract: <number> - <number>; Multiply: <number> * <number>; Divide: <number> / <number>
        2. Power <number> ^ <power>; Square root: sqrt(<number>); Percent: <number>%; Factorial: <number>!
        3. Sin: sin(<angle in rad>); Cos: cos(<angle in rad>); Tan: tg(<angle in rad>); Cot: ctg(<angle in rad>)
        4. history
        5. exit
        """
        )
        if len(results) == 0:
            print('Type 1 to exit.')
            expression = input("Enter an expression > ")
            if expression == '1':
                break
            expression = expression.replace(" ", "")
            result = Calculate.process_expression(expression)
            if result is None:
                continue
            results.append(result)
        else:
            print("Proceed with typing an expression; "
                  "If you want to start new transaction, type - 0; "
                  "For square root -  type 'sqrt'; "
                  "For sin - type 'sin'; for cos - 'cos'; for tan - 'tg'; and for ctg = 'ctg'.\n"
                  "Type 1 to exit.")
            prev_result = results.pop()
            print(f'{prev_result}', end=" ")
            expr = input().strip()
            if expr == '0':
                results.clear()
                continue
            elif expr == '1':
                break
            elif expr == 'sqrt':
                expression = f'sqrt({str(prev_result)})'
            elif expr == 'sin':
                expression = f'sin({str(prev_result)})'
            elif expr == 'cos':
                expression = f'cos({str(prev_result)})'
            elif expr == 'tg':
                expression = f'tg({str(prev_result)})'
            elif expr == 'ctg':
                expression = f'ctg({str(prev_result)})'
            else:
                expression = str(prev_result) + expr
            expression = expression.replace(" ", "")
            result = Calculate.process_expression(expression)
            if result is None:
                continue
            results.append(result)


def navigate_on_history(key):
    global current_index
    try:
        if key == keyboard.Key.up:
            if current_index > -len(transact_history):
                current_index -= 1
            display_transaction(transact_history[current_index])
        elif key == keyboard.Key.down:
            if current_index < -1:
                current_index += 1
            display_transaction(transact_history[current_index])
    except Exception as error:
        print(error)


def display_transaction(transaction):
    sys.stdout.write('\r' + ' ' * 80)
    sys.stdout.write('\rHistory of transactions: ' + transaction)
    sys.stdout.flush()
