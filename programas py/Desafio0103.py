n1 = float(input('primeiro valor: '))
n2 = float(input('segundo valor: '))
soma = n1 + n2
print('A soma float é: ', soma)
n3 = int(input('primeiro valor: '))
n4 = int(input('segundo valor: '))
ssoma = n3 + n4
print('A soma int é: ', ssoma)

# Note by Saiki: https://www.programiz.com/python-programming/string-interpolation
# Vc pode fazer as somas sem atribuí-las em variáveis, confira:
print('A soma dos números é: ' + (n1 + n2))

# Você também pode inseri-las no meio das string, utilizando as f-strings:
# Apenas coloque o código que vc quer dentro de chaves, e pronto -
# ele será executado
print(f'A soma dos números é: {n1 + n2}.')

word = 'tecnologias'
print(f'Cada dia, as {word} vão dominar o mundo :D')

# Sendo o mais arcaico, vc também pode utilizar a boa e velha 
# string interpolation com %
print('Cada dia, as %s vão dominar o mundo :D'%(word))

print('Cada dia, as %(word)s vão dominar o mundo :D')

# Ou por último
print('Cada dia, as {} vão dominar o mundo :D'.format(word))