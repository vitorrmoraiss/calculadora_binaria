# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:33:30 2019

@author: vitor
"""

# Implementar um programa para conversão de bases
#Tal programa deve receber um número e sua base de entrada e a base de saída
#O programa deve verificar se o número informado é válido e convertê-lo para a base de saída
#O programa deve aceitar números fracionários



print (""" \n Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para DECIMAL
[ 4 ] Converter para HEXADECIMAL """)
  

    


opcao = int(input("Sua opção: "))

#CONVERTER PARA BINÁRIO
if opcao == 1:

#PARTE INTEIRA
    num = int(input("Digite um número: "))
    

    num_int = int(num)
    bin_int = ''
    while num_int > 0:
        resto = num_int % 2
        bin_int = str(resto) + bin_int
        num_int = num_int // 2
    
#PARTE FRACIONÁRIA
    num_frac = num - int(num)
    bin_frac = ''
    for cont in range(8):
        num_frac *= 2
        bin_frac += str(int(num_frac))
        num_frac = int(num_frac)
        if num_frac == 0:
            break
    
    print(" \n Número convertido: ",bin_int + '.' + bin_frac)
    

#CONVERTER PARA OCTAL   
elif opcao == 2:
    
   
    num = str(input('Digite um número: '))
        
    l_partes = num.split('.')
    num_int = l_partes[0]
    num_frac = l_partes[1]
    soma = 0.0
        
    for cont in range(len(num_int)):
        dig = num_int[-(cont+1)]
        num_dig = float(dig)
        soma += num_dig*8**cont
        
    print (soma)
    
    for cont in range(len(num_frac)):
        dig = num_int[-(cont+1)]
        num_dig = float(dig)
    print(" \n Número convertido: ",soma)
        
#CONVERTENDO PARA DECIMAL
elif opcao == 3:
    
    num = str(input("Digite um número: "))

    
    l_partes = num.split('.')
    num_int = l_partes[0]
    num_frac = l_partes[1]
    soma = 0.0
    
    for cont in range(len(num_int)):
        dig = num_int[-(cont+1)]
        num_dig = float(dig)
        soma += num_dig*2**cont
    
    for cont in range(len(num_frac)):
        num_dig = float(num_frac[cont])
        exp = -(cont + 1)
        soma += num_dig*2**exp

    
    print('\n Número convertido :', soma)
    
    
    
#CONVERTER PARA HEXADECIMAL
elif opcao == 4:
    
    num = str(input("Digite um número: "))


    l_partes = num.split('.')
    num_int = l_partes[0]
    num_frac = l_partes[1]
    soma = 0.0
    
    def dig_hex(dig):
        if dig.lower() == 'a':
            return 10.0
        elif dig.lower() == 'b':
            return 11.0
        elif dig.lower() == 'c':
            return 12.0
        elif dig.lower() == 'd':
            return 13.0
        elif dig.lower() == 'e':
            return 14.0
        elif dig.lower() == 'f':
            return 15.0
        else:
            return float(dig.lower)
   
    print( '\n Número convertido: ', )







 