def number_check(num: int, min: int, max: int):
    """
    >>> number_check(5, 4, 10)
    Простое число
    >>> number_check(6, 0, 7)
    Составное число
    >>> number_check(15, 9, -1)
    Число не входит в заданный диапазон
    """

    divider = 2
    count = 0

    if (num >= min and num <= max):
        for i in range(divider, num - 1):
            if (num% i == 0):
                count += 1
        if (count <= 0):
            print("Простое число")
        else:
            print("Составное число")
    else:
        print("Число не входит в заданный диапазон")

def hex(number: int) -> str:
    """
    >>> hex(5)
    "result='5'"
    >>> hex(1204)
    "result='4B4'"
    """

    HEX = 16
    TEN16 = "A"
    ELEVEN16 = "B"
    TWELVE16 = "C"
    THIRTEEN16 = "D"
    FOURTEEN16 = "E"
    FIFTEEN16 = "F"

    result: str = ""
    while number > 0:
        temp_result: int = number % HEX
        match temp_result:
            case 10:
                result = TEN16 + result
            case 11:
                result = ELEVEN16 + result
            case 12:
                result = TWELVE16 + result
            case 13:
                result = THIRTEEN16 + result
            case 14:
                result = FOURTEEN16 + result
            case 15:
                result = FIFTEEN16 + result
            case _:
                result = str(temp_result) + result
        number //= HEX
    return f'{result=}'

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)