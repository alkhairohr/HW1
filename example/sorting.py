import matplotlib.pyplot as plt
import time 
import random



def bubble_sort(array):
	global COND
	global ASSIGN

	flag = True

	while flag:
		flag = False
		for index in range(len(array)-1):
			COND += 1
			if array[index] > array[index+1]:
				ASSIGN += 2
				array[index],array[index+1] = array[index+1],array[index]

				flag = True

	return array

def insertion_sort(array):
	global COND
	global ASSIGN

	i = 1
	while i < len(array):
		j = i
		while j > 0 and array[j-1] > array[j]:
			array[j],array[j-1] = array[j-1],array[j]
			j = j -1
		i = i + 1
	return array


def quick_sort(array,low,high):
	global COND
	global ASSIGN 

	COND += 1
	if low < high:
		p = partition(array,low,high)
		quick_sort(array,low,p - 1)
		quick_sort(array,p+1,high)

	return array

def partition(array,low,high):
	global COND
	global ASSIGN
	pivot = array[high]

	i = low
	for j in range(low,high):
		COND += 1
		if array[j] < pivot:
			ASSIGN += 2
			array[i],array[j] = array[j],array[i]
			i += 1
	ASSIGN += 2
	array[i],array[high] = array[high],array[i]

	return i

def generate_random_arrays(n):
	"""
		Generates a list of length n with random integers between 1 and 1000 using 
		the sample function in the random module
	"""

	l = [random.randrange(1, 1000) for _ in range(0, n)]

	return l

def sort_n_time(func, temp_list):
	"""
	Given a sorting function, func, and a nested list containing lists of integers, 
	sort each list and time. Return an average soring time 
	"""
	times = []
	count = 0 
	for element in temp_list:
		
		if func.__name__ == "quick_sort":
			start = time.time()
			func(element,0,len(element)-1)
			end = time.time()
		else:
			start = time.time()
			func(element)
			end = time.time()
			count += 1			
		
		times.append(end-start)
	# print(count,end-start)
	return sum(times)/len(times)

def sort_n_count(func, temp_list):
	"""
	Given a sorting function, func, and a nested list containing lists of integers, 
	sort each list and time. Return an average soring time 
	"""
	global COND
	global ASSIGN

	times = []
	count = 0 
	for element in temp_list:
		
		if func.__name__ == "quick_sort":
			start = time.time()
			func(element,0,len(element)-1)
			end = time.time()
		else:
			start = time.time()
			func(element)
			end = time.time()
			count += 1			
		
		times.append(end-start)
	# print(count,end-start)
	return sum(times)/len(times)





if __name__ == "__main__":

	print("IN MAIN")


