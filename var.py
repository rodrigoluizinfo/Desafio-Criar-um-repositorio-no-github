# print('\nCurso DIO - Introdução à programação com Python')
#
# # Variáveis pr
# # a = 5
# # b = 6
#
# # Dados sendo solicitados
# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
#
# soma = a + b
# sub = a - b
# multi = a * b
# div = a / b
# resto = a % b
#
# print('============Sem concatenação==================\n')
# print(soma)
# print(sub)
# print(multi)
# print(div)
# print(str(resto) + '\n')
#
# print('============Com concatenação(Incorreto)==================\n')
# print('A soma é: ' + str(soma))
# print('A subtração é: ' + str(sub))
# print('A multiplicação é: ' + str(multi))
# print('A divisão é: ' + str(div))
# print('O resto é: ' + str(resto) + '\n')
#
# print('============Com concatenação(Correto)==================\n')
#
# #Forma 1: A concatenção é feita ao apresentar o resultado
# # print('A soma é: {soma}\n'
# #       'A subtração: {sub}\n'
# #       'A multiplicação é: {multi}\n'5
# #       'A divisão é: {div}\n'
# #       'O resto é: {resto}\n'
# #       .format(soma=soma, sub=sub, multi=multi, div=div, resto=resto))
#
# #Forma 2: A concatenação é armazenada em uma variável
# resultado = ('A soma é: {soma}\n'
#       'A subtração: {sub}\n'
#       'A multiplicação é: {multi}\n'
#       'A divisão é: {div}\n'
#       'O resto é: {resto}\n'.format(soma=soma, sub=sub, multi=multi, div=div, resto=resto))
#
# print(resultado)
#
#
#
