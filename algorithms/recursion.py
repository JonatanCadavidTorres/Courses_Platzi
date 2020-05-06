

def recursion(target):
    if target == 1:
        return 1
    elif target == 0:
        return 'the number can not be 0'
    elif type(target) == float:
        return 'the number can not be float'
    
    return target * (recursion(target - 1))

print(recursion(int(input('Please insert a integer number: '))))




