from time import time
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print func.__name__, 'took', time() - start
        return result
    return wrapper


@measure
class CombinationList:
    def __init__(self, items):
        self.items = items
        self.combinations = [[]]

        for item in items:
            lenght = len(self.combinations)  # preciso salver o tamanho da lista de combinacoes para nao ter conflito
            for i in xrange(lenght):
                self.combinations.append(self.combinations[i][:] + [item])  # faco a combinacao com as ja feitas antes

        # usando items comprehension

        # for item in items:
        #     self.combinations += [self.combinations[i][:] + [item] for i in xrange(len(self.combinations))]

    def which_sum_equals_to(self, value, *n):
        if len(n) > 0:
            possibilities = [possibilite for possibilite in self.combinations
                             if len(possibilite) in n and sum(possibilite) == value]
        else:
            possibilities = [possibilite for possibilite in self.combinations
                             if len(possibilite) > 0 and sum(possibilite) == value]

        return possibilities


lista = CombinationList([-25, -10, -7, -3, 2, 4, 8, 10])

print(lista.combinations)
print(lista.which_sum_equals_to(0, 2, 3))
