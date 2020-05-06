objective = int(input('Enter a number: '))
epsilon = 0.001
step = epsilon**2 
answer = 0.0

while abs(answer**2 - objective) >= epsilon and answer <= objective:
    #print(abs(answer**2 - objective), answer)
    answer += step

if abs(answer**2 - objective) >= epsilon:
    print(f'The square root of {objective} was not found')
else:
    print(f'The closer number to the square root of {objective} is {answer}')