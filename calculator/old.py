# The next step for optimization is using the sample space with maybe:
# faces if amount == 1
# faces**2 if amount == 2
# ??? if amount > 2
# ;-;=b
# if amount == 3: if faces is even: 2* (mid*(min+mid)/2); elif faces == 3: (faces+1)**2; elif faces==5: (faces+2)**2...
# I think...


def sums_counter(amount: int, faces: int):
    result_min = amount  # * 1 (minor face); The minimum scrollable result
    result_max = amount * faces  # The maximum scrollable result
    results = dict()  # The count will be allocated in a dictionary listing how many times each hit occurs
    even = amount % 2 != 0 and faces % 2 == 0  # No, no is wrong! This "even" meas if the length counts is even,
    # and it will be important in the line 18
    result_mid = (result_max + result_min) // 2  # Similar to the Pascal sequence, it is mirrored in its midst

    if amount == 1:  # In the case, we have a equiprobable sample space, so all the results occur once
        for result in range(result_min, result_max+1):
            results[result] = 1
    else:  # If you tab the possible results, you will see that a "pyramidal" pattern to the values with a arithmetic
        # ratio of the 1
        for result in range(result_min, result_max+1):
            if result == result_min:
                results[result] = 1
            elif result <= result_mid:
                results[result] = results[result - 1] + 1
            elif result == result_mid + 1 and even:
                results[result] = results[result - 1]
            else:
                results[result] = results[result-1] - 1
    return results


def sums_probabilities(amount: int, faces: int, percentage=False):
    # With the count values it is possible to calculate the probability by dividing by the sample space, which would
    # be the sum of this count.
    sums_counts = sums_counter(amount, faces)
    results = dict()
    counts = sums_counts.values()
    sample_space = sum(counts)
    for r, c in sums_counts.items():
        probability = c/sample_space
        if percentage:
            probability *= 100
        results[r] = probability
    return results


# Tester
dice_ex = input("<#DADOS>d<#FACES>: ")
n, f = map(int, dice_ex.split('d'))  # n: amount of dices, f: amount of faces
show_percent = input("Mostrar em porcentagem? [Sn]") in "Ss"
f_max = f
del f
for f in range(2, f_max + 1):  # 2: Coin; But it work with 1...
    print("="*30 + f" {n}d{f} " + "="*30)
    sums_n_counts = sums_counter(n, f)
    sums_n_probs = sums_probabilities(n, f, show_percent)
    probabilities = list(map(round, sums_n_probs.values(), [2 for x in sums_n_probs]))

    for soma in sums_n_counts.keys():
        print(str(soma).center(9), end= '| ')
    print()
    for count in sums_n_counts.values():
        print(str(count).center(9), end='| ')
    print("=" + str(sum(sums_n_counts.values())).center(9))
    for probability in probabilities:
        print((str(probability) + ("%" if show_percent else "")).center(9), end='| ')
    print()
print("="*65)
