from reader import dice_reader, sum_reader
from calculator import probability

n, f, m = dice_reader()
s = sum_reader()
print(f"The probability of the sum {s} occurring in rolling of {n}d{f}{'+' if m > 0 else ''}{m if m != 0 else ''} is "
      f"around {round(probability(n, f, s, m)*100, 2)}%")
