class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(str(self.amount))

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)


class BatchBill:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self, bills):
        total_sum = 0
        for bill in bills:
            total_sum += int(bill)
        return total_sum

    def __getitem__(self, index):
        return self.bills[index]

    def __int__(self):
        return self.total(bills)


def group(list):
    sublist = []
    counter = 1
    result = []
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            counter += 1
        else:
            sublist = counter * [list[i]]
            result.append(sublist)
            sublist = []
            counter = 1
    result.append([list[len(list) - 1]] * counter)
    return result


class CashDesk:

    def __init__(self):
        self.money = []

    def take_money(self, currency):
        self.money.append(currency)

    def total(self):
        result = 0
        for money in self.money:
            result += int(money)
        return result

    def inspect(self):
        self.bills = group(bills)
        occurrences = []
        for bill in self.bills:
            occurrences.append(len(bill))
        for i in range(len(self.bills)):
            print (str(int(self.bills[i][0])) + '$ bills -', occurrences[i])

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total())  # 390
desk.inspect()
