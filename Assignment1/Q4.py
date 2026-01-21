def remove_even_inplace(numbers):
    for n in numbers[:]: 
        if n % 2 == 0:
            numbers.remove()
    return numbers
    nums = (1,2,3,4,5,6,7,8,9,10)
    Print( remove_even(nums))

Output:- nums(1,2,3,4,5,6,7,8,9,10)