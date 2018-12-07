from multimethod import multimethod


class CombinationList:
    def __init__(self, items):
        self.list = items
        self.listItemsComb = [[]]

        for item in items:
            lenght = len(self.listItemsComb)  # preciso salvar o tamanho da lista de combinacoes para nao ter conflito
            for i in range(lenght):
                self.listItemsComb.append(self.listItemsComb[i][:] + [item])  # faco a combinacao com as ja feitas antes

        '''
        usando list comprehension
        
        for item in items:
            self.listItemsComb += [self.listItemsComb[i][:] + [item] for i in range(len(self.listItemsComb))]
        '''
        
    @multimethod(object, int)
    @multimethod(object, float)
    def which_sum_equals_to(self, value):
        possibilities = [possibilite for possibilite in self.listItemsComb
                         if len(possibilite) > 0 and sum(possibilite) == value]

        return possibilities

    @multimethod(object, int, int)
    @multimethod(object, float, int)
    def which_sum_equals_to(self, value, n):
        possibilities = [possibilite for possibilite in self.listItemsComb
                         if len(possibilite) == n and sum(possibilite) == value]

        return possibilities


lista = CombinationList([-25, -10, -7, -3, 2, 4, 8, 10])

print(lista.listItemsComb)
print(lista.which_sum_equals_to(0, 3))
