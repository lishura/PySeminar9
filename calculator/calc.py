def sum(num_1, num_2):
    return float(num_1) + float(num_2)


def sub(num_1, num_2):
    return float(num_1) - float(num_2)


def mult(num_1, num_2):
    return float(num_1) * float(num_2)


def div(num_1, num_2):
    return float(num_1) / float(num_2)


def exp(num_1, num_2):
    return float(num_1) ** float(num_2)


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

