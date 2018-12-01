from multimethod import multimethod


class CombinationList:
    def __init__(self, items):
        self.list = items
        self.listItemsComb = [[]]

        for item in items:
            lenght = len(self.listItemsComb)  # preciso salvar o tamanho da lista de combinacoes para nao ter conflito
            for i in range(lenght):
                self.listItemsComb.append(self.listItemsComb[i][:] + [item])  # faco a combinacao com as ja feitas antes

    @multimethod(object, int)
    def which_sum_equals_to(self, value):
        possibilities = []

        for possibilitie in self.listItemsComb:
            if len(possibilitie) > 0 and sum(possibilitie) == value:
                possibilities.append(possibilitie)

        return possibilities

    @multimethod(object, float)
    def which_sum_equals_to(self, value):
        possibilities = []

        for possibilitie in self.listItemsComb:
            if len(possibilitie) > 0 and sum(possibilitie) == value:
                possibilities.append(possibilitie)

        return possibilities

    @multimethod(object, int, int)
    def which_sum_equals_to(self, value, n):
        possibilities = []

        for possibilitie in self.listItemsComb:
            if len(possibilitie) == n and sum(possibilitie) == value:
                possibilities.append(possibilitie)

        return possibilities

    @multimethod(object, float, int)
    def which_sum_equals_to(self, value, n):
        possibilities = []

        for possibilitie in self.listItemsComb:
            if len(possibilitie) == n and sum(possibilitie) == value:
                possibilities.append(possibilitie)

        return possibilities


lista = CombinationList([-25, -10, -7, -3, 2, 4, 8, 10])

print(lista.listItemsComb)
print(lista.which_sum_equals_to(0))
