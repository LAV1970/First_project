result = None
operand = None
operator = None
wait_for_number = True

while True:
    try:
        user_input = input("Введіть число або оператор (+, -, *, /) або = для результату: ")

        if user_input == "=":
            if result is None or operator is None:
                print("Помилка: Введіть число і оператор перед знаком =.")
            else:
                print("Результат:", result)
                break

        if user_input.replace('.', '', 1).isdigit():
            number = float(user_input)
            if operator is None:
                result = number
            else:
                if operator == '+':
                    result += number
                elif operator == '-':
                    result -= number
                elif operator == '*':
                    result *= number
                elif operator == '/':
                    result /= number
            operator = None
            wait_for_number = False
        elif user_input in ['+', '-', '*', '/']:
            if operator is not None or not wait_for_number:
                print("Помилка: Введіть число перед оператором.")
            else:
                operator = user_input
                wait_for_number = True
        else:
            print("Помилка: Введено неправильний символ.")
    except ValueError:
        print("Помилка: Введено некоректне значення. Введіть число або оператор (+, -, *, /).")
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль недопустиме.")
