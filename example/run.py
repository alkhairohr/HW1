# You can do all of this in the `__main__.py` file, but this file exists
# to shows how to do relative import functions from another python file in
# the same directory as this one.
import numpy as np
import sorting as so
import matplotlib.pyplot as plt

# from .sorting import quick_sort, bubble_sort, generate_random_arrays, sort_n_time

def run_stuff():
	"""
	This function is called in `__main__.py`
	"""
	print("This is `run()` from ", __file__)

	sorting_functions = {so.bubble_sort:[],so.quick_sort:[]}
	#sorting_functions = {bubble_sort:[]}

	so.COND = 0 
	so.ASSIGN = 0
	#Time complexity
	for n in range(100,1100,100): #for sizes 100,200,300....1000

		temp_list = [so.generate_random_arrays(n) for x in range(100)]
		for sort_func,value in sorting_functions.items():

			timed = so.sort_n_time(sort_func, temp_list)
			value.append(timed)


	y = [x for x in range(100,1100,100)]
	for k,v in sorting_functions.items():
		# print(k.__name__,v)
		print(k.__name__)
		#plot_complexity(y,v)
		plt.plot(y,v,label=k.__name__)

	plt.legend()
	plt.xlabel("Vector length")
	plt.ylabel("Time (s)")
	plt.show()

	#Assignment/Conditional
	sorting_functions = {so.bubble_sort:[],so.quick_sort:[]}

	for n in range(100,1100,100):
		temp_list = so.generate_random_arrays(n)
		for sort_func,value in sorting_functions.items():
			so.ASSIGN = 0
			so.COND = 0
			if sort_func.__name__ == "quick_sort":
				sort_func(temp_list,0,n-1)
			else:
				sort_func(temp_list)

			value.append((so.COND,so.ASSIGN))

	y = [x for x in range(100,1100,100)]
	fig, axs = plt.subplots(2)
	for k,v in sorting_functions.items():

		yaxis_1 = [val[0] for val in v]
		yaxis_2 = [val[1] for val in v]
		axs[0].plot(y,yaxis_1,label=k.__name__)
		axs[1].plot(y,yaxis_2,label=k.__name__)

	axs[0].set_title("Conditionals")
	axs[1].set_title("Assignments")

	plt.legend()
	plt.show()
