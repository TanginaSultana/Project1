import time
# For loop
start_time = time.time()
numbers = [i for i in range(0,1000)]
result = []
for num in numbers:
    if num % 2 == 1:
        result.append(num ** 2)
end_time = time.time()
for_loop_time = end_time - start_time
# List comprehension
start_time = time.time()
result = [num ** 2 for num in numbers if num % 2 == 1]
end_time = time.time()
list_comp_time = end_time - start_time
print("For loop time:", for_loop_time)
print("List comprehension time:", list_comp_time)
print("Difference:", for_loop_time - list_comp_time)