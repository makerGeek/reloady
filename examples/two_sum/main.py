# read input from file
from two_sum import two_sum


with open('input.txt', 'r') as input_file, open('output.txt', 'r') as expected_output_file:
    
    n_cases = int(input_file.readline().strip())
    for _ in range(n_cases):
        nums = list(map(int, input_file.readline().split()))
        target = int(input_file.readline().strip())

        # get result
        result = two_sum(nums, target)
        formatted_result = ' '.join(map(str, result))

        # compare result with expected output
        expected_output = expected_output_file.readline().strip()
        assert formatted_result == expected_output, f"Expected {expected_output}, but got {result}"

    print("All tests passed!")
