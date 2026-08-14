def naive_matching(pattern, text):
    positions = []

    for i in range(len(text) - len(pattern) + 1):
        match = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            positions.append(i)

    return positions


text = "AACCGAACCG"
pattern = "ACCG"

print("Text:", text)
print("Pattern:", pattern)
print("Matches:", naive_matching(pattern, text))