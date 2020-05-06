def fibo_dinamico(n, memo={}):

    step = 0

    if n == 0:
        step += 1
        print(f'.........Caso base - Fibo({n}) = {0}')
        return0
    elif n == 1:
        step += 1
        print(f'.........Caso base - Fibo({n}) = {0}')
        return1
    try:
        print(f'..Consultando en dic_memo Fibo({n})')
        return memo[n]
    except KeyError:
        print(f'....No existe Fibo({n}) en el diccionario')
        print(f'......Calculando Fibo({n})')
        resultado = fibo_dinamico(n-1, memo) + fibo_dinamico(n-2, memo)
        memo[n] = resultado
        print(f'.........Se guardo Fibo({n})={resultado} en el diccionario')
        
    return resultado

if __name__ == '__main__':
    n = 5
    num_fibo_n = fibo_dinamico(n)
    print('*'*40)
    print(f'El numero Fibo({n}) = {num_fibo_n}')