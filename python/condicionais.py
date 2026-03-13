# condicional if
# acompanhada = 'Sim'
# idade = 14


# if idade >=18:
#     print('Você pode assistir o filme')
# elif (idade >=15 and idade <=17 ) and acompanhada == 'Sim':
#     print('Você pode assistir o filme')
# else:
#     print('Você não pode assistir o filme')
print('0 - cadastrar')
print('1 - editar')
print('2 - excluir')

opcao = int(input('O que deseja realizar'))

match opcao:
    case 0:
        print('voce escolheu cadastrar')
    case 1:
        print('voce escolheu editar')
    case 2:
        print('voce escolheu excluir')
    case _:
        print('opção invalida')
