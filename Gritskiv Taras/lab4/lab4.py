def factorial(number):
    my_score=1
    start_point=1
    for i in range(number):
        my_score*=start_point
        start_point+=1
    return my_score
print(factorial(7))