# number 1

def max_num(num1, num2, num3):
    max_of_first_two = max(num1, num2)
    maximum = max(max_of_first_two, num3)
    return maximum
num1 = 10
num2 = 25
num3 = 15
result = max_num(num1, num2, num3)
print("The maximum number is:", result)

# number 2

def mult_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = mult_list(my_list)
print("The result of multiplying is:", result)

#number 3

def rev_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

original_string = "r-a-c-e-c-a-r "
reversed_str = rev_string(original_string)
print("Original:", original_string)
print("Reversed:", reversed_str)

#number 4

def num_within(number, start_range, end_range):
    if start_range <= number <= end_range:
        return True
    else:
        return False
result1 = num_within(6, 2, 6)
print(result1)  
result2 = num_within(36, 16, 34)
print(result2)  

# number 5

def pascal(n):
    triangle = []
    for i in range(n):
        current_row = [1]
        if i > 0:
            previous_row = triangle[i - 1]
            for j in range(1, i):
                current_element = previous_row[j - 1] + previous_row[j]
                current_row.append(current_element)
        if i > 0:
            current_row.append(1)
        triangle.append(current_row)
    for row in triangle:
        print(" ".join(map(str, row)).center(n * 2 - 1))
n = 5
pascal(n)


