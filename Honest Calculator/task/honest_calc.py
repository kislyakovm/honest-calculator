message = {
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move...",
    4: "Do you want to store the result? (y / n):",
    5: "Do you want to continue calculations? (y / n):",
    6: " ... lazy",
    7: " ... very lazy",
    8: " ... very, very lazy",
    9: "You are",
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
 }

memory = 0


def input_func():
    print(message[0])
    calc = input().split()
    oper = calc[1]

    if calc[0] == 'M':
        global memory
        if memory % 1 == 0:
            x = int(memory)
        else:
            x = memory
    else:
        x = calc[0]
    if calc[2] == 'M':
        try:
            int(memory)
            y = int(memory)
        except ValueError:
            y = memory
    else:
        y = calc[2]

    main(x, oper, y)


def is_digit(a):
    if str(a).isdigit():
        return True
    else:
        try:
            float(a)
            return True
        except ValueError:
            return False


def is_continue():
    print(message[5])
    answer_continue = input()
    if answer_continue == 'y':
        input_func()
    elif answer_continue == 'n':
        return
    else:
        is_continue()


def message_index(msg_index, result):

    print(message[msg_index])
    answer_msg = input()

    if answer_msg == 'y':
        if msg_index < 12:
            msg_index += 1
            message_index(msg_index, result)
        else:
            global memory
            memory = result
            is_continue()
    elif answer_msg == 'n':
        is_continue()
    else:
        message_index(msg_index, result)


def store_result(result):
    print(message[4])
    answer_store = input()
    if answer_store == 'y':
        if is_one_digit(str(result)):
            msg_index = 10
            message_index(msg_index, result)
        else:
            global memory
            memory = result
            is_continue()
    elif answer_store == 'n':
        is_continue()
    else:
        store_result(result)


def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + message[6]
    if (v1 == '1' or v2 == '1') and v3 == '*':
        msg = msg + message[7]
    if (v1 == '0' or v2 == '0') and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + message[8]
    if msg != '':
        msg = message[9] + msg
        print(msg)


def is_one_digit(v):
    try:
        if float(v) % 1 == 0:
            v = int(float(v))
            if -10 < v < 10:
                return True
    except ValueError:
        return False


def main(x, oper, y):
    if is_digit(x) and is_digit(y):
        if oper not in ['+', '-', '*', '/']:
            print(message[2])
            input_func()
        else:
            check(x, y, oper)
            result = 0
            if oper == '+':
                result = float(x) + float(y)

            elif oper == '-':
                result = float(x) - float(y)

            elif oper == '*':
                result = float(x) * float(y)

            else:
                if float(y) != 0:
                    result = float(x) / float(y)

                else:
                    print(message[3])
                    input_func()

            print(result)
            store_result(result)
    else:
        print(message[1])
        input_func()


input_func()
