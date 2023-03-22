print('Vamos calcular seu IMC? :P')
nome = input('Digite seu nome: ')

peso = int(input('Diga seu peso(kg): ')) 
altura = float(input('Agora, diga sua altura(m): '))

imc = peso / altura**2

print(f'{nome}, seu IMC é = {imc:,.2f}')

if imc <= 18.5:
    print('Você está abaixo do peso!')

elif imc > 18.5 and imc <= 24.9:
    print('Você tem um peso normal!')

elif imc >= 25 and imc <= 29.9:
    print('Você está com excesso de peso.')

elif imc == 30:
    print('Cuidado! Você está no começo de uma obesidade!')

elif imc > 30 and imc <= 34.9:
    print('Você está com obesidade classe 1.')

elif imc >= 35 and imc <= 39.9:
    print('Você está com obesidade classe 2.')

else:
    print('Nível de obesidade classe 3.')


# Baixo peso – IMC <18,5
# Peso normal – IMC ≥18,5 a 24,9
# Excesso de peso – IMC ≥25 a 29,9
# Obesidade – IMC ≥30
# Obesidade classe 1 – IMC 30 a 34,9
# Obesidade classe 2 – IMC de 35 a 39,9
# Obesidade classe 3 – IMC ≥40


# RESPOSTA DADA NA ATIVIDADE, MAIS SIMPLES 
# peso = eval(input('Entre com seu peso: '))
# altura = eval(input('Entre com altura: '))
# imc = peso/(altura2)
# print('imc = ', imc)


