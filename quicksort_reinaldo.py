from random import randint

def rand_partition(arr, left, right):
	rand_pivot = randint(left,right)
	arr[left], arr[rand_pivot] = arr[rand_pivot], arr[left] 

	return partition(arr, left, right)

def partition (arr, left, right):
	pivot_index = right
	i = left - 1
	for j in range(left, right):
		if arr[j] <= arr[pivot_index]:
			i+=1
			arr[j], arr[i] = arr[i], arr[j]
	arr[pivot_index], arr[i + 1] = arr[i + 1], arr[pivot_index]
	pivot_index = i + 1
	return pivot_index

	
	
	
def quicksort_rei (arr, left=0, right=None,debug=False):
	if right == None:
		right = len(arr) - 1 
	if left < right:
		if debug:
			print(arr[left:right])
		part_index = rand_partition(arr, left, right)
		quicksort_rei(arr, left, part_index - 1)
		quicksort_rei(arr, part_index + 1, right)


if __name__ == "__main__":
	n = input("Insert range of random array\n")
	try:
		n = int(n)
	except:
		raise("Error type an non negative instance of int")
	arr = []
	for _ in range(n):
		arr.append(randint(-20,20))
	print(arr)
	quicksort_rei(arr)
	print(arr)
