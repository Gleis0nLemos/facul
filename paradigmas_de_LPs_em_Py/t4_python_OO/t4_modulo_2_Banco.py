from t4_modulo_2_Conta2 import Conta
from t4_modulo_2_Cliente import Cliente
from typing import List

class Banco: 

    def __init__(self):
        self.clientes: List[Cliente] = []
        self.contas: List[Conta] = []

    def cadastrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)

    def criar_conta(self, clientes, numero, saldo):
        conta = Conta(clientes, numero, saldo)
        self.contas.append(conta)

        for cliente in clientes:
            cliente.contas.append(conta)

        return conta

    def pesquisar_cliente(self, cpf: int) -> Cliente:
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
            
        return None

    def pesquisar_conta(self, numero: int) -> Conta:
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        
        return None
    
    def listar_clientes(self):
        for cliente in self.clientes:   
            print(f"-------------- \nCliente: {cliente.nome} \nEndereço: {cliente.endereco}")

            for conta in cliente.contas:
                print(f"Conta: {conta.numero}")

    def listar_contas(self):
        for conta in self.contas:
            print("--------------")
            for cliente in conta.clientes:
                print(f"Cliente: {cliente.nome}")

            print(f"Número: {conta.numero} \nSaldo: {conta.saldo}")
            
    def extrato(self, numero_conta):
        conta = self.pesquisar_conta(numero_conta)
        if conta:
            conta.extrato.extrato(numero_conta)
        else:
            print("Conta não encontrada") 