"""
Achar todos os números palíndromos existentes entre 100 e 500. Um número é palíndromo se ele tiver o memso valor quando escrito da direita
para esquerda. Ex> 17371. Escreva e utilize uma subrotina cujo resultado é o valor recebido no parametro (número inteiro) escrito ao contrário.
"""
def is_palindrome(n):
    # Converte o número em uma string
    num_str = str(n)
    # Verifica se a string é igual à sua reversa
    return num_str == num_str[::-1]
# Loop de 100 a 500
for num in range(100, 501):
    if is_palindrome(num):
        print(num)