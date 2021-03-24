from typing import TypeVar, List, Callable, Union, Iterable

CALC_NUMBER = TypeVar('CALC_NUMBER', int, float, bool)
BOOL_INT = TypeVar('BOOL_INT', int, bool)


def add(a: CALC_NUMBER, b: CALC_NUMBER) -> CALC_NUMBER:
    """
    adds two values

    :param a: first value
    :param b: second value
    :return: result of addition
    """
    return a + b


def sub(a: CALC_NUMBER, b: CALC_NUMBER) -> CALC_NUMBER:
    """
    subtracts value b from a

    :param a: value to be deduct
    :param b: deductible value
    :return: result of subtraction
    """
    return a - b


def neg(a: CALC_NUMBER) -> CALC_NUMBER:
    """
    Negates number

    if Bool will change the boolean vaule

    :param a: value to be negate
    :return: -a
    """
    if a is bool:
        return not a

    return sub(0, a)


def mul(a: CALC_NUMBER, b: CALC_NUMBER) -> CALC_NUMBER:
    """

    multiples values

    :param a: first value
    :param b: second value
    :return: result of multiplication
    """
    return a * b


def div(a: CALC_NUMBER, b: CALC_NUMBER) -> CALC_NUMBER:
    """
    divides a by b
    :raise if b == 0

    :param a: dividend
    :param b: divisor
    :return: quotient
    """
    return a / b


def full_div(a: CALC_NUMBER, b: CALC_NUMBER) -> int:
    """
    floor divides a by b
    :raise if b == 0

    :param a: dividend
    :param b: divisor
    :return: floor quotient
    """
    return a // b


def mod(a: CALC_NUMBER, b: CALC_NUMBER) -> int:
    """
    return the remain of floor division a by b
    :raise if b == 0

    :param a: dividend
    :param b: divisor
    :return: remainder
    """
    return a % b


def pow_(a: CALC_NUMBER, b: CALC_NUMBER) -> CALC_NUMBER:
    """
     power a by b

    :param a: base
    :param b: exponent
    :return: result of power
    """
    return a ** b


def and_(a: BOOL_INT, b: BOOL_INT) -> BOOL_INT:
    """
    bitwise AND on a and B

    :param a: first value
    :param b: second value
    :return: result of bitwise AND
    """
    return a & b


def or_(a: BOOL_INT, b: BOOL_INT) -> BOOL_INT:
    """
    bitwise OR on a and B

    :param a: first value
    :param b: second value
    :return: result of bitwise OR
    """
    return a | b


def xor_(a: BOOL_INT, b: BOOL_INT) -> BOOL_INT:
    """
    bitwise XOR on a and B

    :param a: first value
    :param b: second value
    :return: result of bitwise XOR
    """
    return a ^ b


def shit_left(a: BOOL_INT, b: BOOL_INT) -> int:
    """
    bitwise shift left a by B

    :param a: value to be shift
    :param b: amount of shift
    :return: a shifted left by b amount
    """
    return a >> b


def shit_right(a: BOOL_INT, b: BOOL_INT) -> int:
    """
    bitwise shift right a by B

    :param a: value to be shift
    :param b: amount of shift
    :return: a shifted right by b amount
    """
    return a << b


def fac(a: BOOL_INT) -> int:
    """
    Factorial:  multiply all whole numbers from the a down to 1.

    :param a: value to be factorial
    :return: resulto of factorization
    """
    if a < 1:
        raise ("there is no factorization of vaules that are less then 1", ArithmeticError)

    value = 1
    for i in range(1, a + 1):
        value *= i
    return value


def equal(a: CALC_NUMBER, b: CALC_NUMBER) -> bool:
    """
    Test equality

    :param a: first value
    :param b: second value
    :return: True if there are equal, False otherwise
    """
    return a == b


def not_equal(a: CALC_NUMBER, b: CALC_NUMBER) -> bool:
    """
    Negation of equality <=> neg(equal(a,b))

    :param a: first value
    :param b: second value
    :return: True if there are diferent, False otherwise
    """
    return a != b


def more(a: CALC_NUMBER, b: CALC_NUMBER) -> bool:
    """
    Compare if a is bigger than b

    Bool values will converted to int before operated

    :param a: first value
    :param b: second value
    :return: True if a is bigger then b, False otherwise
    """
    return a > b


def less(a: CALC_NUMBER, b: CALC_NUMBER) -> bool:
    """
    Compare if a is bigger than b

    Bool values will converted to int before operated

    :param a: first value
    :param b: second value
    :return: True if a is bigger then b, False otherwise
    """
    return a < b


def more_eq(a: CALC_NUMBER, b: CALC_NUMBER) -> bool:
    """
    Compare if a is bigger or equal than b

    Bool values will converted to int before operated

    :param a: first value
    :param b: second value
    :return: True if a is bigger or equal then b, False otherwise
    """
    return a >= b


def less_eq(a: CALC_NUMBER, b: CALC_NUMBER) -> bool:
    """
    Compare if a is bigger or equal than b

    Bool values will converted to int before operated

    :param a: first value
    :param b: second value
    :return: True if a is bigger or equal then b, False otherwise
    """
    return or_(less(a, b), equal(a, b))


