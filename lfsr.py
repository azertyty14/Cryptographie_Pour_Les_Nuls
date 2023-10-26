def affiche_polynome_generateur(polynome_generateur):
    n = len(polynome_generateur)
    output_poly = []
    for i in range(n):
        if polynome_generateur[i] == 1:
            output_poly.append('x^{i}'.format(i=i))
    print(" + ".join(output_poly) + " + x^{n}".format(n=n))


def calc_retroaction_bit(state, polynome_generateur):
    n = len(polynome_generateur)
    bit = 0
    for i in range(n):
        bit += state[i]*polynome_generateur[i]
    return bit % 2


def calc_next_state(state, polynome_generateur):
    n = len(polynome_generateur)

    retroaction_bit = calc_retroaction_bit(state, polynome_generateur)
    next_state = [0]*n
    next_state[:n-1] = state[1:n]
    next_state[n-1] = retroaction_bit
    return next_state


if __name__ == "__main__":
    # TO CHANGE WITH EXERCISE
    polynome_generateur = [1, 1, 0, 0]
    initial_state = [1, 0, 0, 1]

    t = 0
    n = len(polynome_generateur)

    print("Polynôme générateur:")
    affiche_polynome_generateur(polynome_generateur)

    print("\nÉtats internes:")
    print("t = {t} : {initial_state}".format(t=t, initial_state=initial_state))

    curr_state = calc_next_state(initial_state, polynome_generateur)
    t += 1
    while curr_state != initial_state:
        print("t = {t} : {curr_state}".format(t=t, curr_state=curr_state))
        curr_state = calc_next_state(curr_state, polynome_generateur)
        t += 1

    print("t = {t} : {curr_state}".format(t=t, curr_state=curr_state))
    print("\nPeriode trouvée : T = {t}".format(t=t))

    print(
        "\nPeriode max : t_max = 2^{n} -1 = {t_max}".format(n=n, t_max=2**n - 1))
