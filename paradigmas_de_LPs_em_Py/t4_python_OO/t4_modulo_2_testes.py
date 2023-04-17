from t4_modulo_2_Conta2 import Conta
from t4_modulo_2_Cliente import Cliente
from t4_modulo_2_Banco import Banco

#criação dos clientes
cliente1 = Cliente(123, "João", "Rua 1")
cliente2 = Cliente(345, "Maria", "Rua 2")
cliente3 = Cliente(567, "Zé", "Rua 3")
cliente4 = Cliente(879, "Lucas", "Rua 4")

#criação dop banco
banco = Banco()

#criação das contas
# conta1 = Conta([cliente1, cliente2], 1, 2000)
# conta2 = Conta([cliente3, cliente4], 2, 5000)

#cadastrando clientes/contas no banco
banco.cadastrar_cliente(cliente1)
banco.cadastrar_cliente(cliente2)
banco.cadastrar_cliente(cliente3)
banco.cadastrar_cliente(cliente4)

# banco.adicionar_conta(conta1)
# banco.adicionar_conta(conta2)

#criação das contas
banco.criar_conta([cliente1, cliente2], 1, 2000)
banco.criar_conta([cliente3, cliente4], 2, 5000)

#listar todos os clientes e contas no banco
#banco.listar_clientes()
banco.listar_contas()

#mostrar extrato de cada conta
banco.extrato(1)
banco.extrato(2)