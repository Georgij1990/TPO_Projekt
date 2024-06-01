import Utils

prev_result = 0
transact_history = []


def show_history():
    counter = 1
    history = get_transact_history()
    print('History of transactions:')
    for i in history:
        print(str(counter) + '. ' + i)
        counter += 1


def process_expression(s):
    global prev_result
    global transact_history
    try:
        result = Utils.eval_expression(s)
        prev_result = result
        Utils.add_transaction(transact_history, s + str(f'={result}'))
        print(f"Result: {result}")
        s = ""
        return result
    except Exception as error:
        print(f"Error: {error}")


def get_transact_history():
    return transact_history
