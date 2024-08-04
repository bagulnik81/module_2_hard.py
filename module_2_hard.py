def generate_password(n):
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))
    result = ""
    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:
            result += f"{pair[0]}{pair[1]}"
    return result


for n in range(3, 21):
    password = generate_password(n)
    print(f"{n} - {password}")
