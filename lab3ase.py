import numpy as np
import random as rdn
import datetime

def buble(dane):
    zmiana = True
    n = len(dane) - 1
    while(zmiana):
        if (dane[n] < dane[n - 1]):
            buff = dane[n]
            dane[n] = dane[n - 1]
            dane[n - 1] = buff
            n = len(dane) - 1
        else:
            n = n-1
        if(n == 0):
            zmiana = False
    return dane

def selection_sort(dane):
    n = len(dane)
    for i in range(0, n):
        ind = np.argmin(dane[i:n])
        ind = ind + i
        if(ind != i):
            buff = dane[i]
            dane[i] = dane[ind]
            dane[ind] = buff
    return dane


def quicksort(dane):
    # print(dane)
    out = []
    if(len(dane) == 1):
        gr_ind = 0
        pivot = dane[0]
        piv_ind = 0
    else:
        buff = 0
        gr_ind = 0
        piv_ind = len(dane) - 1
        pivot = dane[piv_ind]
        for i in range(0, piv_ind):
            if(dane[i] < pivot):
                buff = dane[i]
                dane[i] = dane[gr_ind]
                dane[gr_ind] = buff
                gr_ind = gr_ind+1
            # print(dane)
        buff = pivot
        dane[piv_ind] = dane[gr_ind]
        dane[gr_ind] = buff
    if (gr_ind != 0):
        left = quicksort(dane[0:gr_ind])
        for i in range(0, len(left)):
            out.append(left[i])
    out.append(pivot)
    if (gr_ind != piv_ind):
        right = quicksort(dane[(gr_ind + 1):(piv_ind) + 1])
        for i in range(0, len(right)):
            out.append(right[i])

    return out



if __name__ == '__main__':

    dane = np.random.randint(10000, size=1000)
    print('Dane przed posortowaniem:')
    print(dane[0:25])

    start_bbl = datetime.datetime.now()
    dane_bbl = buble(dane[0:len(dane)-1])
    time_bbl = datetime.datetime.now() - start_bbl
    print('Czas sortowania algorytmm bąbelkowym:')
    print(time_bbl.microseconds)
    print(dane_bbl[0:25])

    start_select = datetime.datetime.now()
    dane_select = selection_sort(dane[0:len(dane)-1])
    time_select = datetime.datetime.now() - start_select
    print('Czas sortowania algorytmem select sort:')
    print(time_select.microseconds)
    print(dane_select[0:25])

    start_quick = datetime.datetime.now()
    dane_quick = quicksort(dane)
    time_quick = datetime.datetime.now() - start_quick
    print('Czas sortowania algorytmem quick sort:')
    print(time_quick.microseconds)
    print(dane_quick[0:25])





