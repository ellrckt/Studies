import pytest
import sys
sys.path.append('../laaab')

from main import Binary, FloatingPoint


def test_decimal_to_binary_positive():
    binary = Binary(number=10)
    assert binary.binary == '00001010'


def test_decimal_to_binary_negative():
    binary = Binary(number=-10)
    assert binary.binary == '00001010'


def test_check():
    result = [1, 1, 1, 1, 2, 1, 1, 1, 1]
    bn = Binary(4)
    result = bn.check(result)
    assert result == [2, 1, 1, 1, 0, 0, 0, 0, 2]


def test_binary_to_direct():
    binary = Binary(number=-10)
    assert binary.direct_code == '10001010'


def test_decimal_to_binary():
    binary_instance = Binary(number=10)
    assert binary_instance.binary == '00001010'


def test_binary_to_reverse():
    binary_instance = Binary(number=-10)
    assert binary_instance.reverse_code == '11110101'


def test_binary_to_complement():
    binary_instance = Binary(number=-10)
    assert binary_instance.complement_code == '11110110'


def test_reverse_to_direct():
    binary_instance = Binary(reverse_code='10000101')
    assert binary_instance.direct_code == '11111010'


def test_direct_to_decimal():
    binary_instance = Binary(reverse_code='11110101')
    assert binary_instance.number-10


def test_addition():
    binary1 = Binary(number=10)
    binary2 = Binary(number=5)
    result = binary1 + binary2
    assert result.number==15


def test_multiplication():
    binary1 = Binary(number=10)
    binary2 = Binary(number=5)
    result = binary1 * binary2
    assert result.number == 50


def test_division():
    binary1 = Binary(number=10)
    binary2 = Binary(number=5)
    result = binary1 / binary2
    assert result== '00000010.00000'


def test_decimal_to_binary2():
    float_instance = FloatingPoint(number=10.5)
    assert float_instance.result == '01000001001010000000000000000000'


def test_get_fractional_part():
    float_instance = FloatingPoint(number=10.5)
    assert float_instance.fractional_part == '1'


def test_float_to_binary_representation():
    float_instance = FloatingPoint(number=10.5)
    assert float_instance.float == '00001010.10000000000000000000000'


def test_shift_point_to_range():
    float_instance = FloatingPoint(number=10.5)
    assert float_instance.scientific_notation == '00001.01010000000000000000000000'


def test_addition2():
    float1 = FloatingPoint(number=10.5)
    float2 = FloatingPoint(number=5.25)
    result = float1 + float2
    assert result == '01000001011111000000000000000000'


def adition3():
    float_point = FloatingPoint(number=2.5)
    float_point2 = FloatingPoint(number=1.2)
    b = float_point+float_point2
    print(b, '\n01000000011011001100110011001101')


def test_addition3():
    float1 = FloatingPoint(number=13.5)
    float2 = FloatingPoint(number=79.9)
    result = float1 + float2
    assert result == '01000010101110101100110011001100'


def test_addition4():
    float1 = FloatingPoint(number=0.5)
    float2 = FloatingPoint(number=176.4)
    result = float1 + float2
    assert result == '01000011001100001110011001100110'


def test_check2():
    result = [1, 1, 1, 1, 2, 1, 1, 1, 1]
    float1 = FloatingPoint(4.5)
    result = float1.check(result)
    assert result == [1, 1, 1, 1, 0, 0, 0, 0, 0, 1]


def test_decimal_to_binary_representation_positive():
    float_point = FloatingPoint(number=10.5)
    assert float_point.result == '01000001001010000000000000000000'


def test_decimal_to_binary_representation_negative():
    float_point = FloatingPoint(number=-10.5)
    assert float_point.result == '11000001001010000000000000000000'


if __name__ == '__main__':
    pytest.main()
