def calculadora(operacao):
    def soma(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def multi(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    def operacao_invalida(a, b):
        return "Operação inválida"
    
    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return multi
        case "/":
            return div
        case _:
            return operacao_invalida

# Exemplo de uso correto
print(calculadora("+")(2, 2))  # Resultado esperado: 4
print(calculadora("-")(2, 2))  # Resultado esperado: 0
print(calculadora("*")(2, 2))  # Resultado esperado: 4
print(calculadora("/")(2, 2))  # Resultado esperado: 1
print(calculadora("%")(2, 2))  # Resultado esperado: "Operação inválida"
