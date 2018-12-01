# from itertools import combinations


class CombinationList:
    def __init__(self, items):
        self.list = items
        self.listItemsComb = [[]]
        
        '''
        for i in range(len(items)):
            for item in list(combinations(items, i+1)):
                self.listItemsComb.append(list(item))
        '''

        for item in items:
            lenght = len(self.listItemsComb)  # preciso salver o tamanho da lista de combinacoes para nao ter conflito
            for i in range(lenght):
                self.listItemsComb.append(self.listItemsComb[i][:] + [item])  # faco a combinacao com as ja feitas antes

    def which_sum_equals_to(self, value, n):
        possibilities = []

        for possibilitie in self.listItemsComb:
            if len(possibilitie) == n and sum(possibilitie) == value:
                possibilities.append(possibilitie)

        return possibilities


lista = CombinationList([-25, -10, -7, -3, 2, 4, 8, 10])

print(lista.listItemsComb)
print(lista.which_sum_equals_to(0, 3))
