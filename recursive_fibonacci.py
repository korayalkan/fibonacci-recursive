# Find fibonacci numbers with recursive function
def find_fibonacci(i):

    # Return 1
    if i <= 1:
        return i

    # Return the fibonacci numbers
    else:
        return find_fibonacci(i-1) + find_fibonacci(i-2)



# Print range() amount of fibonacci numbers to console
for i in range(10):
    print(find_fibonacci(i))
