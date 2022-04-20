from django.shortcuts import render
# # Create your views here.
# import requests
# import time
# import pprint
# def h(request):
#     url='https://vgo123.herokuapp.com'
#     response = requests.post(url)
#     o=response.json()
#     l=[]
#     for i in o:
#         l.append(i)
#         # time.sleep(20)
#         print(i),"#################")
#     # print(dir(response))
#     # pp = pprint.PrettyPrinter(indent=4)
#     # pp.pprint(o)
#     return render(request ,'index.html' , {'r':list(l)})
# Python program to illustrate the concept
# of threading
# importing the threading module

# import threading

# def print_cube(num):
# 	"""
# 	function to print cube of given num
# 	"""
# 	print("Cube: {}".format(num * num * num))

# def print_square(num):
# 	"""
# 	function to print square of given num
# 	"""
# 	print("Square: {}".format(num * num))

# # if __name__ == "__main__":
# 	# creating thread
# 	t1 = threading.Thread(target=print_square, args=(10,))
# 	t2 = threading.Thread(target=print_cube, args=(10,))

# 	# starting thread 1
# 	t1.start()
# 	# starting thread 2
# 	t2.start()

# 	# wait until thread 1 is completely executed
# 	t1.join()
# 	# wait until thread 2 is completely executed
# 	t2.join()

# 	# both threads completely executed
# 	print("Done!")
