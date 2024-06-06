# Trabalho Calculadora Digital em Python(PARADIGMAS DE LINGUAGENS DE PROGRAMAÇÃO EM PYTHON)

def soma(x, y):
    """mostra a soma de x e y"""
    return x + y

def subtrai(x, y):
    """mostra a diferença entre x e y"""
    return x - y

def multiplica(x, y):
    """mostra a multiplicação entre x e y"""
    return x * y

def divide(x, y):
    """mostra a divisão de x por y,"""
    if y == 0:
        raise ValueError("Não divide por zero!")
    return x / y

def main():
    while True:
        print("CALCULADORA")
        print("1. SOMAR")
        print("2. SUBTRAIR")
        print("3. MULTIPLICAR")
        print("4. DIVIDIR")
        print("5. SAIR")

        choice = input("Escolha uma opção: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if choice < 1 or choice > 5:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 5.")
            continue

        if choice == 5:
            print("Finalizando o programa!")
            break

        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            continue

        if choice == 1:
            result = soma(num1, num2)
        elif choice == 2:
            result = subtrai(num1, num2)
        elif choice == 3:
            result = multiplica(num1, num2)
        elif choice == 4:
            try:
                result = divide(num1, num2)
            except ValueError as e:
                print(e)
                continue

        print(f"Resultado final: {result:.2f}")

if __name__ == "__main__":
    main()