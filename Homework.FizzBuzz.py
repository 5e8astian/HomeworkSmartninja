#for i in range(1,101):
    #print("Fizz"*(i%3<1)+(i%5<1)*"Buzz" or i)
for i in range(1,101):
    if i%3==0:
        print('fizz')
    elif i%5==0:
        print('buzz')
    elif i%3==0 and i%5==0:
        print('FizzBuzz')
    else:
        print(i)
