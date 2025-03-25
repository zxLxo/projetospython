primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

pvf = float(primeiro_valor)
svf = float(segundo_valor)

if pvf > svf:
    print(f'O primeiro valor: {pvf} é maior que o segundo valor: {svf}')
elif svf > pvf:
    print(f'O segundo valor: {svf} é maior que o primeiro valor: {pvf}')