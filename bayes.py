import csv
import matplotlib.pyplot as plt



def stworz_tablice(string, tablicax, tablicay):
    
    tablica = []
    dane = csv.reader(open(string, 'r'), delimiter='|')
    for row in dane:
        tablica.append([float(x) for x in row])
    for element in tablica:
        tablicax.append(element[0])
        tablicay.append(element[1])

def wykres(x, y, x1, y1, x2, y2, t):
    plt.scatter(x1, y1,)
    plt.scatter(x2, y2,)
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel("Y")
    if t:
        plt.title("Punkt przydzielono do niebieskich")
    else:
        plt.title("Punkt przydzielono do pomaranczowych")
    plt.show()
def sasiedztwo(r, x, y, x1, x2, y1, y2):
    liczba1 = 0
    liczba2 = 0
    liczba_cal = 0
    for i in range(0, len(x1)):
        if ((x - x1[i])**2 + (y - y1[i])**2 <= r):
            liczba1 = liczba1+1
            liczba_cal = liczba_cal + 1
    for i in range(0, len(x2)):
        if ((x - x2[i])**2 + (y - y2[i])**2 <= r):
            liczba2 = liczba2+1
            liczba_cal = liczba_cal + 1
    return liczba1, liczba2, liczba_cal
def bayes(x, y, x1, y1, x2, y2):
    apriori1 = len(x1)/(len(x1) +len(x2))
    apriori2 = len(x2)/(len(x2) + len(x1))
    sasiad1 = 0
    sasiad2 = 0
    sasiad = 0
    r = 0.5
    while sasiad < 2:
        sasiad1, sasiad2, sasiad = sasiedztwo(r, x, y, x1, x2, y1, y2)
        r = r + 0.5
    szansa1 = sasiad1/len(x1)
    szansa2 = sasiad2/len(x2)
    aposteriori1 = apriori1*szansa1
    aposteriori2 = apriori2*szansa2
    if aposteriori1 > aposteriori2:
        przynaleznosc = True
    else:
        przynaleznosc = False
    return przynaleznosc




if __name__ == '__main__':
    x1 = []
    x2 = []
    y1 = []
    y2 = []
    x = 4
    y = 1
    stworz_tablice('data3.csv', x1,y1)
    stworz_tablice('data4.csv', x2, y2)
    czy_1 = bayes(x, y, x1, y1, x2, y2)
    wykres(x, y, x1, y1, x2, y2, czy_1)


