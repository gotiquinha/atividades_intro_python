# 1 Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def mostrar_mensagem():
    print("Hello World")


# 2 Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
def pergunta_numero():
    pergunta = int(input("Escolha um número: "))
    print("O número informado foi", pergunta)


# 3 Faça um Programa que peça dois números e imprima a soma
def pede_numero():
    num1 = int(input("Escolha o primero número: "))
    num2 = int(input("Escolha o segundo número: "))
    print("A soma dos números que você escolheu é:", num1 + num2)


# 4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.
def nota_escolar():
    print("Digite suas 4 notas bimestrais para sabermos sua média!")
    nota1 = int(input("Qual a sua nota de Português? "))
    nota2 = int(input("Qual a sua nota de Matemática? "))
    nota3 = int(input("Qual a sua nota de Ciências? "))
    nota4 = int(input("Qual a sua nota de Geografia? "))
    media = nota1 + nota2 + nota3 + nota4 / 4
    print("Sua média final é:", media)


# 5 Faça um Programa que converta metros para centímetros.
# para fazer isso, é só multiplicarmos o metro por 100 (centimetros)
def conversor_centimetros():
    metros = float(input("Quantos metros você tem? "))
    metros_centimetros = metros * 100
    print("Convertendo sua altura em cm, você tem ", metros_centimetros)


# 6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# a formula é A = pi * r² , area = pi que é 3.14 * raio elevado ao quadrado
def raio_circulo():
    raio = float(input("Qual é o raio do seu circulo? "))
    a = 3.14 * (raio ** 2)
    print("A area é ", a)


# 7 Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def area_quadrado():
    a = int(input("Quantos cm tem o lado do seu quadrado? "))
    area = a * a
    dobro = area * 2
    print("A area é", area, "e dobro da area é", dobro)

# 8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

def salario_hora ():
    salario = float(input("Quantos você ganha por hora?"))
    horas = int(input("E quantas horas você trabalha?"))
    horas_salario = horas * salario
    print("Você trabalhou", horas, "horas e recebeu R$", horas_salario)

# 9 Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).
def f_para_c ():
    f = int(input("Qual a temperatura em graus Fahrenheit? "))
    c = 5 * ((f - 32) / 9)
    print("A temperatura em graus Celsius é", c)

# 10 Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F = (C*9/5) + 32
def c_para_f ():
    c = float(input("Qual a temperatura em graus Celsius? "))
    f = (c*9/5) + 32
    print("A temperatura em graus Fahrenheit é", f)

