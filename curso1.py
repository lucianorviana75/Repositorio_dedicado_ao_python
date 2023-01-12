
#MUNDO UM-------------

#OS EXERCICIOS COMEÇÃO NA AULA 005.
# Exercicio 01 ao 035(PRIMEIROS PASSOS COM PYTHON)

# Exercicio 001 -Deixando tudo pronto ( Aula 03)
# Crie um programa que escreva "Olá Mundo!" na tela.
print('Olá Mundo!')

#Exercicio 002 -respondendo ao usuario ( Aaula 03)
#Faça um programa que leia o nome de uma pessoa .
#E mostre uma mensagem de boas-vindas.
nome= input('Digite seu nome .' )
print('Prazer em conhece - lo {}!' . format(nome))


#AULA 006 (TIPOS PRIMITIVOS E SAIDA DE DADOS)

#Exercicio 003 -Somando dois numeros( Aula 06)
# Crie um programa que leie dois numeros e mostre a soma entre eles;

n1 = int(input('Digite um valor ;'))
n2 = int(input('Digite outro valor ; '))
s = n1 + n2
print ( 'A soma entre o valor {} e o valor {} é {} . ' . format(n1,n2,s))

# Exercicio 004 -Dissecando uma variavel( Aula 06)
# Faça um programa que leia algo pelo teclado e mostre na tela.
# O seu tipo primitivo e todas as informações possiveis.
casa = str(input('Digite algo :'))
print('O tipo primitivo desse valor é ', type(casa))
print('Só tem espaços ? ', a.isnumeric())
print('É alfabetico ?' ,a.isalpha())
print('É alfanumerico ?' ,a.isalnum())
print('É maiuscula ?' ,a.isupper())
print('É minuscula ?' ,a.islower())
print('Éla esta capitalizada ?' ,a.istitle())


# AULA 007 (OPERANDO ARTMÉTICOS)

# exercicio 005 -Antecessor e sucessor .(Aula 07)
# Faça um programa que leia um número inteiro e mostre na tela o seu
# sucessor e o antecessor.
# exemplo_1 

n=int(input('*Digite um valor'))
x=n-1
y=n+1
print('Analisando o valor {},seu antecessor é {} e o seu sucessor é {} .' . format(n,x,y))

#exemplo_2

