'''Proszę napisać funkcję bool possible( char* u, char* v, char* w ), która zwraca prawdę
jeśli z liter słów u i v da się ułożyć słowo w (nie jest konieczne wykorzystanie wszystkich liter)
oraz fałsz w przeciwnym wypadku. Można założyć, że w i v składają się wyłącznie z małych liter
alfabetu łacińskiego. Proszę krótko uzasadnić wybór zaimplementowanego algorytmu'''

def slowo(u,v,w):
    litery = [0]*26
    for i in range(len(u)):
        litery[ord(u[i])-97] += 1
    for i in range(len(v)):
        litery[ord(v[i])-97] += 1
    for i in range(len(w)):
        litery[ord(w[i])-97] -= 1
        if litery[ord(w[i])-97] < 0:
            return False
    return True
print(slowo('ala','basia','aaaaa'))