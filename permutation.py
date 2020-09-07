def getPermutations(array):
	permutations = []
	permutationsHelper(array, [], permutations)
	return permutations

def permutationsHelper(array, currentPermutation, permutations):
	if not len(array) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i + 1 :]
			newPermutation = currentPermutation + [array[i]]
			permutationsHelper(newArray, newPermutation, permutations)

#solution 2


def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i + 1, array, permutations)
            swap(array, i, j)


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]