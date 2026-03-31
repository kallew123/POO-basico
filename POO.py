class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor

    def mostrar_saldo(self):
        print(f"Saldo atual: {self.saldo}")

titular = input("Titular: ")
saldo = float(input("Saldo: "))

print("")

conta1 = ContaBancaria(titular, saldo)

while True:
    escolha = int(input("O que deseja fazer?(1 - Depositar, 2 - Sacar, 3 - Mostar Saldo, 4 - Sair) "))
    print("")
    try:
        if escolha == 1:
            depositar = float(input("Valor do deposito: "))
            conta1.depositar(depositar)
            print("Deposito realizado!")
            print("")
        elif escolha == 2:
            sacar = float(input("Valor do saque: "))
            conta1.sacar(sacar)
            print("Saque realizado!")
            print("")
        elif escolha == 3:
            conta1.mostrar_saldo()
            print("")
        elif escolha == 4:
            print("Ate mais!")
            break
        else:
            print("Escolha invaida!")
            print("")
    except ValueError:
        print("Invalido!")
        
