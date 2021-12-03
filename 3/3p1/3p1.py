with open("../input.txt", "r") as f_input:
    threshold = (sum(1 for _ in f_input) / 2) + 1
    n_bits = 12
    zero = 0
    one = 0
    gamma = 0b0
    mask = 0b111111111111

    print(f"nbits: {n_bits}")

    for b in range(0, n_bits):
        zero = 0
        one = 0
        f_input.seek(0)
        for line in f_input:
            if line[b] == '0': zero += 1
            else: one += 1

            if zero >= threshold:
                print(f"zeros: {zero}")
                break

            if one >= threshold:
                print(f"ones: {one}")
                gamma |= (1 << (n_bits - 1 - b))
                break

    print(f"gamma: {bin(gamma)}")
    print(f"epsilon: {bin(gamma ^ mask)}")
    print(f"Prod: {gamma * (gamma ^ mask)}")