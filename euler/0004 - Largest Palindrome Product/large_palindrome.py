def reverse_number(number):
    # Convert the number to a string
    number_str = str(number)
    
    # Reverse the string
    reversed_str = number_str[::-1]
    
    # Convert the reversed string back to an integer
    reversed_number = int(reversed_str)
    
    return reversed_number

def find_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

palindromic_products = []

for valuea in range(99, 1000):
    for valueb in range(99, 1000):
        product = valuea * valueb
        if find_palindrome(product):
            palindromic_products.append((valuea, valueb, product))

# Sort the list by product
palindromic_products.sort(key=lambda x: x[2])

# Print sorted list
for factors in palindromic_products:
    print(f"{factors[0]} x {factors[1]} = {factors[2]}")

# Print the largest palindromic product
largest_palindrome = palindromic_products[-1]
print(f"The largest palindromic product of two three-digit numbers is {largest_palindrome[2]}, which is the product of {largest_palindrome[0]} and {largest_palindrome[1]}.")