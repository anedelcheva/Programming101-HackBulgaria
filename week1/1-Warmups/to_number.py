def to_number(digits):
    result = 0
    for digit in digits:
        result *= 10
        result += digit
    return result
