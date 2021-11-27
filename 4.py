string = input("Insert words in spaces: ").split()
for i, word in enumerate(string, 1):
    print(f'{i}, {word[:10]}')
    