objective = int(input('Please enter a integer number: '))
answer = 0

while answer**2 < objective:
    print(answer)
    answer += 1

if answer**2 == objective:
    print(f'The square root of {objective} is {answer}')
else:
    print(f'{objective} does not have an exactly square root ')