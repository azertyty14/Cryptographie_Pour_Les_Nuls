import sympy


def get_ciphered(n: int, e: int, m: int) -> int:
    c = pow(m, e, n)
    return (c)


def get_q_and_phi_from_p(n: int, p: int) -> (int, int):
    q = n/p
    if q != int(q):
        print("Error, n/p is not an int !!")
    else:
        q = int(q)
        phi_n = (p-1)*(q-1)
    return (int(q), phi_n)


def get_d_from_phi_n(e: int, phi_n: int) -> int:
    d = sympy.mod_inverse(e, phi_n)
    return d


def get_clear_from_ciphered(n: int, c: int, d: int) -> int:
    m = pow(c, d, n)
    return m


if __name__ == "__main__":
    n = 4331
    e = 59
    m1 = 3158
    p = 61
    c2 = 167

    print("\nBase parameters:")
    print("n={n}".format(n=n))
    print("e={e}".format(e=e))
    print("m1={m1}".format(m1=m1))
    print("p={p}".format(p=p))
    print("c2={c2}".format(c2=c2))

    print("\nQuestion 1:")
    c1 = get_ciphered(n, e, m1)
    print("m1={m1}".format(m1=m1))
    print("c1={c1}".format(c1=c1))

    print("\nQuestion 2:")
    (q, phi_n) = get_q_and_phi_from_p(n, p)
    print("n=p*q={n}".format(n=n))
    print("p={p}".format(p=p))
    print("q={q}".format(q=q))
    print("phi(n)=(p-1)*(q-1)={phi_n}".format(phi_n=phi_n))

    print("\nQuestion 3:")
    d = get_d_from_phi_n(e, phi_n)
    print("d={d}".format(d=d))

    print("\nQuestion 4:")
    m2 = get_clear_from_ciphered(n, c2, d)
    print("c2={c2}".format(c2=c2))
    print("m2={m2}".format(m2=m2))
