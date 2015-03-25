def p_score(n):
    if palindrome(n):
        return 1
    else:
        return 1 + p_score(n + int(reverse(n)))