def apply_operators(expression: List[Union[CALC_NUMBER, Callable]], operators: Iterable[Callable]) -> \
        List[Union[CALC_NUMBER, Callable]]:
    """
    from expression, applies the operators given from para

    :param expression: List of Ints and operators
    :param operators: List of the operators the are desire to be apply
    :return: expression after all the operators given were applied

    :raise if the operator to be aplied is not between to CALC_NUMBER
    """
    new_expression = []
    while operators in expression:
        exp = expression.pop()
        if exp in operators:
            new_expression[-1] = exp(new_expression[-1], expression.pop())
    new_expression.extend(expression)

    return new_expression


def process_operation(eval_str: str) -> CALC_NUMBER:
    """
    Reads String and evaluates and return mathematically result

    Booleans can be represented as T for True and F for False
    doesn't matter the capitalization
    Booleans are consider a operator for the inout but behave as a value

    :raises if the operators aren't separated by spaces
    :raises if two numbers are separated by spaces
    :raises if "open" parentheses doesn't have the "close" correspondent and vice-versa
    :raise if Boolean value don't follow operator input rules

    parenthesis are just to give priority but they don't indicate multiplications or any other operation:
    e.g:
    2 (2 + 3) # This will crash
    as to be writen as:
    2 *(2 + 3)

    there is no need to have spaces between a number and an operator
    spaces around parenthesis are ignored

    :raise if operator doesnt have valid number to be applied on

    :param eval_str: string with te expression to be evaluated
    :return: result of the operation
    """
    # First Step: deal with parentheses
    # pretty much divide what is between the parentheses as a new expression
    # Divide and Conquer
    if '(' in eval_str:
        index_first_parentheses = eval_str.index('(')
        try:
            index_last_parentheses = eval_str[::-1].index(')')
        except ValueError as e:
            raise ("Missing close parentheses", e)

        pa_value = eval_str[index_first_parentheses + 1: len(eval_str) - index_last_parentheses - 1]
        eval_str = eval_str[:index_first_parentheses] + \
                   str(pa_value) + \
                   eval_str[len(eval_str) - index_last_parentheses + 1]

    if ')' in eval_str:
        raise ("Missing open parentheses", ValueError)
    # END OF DEALING WITH PARENTHESES

    # TURN STRING IN TO List[Union[CALC_NUMBER, Callable]] SECTION
    # To be more easily to deal

    expression = []
    num = 0.0
    exp = ''
    decimal = 1

    type_add = 0  # type of the last character added
    # 0 Nothing
    # 1 Number
    # 2 Expression
    # 3 Decimal part of Number

    # Dictionary of the operators
    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div,
        '//': full_div,
        '%': mod,
        '**': pow_,
        '&': and_,
        '|': or_,
        '^': xor_,
        '>>': shit_left,
        '<<': shit_right,
        '!': fac,
        '==': equal,
        '!=': not_equal,
        '>': more,
        '<': less,
        '>=': more_eq,
        '<=': less_eq,
        'T': True,
        'F': False
    }

    for i, chr_ in enumerate(eval_str):

        # space means end of operator or value being read
        if chr_ == ' ':

            # if the last char added was a space, ignore an continue
            if type_add == 0:
                continue

            # if the last char was a digit save number
            elif type_add in [1, 3]:

                if decimal == 1:  # if was a int save as it
                    expression.append(int(num))
                else:  # save float
                    expression.append(num)

                # reset values
                num = 0.0
                decimal = 1

            # if the last char was a operator
            elif type_add == 2:

                # See if operator is a valid one
                try:
                    operation = operators[exp]
                except KeyError as e:
                    raise ("Operation {} unknown".format(exp), e)

                # change subtraction for negation if isn't between to values
                if operation is sub and (not len(expression) or (type(expression[-1]) is (float or int))):
                    operation = neg

                # reset values
                expression.append(operation)
                exp = ''

            # last char was a space
            type_add = 0

        # to know that now we are dealing with a decimal part
        elif chr_ == '.':
            type_add = 3
            decimal = 1

        # deal with digits
        elif chr_.isdigit():
            if type_add == 1:  # int part
                num = num * 10 + int(chr_)
            else:  # float part
                decimal *= 10
                num += int(chr_) / decimal

        # deal with operators char
        else:
            exp += chr_.upper()
            type_add = 2
    # END OF SECTION

    # we simplicity we are going to start from the end to the start of the list
    # so to keep the left right reading we going to reverse list
    expression.reverse()

    # CAlCUlATION SECTION

    # 1º Unitary operators
    newexpresion = []
    while (neg or fac) in expression:
        exp = expression.pop()
        if exp is neg:
            newexpresion.append(exp(expression.pop()))
        elif exp is fac:
            newexpresion[-1] = exp(newexpresion[-1])
    newexpresion.extend(expression)
    expression = newexpresion

    # 2º Power operators
    expression = apply_operators(expression, (pow_,))

    # 3º Mult-version operators
    expression = apply_operators(expression, (mul, div, full_div, mod))

    # 4º Bitwise shifts
    expression = apply_operators(expression, (shit_left, shit_right))

    # 5º Bitwise and, or and xor correspondent
    expression = apply_operators(expression, (and_,))
    expression = apply_operators(expression, (or_,))
    expression = apply_operators(expression, (xor_,))

    # 6º Bool operators
    expression = apply_operators(expression, (less, more, less_eq, more_eq,))
    expression = apply_operators(expression, (equal, not_equal,))
    # END OF CALCULATION SECTION

    # See if there missing operation or strange configurations
    if len(expression) != 1:
        raise (expression, ArithmeticError)
    if type(expression[0]) not in (int, float, bool):
        raise (expression, ArithmeticError)

    return expression[0]