n=int(input('*Digite um valor'))
print('Analisando o valor {} ,seu antecessor é {} e o seu sucessor é {} .'. format(n,(n-1),(n+1)) 


# Exercicio 006 -Doblo ,Triplo, Raiz Quadrada .(Aula 07).
# Crie um algoritmo que leie um número e mostre o seu dobro , triplo e Raiz Quadrada.
#exemplo _1

n=int(input('*Digite um numero '))
x=n*2
y=n*3
z=n**(1/2)
print('O dobro de {} vale {} .' . format(n,x))
print('O triplo de {} vale {}.\n A raiz de {} é igual a {:.2f} .' . format(n , y ,n , z ))


#exemplo_2

n=int(input('*Digite um valor '))
print('Analisando o valor de {} o dobro é {} *\nO triplo é {} .' . format(n ,(n*2),(n*3)))
print('A raiz quadrada de {} e igual a {:.2f} .' . format(n,(pow(n ,1/2))))

# Exercicio 007 -Média  Aritmética . (Aula 07)
# Desenvolva um programa que leia as duas notas de um aluno ,
# calcule e mostre sua média.

n1=float(input('peimeira nota do aluno'))
n2=float(input('segunda nota do aluno'))
x=(n1+n2)/2 #seguir a hordem de precedencia:

print('a media entre {:.1f} e {:.1f} é igual a {:.1f}.' . format(n1,n2,x))


# Exercicio 008 -Conversor de Medida. (Aula 07)
# Escreva um programa que leia um valor em metros,
# e o exiba convertido em centimetros e milimetros.

medida =float(input('uma distancia em metros'))
cm=medida *100
mm=medida*1000
print('a medida de {} corresponde a {:.1f} cm e a {:.1f} mm .' . format(medida,cm,mm)) 


# Exercicio 009 -Tabuada .(Aula 07)
# faça um programa que leia um numero interiro qualquer,
# e mostre na tela a sua tabuada.

num= int(input('digite um numero para ver sua tabuada'))
print('-'*12)
print('{}x{:2}={}' .  format(num, 1, num*1))
print('{}x{:2}={}' .  format(num, 2, num*2))
print('{}x{:2}={}' .  format(num, 3, num*3))
print('{}x{:2}={}' .  format(num, 4, num*4))
print('{}x{:2}={}' .  format(num, 5, num*5))
print('{}x{:2}={}' .  format(num, 6, num*6))
print('{}X{:2}={}' .  format(num, 7, num*7))
print('{}X{:2}={}' .  format(num, 8, num*8))
print('{}X{:2}={}' .  format(num, 9, num*9))
print('{}X{:2}={}' .  format(num, 10,num*10))
print('-'*12)

# Exercicio 010 -Conversor de Moedas.(Aula 07)
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,
# e mostre quantos dólares ela pode comprar.

Real=float(input('quanto voce tem na carteira? R$'))
Dolar=Real/ 3.27
print('com R${:.2f} voce pode comprar  USS{:.2f}' .  format(Real,Dolar))


#Exercicio 011 -Pintando Parede. (Aula 07)
# Faça um programa que leie a largura e a altura de uma parede em metros,
# Calcule a sua área e a quantidade de tinta necessária para pinta-lá,
# sabendo que cada litro de tinta ,pinta uma area de 2 metros quadrados.

# Eu fiz.

n= int(input('qual a altura da parede? '))
print( n ,'metros')
m= int(input('qual a largura da parede? '))
print( m ,'metros')
x=n*m
print('a metragem total da parede é de {} metros² :' . format(x,n,m))
print('quanto de tinta preciso pra pintar a parede ?')
print('Cada litro de tinta pinta uma area de 2m² .')
r=x*500
print ('E necessario {}litros de tinta pra pintar a parede .' . format(r,n,m))


# Exercicio do curso

larg=float(input('largura da parede ;'))
alt=float(input('altura da parede ;'))
Área= larg*alt
print('sua parede tem a dimençao de {} x{} e sua area é de {} m².' .  format(Área,larg,alt))
tinta= Área/ 2
print('para pintar sua parede, voce precisará de  {}l de tinta. ' .  format(tinta))

#exercicio 12 -Calculando Descontos (Aula 07)
# Faça um algoritimo que leia o preço de um produto,
# e mostre seu novo preço, com 5% de desconto.

preço=float(input('qual e o valor do produto ?'))
novo=preço-(preço*5/100)
print('o produto que estava R${}, na promoçao com 5% de desconto agora custa  R${} .' .  format(preço,novo))


#exercicio 012 (acertei)

a=str(input(' produto '))
print(a)
b=float(input(' valor '))
print(b ,'reais')
r=b-5*b/100
print('valor atual do produto com desconto de 5%  é {} .' . format(r,5,b))



# Exercicio 013 -Reajuste salarial(Aula 007)
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário ,
# com 15% de aumento.

b=str(input('funcionario '))
print('Funcionario ', b)
c=float(input('salario :'))
r=c+15*c/100
print('o novo salario de ',b, 'com o acrecimo de 15% é de,{} reais .' .  format(r,c,15))

# Exercicio 014 -conversor de temperatura.(Aula 007)
# Escreva um programa que converta uma temperatura digitando em graus Celsius,
# e converta para graus fahrenheit.

C =float(input('Informe a temperatura em ºC: '))
F = ((9*c) /5) + 32
print('A temperatura de {} ºC corresponde a {} ºF!' . format(C,F))


# Exercicio 15 -Aluguél de carros. (aula 007)
# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado,
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar , sabendo que o carro custa R$60 por dia e R$ 0,15 por Km rodado.

dias = int(input('Quantos dias alugados ? '))
km = float(input('Quantos km rodados ? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f} ' . format(pago))



#correçao do exercicio 016 (quebrando um numero) (Aula 008)
#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira.
#exemplo;Digite um numero ; 6.127
# O numero 6.127 tem a parte inteira 6.

import math
num = float(input('Digite um valor  '))
print('o valor digitado foi {} e a sua porção inteira é {}' . format(num, math.trunc(num)))

#ou

from math import trunc
num = float (input ('Digite um valor '))
print('o valor digitado foi {} e a sua porçao inteira é {} ' . format(num, trunc(num)))

#ou 

num = float (input('Digite um valor '))
print('O valor ddigitado foi {} e a sua porçao inteira é {} ' . format(num, int(num)))

# exercicio 017 (catetos e ipotenusas) (aula 008)
#Faça um programa que leia o comprimento do cateto oposto e a do cateto adjacente  de um triangulo rêtangulo , calcule a mostre o comprimento da hipotenusa.
#comprimento do cateto oposto:3.5
#comprimento do cateto adjacente:4.75
#A hipotenusa vai medir 5.90.

co = float(input('Comprimento do cateto oposto  '))
ca = float(input('comprimento do cateto adjacente  '))
hi = (co**2 + ca**2) **(1/2)
print('A hipotenusa vai medir {:.2f}' . format (hi))

#ou

import math     #ou (from math impot hypot)
co= float (input('Comprimento do cateto oposto '))
ca= float (input('Comprimento do cateto adjacente '))
hi= math.hypot(co, ca)    #(hypot(co, ca))
print('A hipotenusa vai medir {:.2f}' . format(hi))


#exercicio 018;(Aula 008)

#Faça programa que leia um ângulo qualquer e mostre na telao valor do seno ,coseno,e tangente desse Ângulo;
#Digite um valor ; 30
#R:
#o angulo de 30.0 tem o seno de 0.50
#o angulo de 30.0 tem o coseno 0.87
#o angulo de 30.0 tem o tangente 0.58

import math
Ângulo = float(input('Digite o angulo que você deseja:'))
seno = math.sin(math.radians(Ângulo))
print('O angulo de {} tem o seno de {:.2} '. format(Ângulo, seno))
cosseno = math.cos(math.radians(Ângulo))
print('O angulo de {} tem o cosseno de {:.2} ' . format(Ângulo , cosseno))
tangente = math.tan (math.radians(Ângulo))
print('O angulo de {} tem o tangente de {:.2} ' . format(Ângulo , tangente))

#ou

from math import radians, sin, cos, tan
Ângulo = float(input('Digite o angulo que você deseja:'))
seno = sin(radians(Ângulo))
print('O angulo de {} tem o seno de {:.2} ' . format(Ângulo, seno))
cosseno = cos(radians(Ângulo))
print('O angulo de {}tem o cosseno de {:.2} ' . format(Ângulo, cosseno))
tangente = tan(radians(Ângulo))
print('O angulo de {} tem o tangente de {:.2} ' . format(Ângulo, tangente))

# Exercicio 019 -Sorteando um item na lista (Aula 008)
# um Professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele ,lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido.

import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno : '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno :  '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}' . format(escolhido))

 
# Exercicio 020 -Sorteando uma ordem na lista.(Aula008)
# O mesmoprofessor do desafio 19 quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = str(input('Primeiro aluno : '))
n2 = str(input('Segundo aluno  : '))
n3 = str(input('Terceiro aluno : '))
n4 = str(input('Quarto aluno   : '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)

from random import shuffle
n1 = str(input('Primeiro aluno : '))
n2 = str(input('Segundo aluno  : '))
n3 = str(input('Terceiro aluno : '))
n4 = str(input('Quarto aluno   : '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)


# Exercicio 021 -Tocando um MP3.(Aula 008)
# Faça um programa em python que abra e reproduza o áudio de um arquivo de MP3.
import pygame #pygame é um modulo.
pygame.init()
pygame.mixer.music.load('/home/luciano/Música/newboys/021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#AULA 09(MANIPULANDO TEXTO)

#Exercicio 022 -Analizador de textos .(Aula 009)
#Crie um programa que leia um nome completo de uma pessoa e mostre:
#O nome com todas as letras maíusculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo ')).strip()
print('Analisando seu nome...' )
print('Seu nome maiusculo é {}' . format(nome.upper()))
print('Seu nome minusculo é  {}'. format(nome.lower()))
print('Seu nome tem ao todo {} '. format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {}' . format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele Tem {} letras .' . format(separa[0], len (separa[0])))


#Exercicio 023 -Separando digitos de um número. (Aula 009)
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digidos separados.
#ex; Digite um número : 1834
#unidade :4 dezena :3 centena :8 milhar :1

num = int(input('Informe um numero : '))
n=str(num)
print('Analisando o numero {} ;' . format(num))
print('unidade :{}' . format(n[3]))
print('Dezena :{} ' . format(n[2]))
print('Centena :{} '. format(n[1]))
print('Milhar :{} ' . format(n[0]))


num = int(input('Informe um numero :'))# o correto.
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {} '. format(num))
print('Unidade : {} '. format(u))
print('Dezena : {} ' . format(d))
print('Centena : {} '. format(c))
print('Milhar : {} ' . format(m))

num = int(input('Informe um numero :'))
u = num // 1 % 10
d = num // 1 % 100
c = num // 1 % 1000
m = num // 1 % 10000
print('Analisando o número {} '. format(num))
print('Unidade : {} '. format(u))
print('Dezena : {} ' . format(d))
print('Centena : {} '. format(c))
print('Milhar : {} ' . format(m))

#Exercicio 024 -Verificando as primeiras letras de um texto. (Aula 009)
#Crie um programa que leia o nome de uma cidade
#E diga se ela começa ou nao com o nome santo;cidade = str(input('Em que cidade você nasceu ?')).strip() # Elimina os espaços.
print(cidade[:5].upper() == 'SANTO') #[:5] = a SANTO =  0=S,1=A,2=N,3=T,4=O


#Exercicio 025 -Procurando uma string dentro de outra. (Aula 009)
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva "no nome.

nome = str(input('Qual é o seu nome completo ?')). strip()
print('Seu nome tem silva ?{}' . format('silva' in nome)) 


#Exercicio 026 -Primeira e ultima ocorrência de uma uma string.(Aula 009)
#Faça um programa que leie uma frase pelo teclado e mostre:

#Quantas vezes aparece a letra ''A''.
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase  ')).upper().strip()
print('A letra A aparece {} vezes na frase  '. format(frase.count('A')))
print('A primeira letra A aparece na posiçao {} ' . format(frase.find('A')+1))
print('A ultima letra A aparece na posição {} ' . format(frase.rfind('A')+1))

#Exercicio 027 - primeiro e ultimo nome de uma pessoa .(Aula 009)
# EX;                                    :
# Digite seu nome completo:              :
# Muito prazer em te conhgecer.          :
# Seu primeiro nome é Maria              :
# Seu último nome é anjos                :
#----------------------------------------
#Faça um programa que leia o nome completo de uma pessoa ;
#Mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo ')).strip()
nome = n.split()
print('muito prazer em te conhecer, {} !' . format(nome))
print('O meu primeiro nome é, {} ' . format(nome[0]))
print('O meu ultimo nome é, {} ' . format(nome[len(nome)-1]))

# AULA 010 (CONDIÇÕES EM PYTHON (if,,else)
#correção do exercicio 028 do curso em video da aula 010.

#jogo de advinhação:
#Escreva um programa que fassa o computador "pensar" em um numero inteiro entre 0 e 5 e peça pra o
#usuario para tentar descobrir qual foi o numero escolhido pelo computador.
#o programa deverar escrever na tela se o usuário venceu ou perdeu.

#da biblioteca random importei randint

from random import randint
computador = randint(0, 50)              # faz o computador pensar...
print('-=-'*20)
print('Vou pensar em numero entre 0 e 50. tente advinhar...')
print('-=-'*20)
jogador = int(input('em que numero eu pensei ? '))      #jogador tenta advinhar
if jogador == computador :
    print('PARABENS ! você conseguil me vencer !')
else:
    print('GANHEI ! eu pensei no numero {} e não no {} ! ' . format(jogado,computador))

# correção do exercicio 029

#escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80 km/h ,mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00  por cada km acima do limite.

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80 :
    print('MULTADO ! Voce excedeu o limite permitido que é de 80 km/h ')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa que é de R${:.2f} ! ' .format(multa))
print('Tenha um bom dia ! Dirija com segurança !')

#correção do exercicio 030

#crie um programa que leie um numero inteiro e mostre na tela se ele e par ou impar.

numero = int(input('Me diga um numero qualquer ! '))
resultado = numero %2
if resultado == 0:
    print(' O numero {} é par' . format(numero))
else:
    print('O numero é impar ' . format(numero))

#correção do exercicio 031

#Desenvolva um programa que pergunte a distancia de uma  viagem em km.
#Calcule o preço da passagem ,cobrando R$0,50 por km para viagens de até 200km, e R$0,45 para viagens mais longas.

#forma-1
distancia = float(input('Qual é a distancia de sua viagem ?'))
print('Você esta preste a começar uma viagem de {}km .' . format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço de sua passagem será de R${:.2f}' . format(preço))

#forma-2 (simplificado)
distancia = float(input('Qual é a distancia de sua viagem ?'))
print('Você esta preste a começar uma viagem de {}km .' . format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço de sua passagem será de R${:.2f}' . format(preço))

#correção do exercicio 032

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual :'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ano {} é BISSEXTO' . format(ano))
else :
    print('O ano {} NÃO É BISSEXTO ' . format(ano))

# Correção do exercicio 033 (Maior e Menores valores)
#Faça um programa que leia trẽs numeros e mostra qual é o maio e qual é o menor;

a = int(input('Primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
menor = a # verificando quem é o menor;
if b < a and b < c:
    menor = b
if c <a and c < b:
    menor  = c
maior = a # verificando quem e o maior;
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {} ' . format(menor))
print('O maior valor digitado foi {} ' . format(maior))

#correção do exercicio 034
#Escreva um programa que pergunte o salario de um funcionario.
#Calcule o valor do seu almento.
#para salrios superiores a R$1.250.00, calcule um aumento de 10%.
#Para os inferiores ou iguais , o almento e de 15%.

salario = float(input('Qual o salario do funcionario? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print(' Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. ' . format(salario, novo))    

# Correção do exercicio 035 (ultimo da aula 10).
# Desenvolva um programa que leia o comprimento de três retas.
# E diga ao usuario se elas podem ou não formar um triângulo.

print('-='*20)
print('Analizador de triangulos ')
print('-='*20)
r1 = float(input('Primeiro seguimento ;'))
r2 = float(input('Segundo seguimento ; '))
r3 = float(input('Terceiro seguimento ; '))
if r1< r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 :
    print('Os seguimentos acima PODEM FORMAR triângulo ! ')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR triângulo ! ')  
 

















    

