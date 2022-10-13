def invertir_digitos_2(numero):
    num_str = str(numero)
    len_num = len(num_str)
    i=1
    num_inv = 0
    while i<=len_num:
        resto = numero%10
        num_inv = num_inv + (resto*10**(len_num-i))
        numero = numero // 10
        i=i+1
    print(num_inv)

def invertir_digitos(numero):
    num_str = str(numero)
    num_inv = num_str[::-1]
    print(num_inv)