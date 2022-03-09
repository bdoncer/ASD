class Node:
    def __init__(self):
        self.children = 0
        self.child = []
        self.res = [-1,-1] #najdluzsza sciezka w dol, 2 najdluzsza
    def rec(self):
        if self.res[0] != -1 and self.res[1] != -1:
            return self.res
        if self.children == 0:
            self.res[0] = 0
            self.res[1] = 0
            return self.res
        wynik1 = 0
        wynik2 = 0
        for dziecko in self.child:
            if dziecko[0].rec()[0] + dziecko[1] > wynik1:
                wynik2 = wynik1
                wynik1 = dziecko[0].rec()[0] + dziecko[1]
            elif dziecko[0].rec()[0] + dziecko[1] > wynik2:
                wynik2 = dziecko[0].rec()[0] + dziecko[1]
        self.res = [wynik1,wynik2]
        return self.res

def nienawidzeasdiwojtka(T):
    for i in range(len(T)):
        T[i].rec()
    wynik = 0
    for i in range(len(T)):
        wynik = max(wynik,T[i].res[0],T[i].res[0]+T[i].res[1])
    print(wynik)







A = Node()
B = Node()
C = Node()
A.children = 2
A.child = [(B,5),(C,-1)]
T = [A,B,C]
nienawidzeasdiwojtka(T)