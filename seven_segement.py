segement = [[" z"] * 5, [" z"] * 5] * 2
print(segement)
for row in segement:
    for item in row:
        print(item, end=" ")
    print()


def set_a():
    for i in range(0, 1):
        for j in range(0, 5):
            segement[i][j] = "* "
        print()
    return segement


print(set_a())
