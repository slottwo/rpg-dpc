# n: amount of dices
# f: amount of faces
# s: sum witch it wants to check


def len_sums(n: int, f: int):
    # init: n, last: n*f
    length = n*f - n + 1  # How many sums is in range (n to n*f)
    return length


def simple_space(n: int, f: int):
    omega: int  # Simple Space
    # init: n, last: n*f
    if n == 1:
        omega = f
    else:
        length = len_sums(n, f)  # Number of sums that occur
        mid = (length+1)//2  # Round UP length/2; mid: Number of occurrences of events (sums)
        even = length % 2 == 0  # Equivalent to (n % 2 != 0 and f % 2 != 0)
        omega = n**2 * (mid+1)  # Equivalent to 2*S(init, init+1 ... last-1, last) = 2 * (init*(init+last)/2)
        if not even:  # If even, it would be [1, 2, 2, 1]. Else it would be [1, 2, 3, 2, 1], but it would have a 3
            # more: [1, 2, 3, 3, 2, 1]
            omega -= mid  # Then remove the "3"
    return omega


def counter(n: int, f: int, s: int):
    if n == 1:
        return 1
    even = n % 2 != 0 and f % 2 == 0  # If the amount of sums possibles is even or not
    if not n <= s <= n*f:
        return 0
    # mid_sum: Sum value that occurs most often
    mid_sum = n*(f+1)//2  # (init + last)/2 = (n + n*f)/2
    if s < mid_sum:
        return s - n + 1
    elif s == mid_sum or s == mid_sum+1 and even:
        return (len_sums(n, f)+1)//2  # Round UP len/2...
    else:
        return n*f - s + 1


def probability(n: int, f: int, s: int, modifier=0):
    s -= modifier  # For 2d4 with modifier=3, for example, the probability of s=5 is the same to s=3 without modifier
    event = counter(n, f, s)
    omega = simple_space(n, f)
    P = event/omega
    return P


def probability_range(n: int, f: int, s_init: int = 1, s_end: int = -1, modifier= 0):
    probabilities = 0
    if s_end == -1:
        s_end = f*n
    for s in range(s_init, s_end + 1):
        probabilities += probability(n, f, s, modifier)
