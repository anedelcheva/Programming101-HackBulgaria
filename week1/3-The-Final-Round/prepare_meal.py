def prepare_meal(number):
    n = 1
    counter = 0
    spam = ''
    eggs = ''
    while number >= (3 ** n):
        if number % (3 ** n) == 0:
            counter = n
        n += 1
    if counter == 0:
        spam = ''
    else:
        spam = counter * 'spam '
    if spam == '' and number % 5 == 0:
        eggs = 'eggs'
    elif spam != '' and number % 5 == 0:
        eggs = 'and eggs'
    return spam + eggs
