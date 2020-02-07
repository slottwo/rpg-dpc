from reader import dice_reader, sum_reader
from calculator import probability


def one_sum_probability():
    n, f, m = dice_reader()
    s = sum_reader()
    print(f"The probability of the sum {s} occurring in rolling of {n}d{f}{'+' if m > 0 else ''}{m if m != 0 else ''} "
          f"is around {round(probability(n, f, s, m)*100, 2)}%")


'''
def all_sums_probabilities():
'''
