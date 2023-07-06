import pytest


def number_check(num: int, min: int, max: int) -> str:

    divider = 2
    count = 0

    if (num >= min and num <= max):
        for i in range(divider, num - 1):
            if (num% i == 0):
                count += 1
        if (count <= 0):
            result = "Число является простым"
        else:
            result = "Число является составным"
    else:
        result = "Введённое число не входит в заданный диапазон"
    return result

def hex(number: int) -> str:

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

def test_simple_number():
    assert number_check(1, 0, 100000) == "Число является простым"

def test_composite_number():
    assert number_check(99999, 0, 100000) == "Число является составным"

def test_wrong_number():
    assert number_check(100001, 0, 100000) == "Введённое число не входит в заданный диапазон"

def test_dec_to_hex_5():
    assert hex(5) == "result='5'"

def test_dec_to_hex_1204():
    assert hex(1204) == "result='4B4'"



if __name__ == '__main__':
    pytest.main(["-vv"])