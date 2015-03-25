def reverse(element):
    return element[::-1]


def palindrome(obj):
    obj = str(obj)
    return obj == reverse(obj)
