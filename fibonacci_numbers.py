# Fibonacci numbers
def get_fibonacci_numbers(num):

    # Fibonacci list
    fibonacci_list = [0, 1]

    i = 0
    while True:
        new_number = fibonacci_list[i] + fibonacci_list[i + 1]
        fibonacci_list.append(new_number)
        i += 1

        if i > 11:
            print(fibonacci_list)
            break



#  Run the program
get_fibonacci_numbers(0)
