#Creating second list WITHOUT using List comprehension
import numpy as np
import timeit
start_time = timeit.default_timer()
# code you want to evaluate
elapsed = timeit.default_timer() - start_time

start_time = timeit.default_timer()
#first_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
first_list = np.arange(1000)
second_list = [] 
for item in first_list: 
    if item % 2 == 0: 
        second_list.append(item) 
  
#print(second_list) 
elapsed_for = timeit.default_timer() - start_time
print(elapsed_for)

start_time = timeit.default_timer()
#first_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
first_list = np.arange(1000) 
second_list = [item for item in first_list if item % 2 == 0] 
  
#print(second_list)
elapsed_comp = timeit.default_timer() - start_time

print(elapsed_comp)