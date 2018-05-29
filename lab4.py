import numpy as np

class wierzcholek:


    def __init__(self, name):
        self.sasiedzi = []
        self.nazwa = name
        self.odleglosc = 100



    def dodaj_sasiad(self, sasiad,waga):
        self.sasiedzi.append([sasiad, waga])

class graf:
    A = wierzcholek('A')
    B = wierzcholek('B')
    C = wierzcholek('C')
    D = wierzcholek('D')
    E = wierzcholek('E')
    F = wierzcholek('F')
    G = wierzcholek('G')

    def __init__(self):


        self.A.dodaj_sasiad(self.C, 1)
        self.A.dodaj_sasiad(self.D, 2)
        self.B.dodaj_sasiad(self.C, 2)
        self.B.dodaj_sasiad(self.F, 2)
        self.C.dodaj_sasiad(self.A, 1)
        self.C.dodaj_sasiad(self.D, 1)
        self.C.dodaj_sasiad(self.B, 2)
        self.C.dodaj_sasiad(self.E, 3)
        self.D.dodaj_sasiad(self.A, 2)
        self.D.dodaj_sasiad(self.C, 1)
        self.D.dodaj_sasiad(self.G, 1)
        self.E.dodaj_sasiad(self.C, 3)
        self.E.dodaj_sasiad(self.F, 2)
        self.F.dodaj_sasiad(self.B, 2)
        self.F.dodaj_sasiad(self.G, 1)
        self.F.dodaj_sasiad(self.E, 2)
        self.G.dodaj_sasiad(self.D, 1)
        self.G.dodaj_sasiad(self.F, 1)


class Dijkstra:


    def __init__(self):
        self.pierwsze_wykonanie = True
        self.pop = ['None','None','None','None','None','None','None']
        self.naszgraf = graf()
        self.odwiedz = []

    def szukaj(self, point):
        if self.pierwsze_wykonanie:
            self.odwiedz.append(self.naszgraf.A)
            self.naszgraf.A.odleglosc = 0
            self.pierwsze_wykonanie = False

        nowe_d = []
        nastepnicy =[]
        for sasiad in point.sasiedzi:
            if sasiad[0] in self.odwiedz:
                self.wpisz(point, sasiad)
            else:
                nowe_d.append(self.wpisz(point, sasiad))
                nastepnicy.append(sasiad[0])

        najblizszy = min(nowe_d)
        najblizszy = nowe_d.index(najblizszy)
        self.odwiedz.append(nastepnicy[najblizszy])
        return nastepnicy[najblizszy]


    def wpisz(self, poprz, nast):
        if nast[0].nazwa == 'A': numer = 0
        if nast[0].nazwa == 'B': numer = 1
        if nast[0].nazwa == 'C': numer = 2
        if nast[0].nazwa == 'D': numer = 3
        if nast[0].nazwa == 'E': numer = 4
        if nast[0].nazwa == 'F': numer = 5
        if nast[0].nazwa == 'G': numer = 6
        if poprz.nazwa == 'A': numer_poprz = 0
        if poprz.nazwa == 'B': numer_poprz = 1
        if poprz.nazwa == 'C': numer_poprz = 2
        if poprz.nazwa == 'D': numer_poprz = 3
        if poprz.nazwa == 'E': numer_poprz = 4
        if poprz.nazwa == 'F': numer_poprz = 5
        if poprz.nazwa == 'G': numer_poprz = 6
        for sasiad in nast[0].sasiedzi:
            d = sasiad[0].odleglosc + sasiad[1]
            if d < nast[0].odleglosc:
                nast[0].odleglosc = d
                self.pop[numer] = sasiad[0].nazwa
        return nast[0].odleglosc






    def run(self):
        punkt = self.naszgraf.A
        algorytm = True

        while (algorytm):
            punkt = self.szukaj(punkt)
            if punkt.nazwa == 'F':
                algorytm = False


        droga =['F']
        ind = 5
        petla = True
        while(petla):
            droga = [self.pop[ind]] + droga
            if self.pop[ind] == 'A': ind = 0
            elif self.pop[ind] == 'B': ind = 1
            elif self.pop[ind] == 'C': ind = 2
            elif self.pop[ind] == 'D': ind = 3
            elif self.pop[ind] == 'E': ind = 4
            elif self.pop[ind] == 'F': ind = 5
            elif self.pop[ind] == 'G': ind = 6
            if ind == 0:
                petla = False


        print('Najkrótsza droga z A do F wynosi ', self.naszgraf.F.odleglosc, '. Prowadzi następująco:')
        print(droga)





if __name__ == '__main__':
    algorytm = Dijkstra()
    algorytm.run()