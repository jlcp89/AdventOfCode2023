
puzzleInput = [i.strip('\n') for i in open(r'd9_real.txt', 'r').readlines()]
puzzleInput = [list(map(int, i.split(' '))) for i in puzzleInput]

def extrapolate(input):
    last = []

    def returnDifference(lst):
        for i in range(len(lst)-1):
            lst[i] = lst[i+1] - lst[i]
        last.append(lst[len(lst)-1])
        lst.pop(len(lst)-1)
        return lst

    while set(input) != {0}:
        input = returnDifference(input.copy())  # Hacer una copia de la lista original

    return sum(last)

print('part 2:', sum([extrapolate(i[::-1]) for i in puzzleInput]))
