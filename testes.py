j=0
i=0
eixo_a = []
eixo_b = []
while j < 6:
    eixo_a.append(j)
    eixo_b.append(i)
    j = j + 1
    i = i + 2

matriz = [eixo_a , eixo_b]
print(matriz)

def bhaskara (a , b , c):
    delta = b**2 - 4 * a * c
    x1 = (- b + delta**(1/2)) / ( 2 * a )
    x2 = (- b - delta**(1/2)) / ( 2 * a )
    print ('raiz 1 é: ', x1 , 'raiz 2 é : ', x2)
# return manda a variavel para fora da funçao
bhaskara (1, -5, 6)

"""funcoes lambda
so usa uma vez
estrutura  
lambda variavel : variavel**2 ( nome da variavel que vai ser interagida e o retorno depois dos : )
"""

#map vamo la :::::    map(função , lista)
seq = [1, 2, 3, 4,5,6]
def quadrado (var): return var ** 2

print(list(map (quadrado , seq )))

print(list(map(lambda x : x**3 , seq)))


#filter retorna os valores true

print (list(filter(lambda teste : teste%2 != 0 , seq)))

list = [1,2,3,4,5,8,7,6]
list.sort()
x = 6
list.append(3)
print(x in list)
print(list)



