# g(faces, dices) = ((1/faces)*(x + x**2 + x**face)s)**dices
# f(x) = x**sum
# P(sum) = df/dx
# P(sum) = sum*x**(sum-1)
# E g é a função geradora de P(sum)


def funcao_probabilidade(dices, faces, sum):
    return dices+faces+sum
