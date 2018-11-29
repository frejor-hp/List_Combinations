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
            for j in range(i+1, len(items)):  # j se refere a posicao do proximo item a se combinar com i
                comb = [items[i]]
                for k in range(len(items)-j):  # k se refere a quantidade de itens apos j na combinacao
                    comb.append(items[j+k])
                    self.listItemsComb.append(comb[:])  # devo usar comb[:] para nao ter conflito quando atualizar comb


lista = CombinationList([4, 5, 6])

print(lista.listItemsComb)
