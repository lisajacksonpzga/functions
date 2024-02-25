import random

def pluck_random(n, num_list):
    if n >= len(num_list):
        return num_list.copy()
    else:
        random_elements = random.sample(num_list, n)
        for element in random_elements:
            num_list.remove(element)
        return random_elements



num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3

print(num_list)
pluck_elements = pluck_random(n, num_list)
print(pluck_elements, num_list)
