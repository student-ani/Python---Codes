# def calculate_average(numbers):
#     return sum(numbers) / len(numbers)

# my_list = [1, 2, 3, 4, 5]
# average = calculate_average(my_list)
# print(average)

import statistics
def calculate_std_dev(numbers):
    return statistics.stdev(numbers)

my_list = [1, 2, 3, 4, 5]
std_dev = calculate_std_dev(my_list)
print(std_dev)