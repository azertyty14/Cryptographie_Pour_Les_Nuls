import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b//a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m

def bebe_geant(y : int, g : int, n : int):
    """
    y la valeur dont on veut trouver le log discret
    g un générateur du groupe
    n l'ordre du groupe
    """
    m = int(math.sqrt(n))
    print("calcul du dictionnaire")
    d = dict()
    for i in range(m):
        v = pow(g, i, n)
        d[v] = i
    print(d)
    g_m_inv = modinv(pow(g,m,n), n)
    print("g^-" + str(m) +"=" + str(g_m_inv))
    x = y
    j = 0
    print("debut de boucle")
    while x not in d:
        print("j=", j," x=", x)
        x = (x*g_m_inv) % n
        j += 1
    print("fini : j=", j," x=", x)
    print("log discret de " + str(y) + " en base " + str(g) + " modulo " + str(n) + " est : " + str(j*m + d[x]))    


if __name__ == "__main__":
    bebe_geant(23, 7, 101)