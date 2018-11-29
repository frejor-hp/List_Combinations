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

        for i in range(len(items)):  # percorro a lista e fixo o item para as combinacoes
            self.listItemsComb.append([items[i]])
            for j in range(1, len(items)-i):  # j se refere a quantidade de itens na combinacao alem do fixado
                for k in range(i+1, len(items)-j+1):  # percorro a lista para a fazer as combinacoes com i limitado por j
                    comb = [items[i]]
                    for x in range(j):  # x se refere a quantidade de itens que devo pegar apos posicao k com max j
                        comb.append(items[k+x])
                    self.listItemsComb.append(comb)  # adiciono o conjunto com o i, o k e os x's itens apos k


lista = CombinationList([4, 5, 6])

print(lista.listItemsComb)
