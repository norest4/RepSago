def fizbuzz(range_up_to):
    # function here
    # range_up_to - str
    for cnt in range(1, range_up_to+1):
        if cnt%3 == 0 and cnt%5 == 0: print('FizzFuzz')
        elif (cnt%3) == 0: print('Fizz')
        elif cnt%5 == 0: print('Fuzz')
        else: print(cnt)

first_example = 50
second_example = 150
third_example = 1473
fizbuzz(first_example)
fizbuzz(second_example)
fizbuzz(third_example)