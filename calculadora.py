'''
Regras:
--> Receber as seguintes informações:
    - Graduação
        1- Oficiais Generais
        2- Oficiais Superiores
        3- Oficiais
        4- Suboficiais, Aspirantes, Cadetes e Sargentos
        5- Alunos do CPOR
        6- Demais praças e praças especiais
    - existencia de dependentes
    - valor do soldo
    - variáveis
    - qtd de módulos
    - localidade dos módulos
        1- Brasilia, Manaus e Rio de Janeiro
        2- Belo Horizonte, Fortaleza, Porto Alegre, Recife, Salvador e São Paulo
        3- Outras capitais
        4- demais localidades
    - quantidade de dias de cada módulo
--> Para comissionamentos com total de dias => 90 o pagamento de ajuda de custo é automatico.
--> Na contabilização de dias em diárias o total é qtd_dia - 0.5
--> A cada módulo é acrescido 95.00 (95 * qtd de módulos)
--> Em caso de um comissionamento com dias > 14 and <90, deverá ser feito um comparativo entre diárias e ajuda de custo sendo apresentado qual pagamento mais viavel.
--> para o calculo de ajuda de custo:
    dias > 90 com de dependentes
        ajuda de custo * 3
    dias > 90 sem dependentes
        ajuda custo * 1,5
    dias < 90 com dependentes
        ajuda de custo * 2
    dias < 90 sem dependentes
        ajuda de custo * 1
'''
tot_dias = 0
tot_diaria = 0
tot_valor_diaria = 0
subtot_ajuda_custo = 0
variaveis = None
tot_ajuda_custo = 0


print("1- Oficiais Generais\n2- Oficiais Superiores\n3- Oficiais\n4- Suboficiais, Aspirantes, Cadetes e Sargentos\n5- Alunos do CPOR\n6- Demais praças e praças especiais")

graduacao = int(input(
    'Informe o código da graduação do militar conforme a lista: '))

dependente = input('O militar tem dependentes (s/n)?: ')

while dependente != 's' and dependente != 'n':
    dependente = input('Erro: Informe s para sim ou n para não! ')

if dependente == 's':
    dep = True

elif dependente == 'n':
    dep = False

soldo = float(input('Informe o valor do soldo do militar: '))
subtot_ajuda_custo = float(subtot_ajuda_custo + soldo)

while variaveis != 0:
    variaveis = float(input(
        'Informe o valor da variavel a ser incluida (0 para concluir): '))
    subtot_ajuda_custo = subtot_ajuda_custo + variaveis

qtd_modulos = int(input("Informe a quantidade total de módulos: "))

for dias in range(qtd_modulos):
    dias = float(input(f'Informe quantos dias tem o módulo {dias++1}:'))
    tot_dias = tot_dias + dias
    tot_diaria = (dias-0.5) + tot_diaria
    cod_localizacao = int(input(
        f"1- Brasilia, Manaus e Rio de Janeiro\n2- Belo Horizonte, Fortaleza, Porto Alegre, Recife, Salvador e São Paulo\n3- Outras capitais\n4- demais localidades\nInforme a localidade do módulo {dias++1} pelo código conforme a lista: "))

    if graduacao == 1:
        if cod_localizacao == 1:
            diaria = ((dias-0.5) * 321.10)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 2:
            diaria = ((dias-0.5) * 304.20)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 3:
            diaria = ((dias-0.5) * 287.30)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 4:
            diaria = ((dias-0.5)*253.50)+95
            tot_valor_diaria = tot_valor_diaria + diaria

    if graduacao == 2:
        if cod_localizacao == 1:
            diaria = ((dias-0.5) * 267.90)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 2:
            diaria = ((dias-0.5) * 253.80)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 3:
            diaria = ((dias-0.5) * 239.7)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 4:
            diaria = ((dias-0.5)*211.50)+95
            tot_valor_diaria = tot_valor_diaria + diaria

    if graduacao == 3:
        if cod_localizacao == 1:
            diaria = ((dias-0.5) * 224.20)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 2:
            diaria = ((dias-0.5) * 212.40)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 3:
            diaria = ((dias-0.5) * 200.60)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 4:
            diaria = ((dias-0.5)*177)+95
            tot_valor_diaria = tot_valor_diaria + diaria

    if graduacao == 4:
        if cod_localizacao == 1:
            diaria = ((dias-0.5) * 224.20)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 2:
            diaria = ((dias-0.5) * 212.40)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 3:
            diaria = ((dias-0.5) * 200.60)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 4:
            diaria = ((dias-0.5)*177)+95
            tot_valor_diaria = tot_valor_diaria + diaria

    if graduacao == 5:
        if cod_localizacao == 1:
            diaria = ((dias-0.5) * 186.20)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 2:
            diaria = ((dias-0.5) * 176.40)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 3:
            diaria = ((dias-0.5) * 166.60)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 4:
            diaria = ((dias-0.5)*147)+95
            tot_valor_diaria = tot_valor_diaria + diaria

    if graduacao == 5:
        if cod_localizacao == 1:
            diaria = ((dias-0.5) * 186.20)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 2:
            diaria = ((dias-0.5) * 176.40)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 3:
            diaria = ((dias-0.5) * 166.60)+95
            tot_valor_diaria = tot_valor_diaria + diaria

        elif cod_localizacao == 6:
            diaria = ((dias-0.5)*147)+95
            tot_valor_diaria = tot_valor_diaria + diaria

if tot_dias >= 90:
    if dep == True:
        tot_ajuda_custo = subtot_ajuda_custo * 3
    else:
        tot_ajuda_custo = subtot_ajuda_custo * 1.5
    print(
        f'O comissionamento tem um total de {tot_dias} dias. A indenização a ser paga é Ajuda de Custo no valor de: {tot_ajuda_custo}')

# Até este ponto o código está funcionando sem erros, falta acrescentar as regras de comparação e entrega de valores para comissionamentos com < 90 dias.
