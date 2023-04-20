from sort import sort
from random import randint

test_array = []
test_array_two = []
array_len = randint(5, 20)

while len(test_array) != array_len:
    test_array.append(randint(0, 1000))
    test_array_two.append(randint(0, 1000))

ascending_result = sort(True, test_array)
descending_result = sort(False, test_array_two)

print(
    f"Here is a random array sorted in an ascending manner: {ascending_result}\n")
print(
    f"Here is a random array sorted in a descending manner: {descending_result}")
