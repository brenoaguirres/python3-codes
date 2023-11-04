# if you return a nested function from a function, that nested function
#   has access to the variables defined in that function, even if the
#   function is not active anymore.

# fechamento ou clausura (closures)
# funções que foram definidas dentro do escopo de outra função e por isso possuem acesso ao
#   contexto, variaveis da função mãe.


def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment


increment = counter()

print(increment())
print(increment())
print(increment())

