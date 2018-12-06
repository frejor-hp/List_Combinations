class CombinationList:
    def __init__(self, items):
        self.list = items
        self.listItemsComb = [[]]

        for item in items:
            lenght = len(self.listItemsComb)  # preciso salver o tamanho da lista de combinacoes para nao ter conflito
            for i in range(lenght):
                self.listItemsComb.append(self.listItemsComb[i][:] + [item])  # faco a combinacao com as ja feitas antes

    def which_sum_equals_to(self, value, n=0):
        if n > 0:
            possibilities = [possibilite for possibilite in self.listItemsComb
                             if len(possibilite) == n and sum(possibilite) == value]
        else:
            possibilities = [possibilite for possibilite in self.listItemsComb
                             if len(possibilite) > 0 and sum(possibilite) == value]

        return possibilities


lista = CombinationList([-25, -10, -7, -3, 2, 4, 8, 10])

print(lista.listItemsComb)
print(lista.which_sum_equals_to(0))
