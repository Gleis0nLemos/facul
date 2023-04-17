class Conta:

    #__init__() funciona como inicializador de classes
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):

        if self.saldo < valor:
            return False
        
        else: 
            self.saldo -= valor

    def gerar_extrato(self):
        print(f"Número: {self.numero} \nCPF: {self.cpf} \nSaldo: {self.saldo}")

    def trasfere_valor(self, contaDestino, valor):

        if self.saldo < valor: 
            print("Saldo insuficiente.")
        
        else: 
            contaDestino.depositar(valor)
            self.saldo -= valor
        
        return ("Transferência realizada.")

# def main():
#     c1 = Conta(1, 1, "João", 0) #Objeto sendo instanciado
#     c1.depositar(300)
#     saque = c1.sacar(400)
#     c1.gerar_extrato()
#     print(f"O saque foi realizado? {saque}")
# # Quando um script Python é executado a variável reservada 
# # NAME referente a ele tem valor igual a "__main__"
# # Nesse caso, a condição do IF a seguir será TRUE
# # Então o que está no corpo do IF será executado. No caso,
# # É um chamado ao método, main do script 
# if __name__ == "__main__":
#     main()