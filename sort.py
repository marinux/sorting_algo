def sort(ascending: bool, array: list) -> list:
    curr_smallest = array[0]
    curr_smallest_idx = 0
    left_to_check = array
    output = []

    while len(left_to_check) >= 1:
        if len(left_to_check) == 1:
            output.append(left_to_check[0])
            break

        for i, j in enumerate(left_to_check):
            if not curr_smallest:
                curr_smallest, curr_smallest_idx = left_to_check[i], i
            elif j < curr_smallest:
                curr_smallest, curr_smallest_idx = j, i
            elif i == len(left_to_check) - 1:
                output.append(curr_smallest)
                del left_to_check[curr_smallest_idx]
                curr_smallest = curr_smallest_idx = None

    if not ascending:
        output.reverse()

    return output
