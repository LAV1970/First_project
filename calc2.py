result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input("Введите число или оператор (+, -, *, /) или = для результата: ")

    if user_input == "=":
        break

    if wait_for_number:
        try:
            operand = float(user_input)
            if result is None:
                result = operand
            else:
                if operator == "+":
                    result = result + operand
                elif operator == "-":
                    result = result - operand
                elif operator == "*":
                    result = result * operand
                elif operator == "/":
                    if operand == 0:
                        print("Ошибка: Деление на ноль.")
                    else:
                        result = result / operand
            wait_for_number = False
        except ValueError:
            print("Ошибка: Введено неправильный символ")
    else:
        if user_input in ("/", "+", "-", "*"):
            operator = user_input
            wait_for_number = True
        else:
            print("Ошибка: Введите оператор")

print(f"Результат: {result}")

