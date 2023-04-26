#Nesse programa irei melhorar o código do desafio anterior
#o arquivo que foi usado é muito grande para coloca-lo aqui no repositório no git hub
from lxml import etree
import locale

def carregar_dados():
    dicionario_deputados = {}
    dados = etree.parse("Ano-2017.xml")
    listas_depesas = dados.findall('DESPESAS')
    for despesa in listas_depesas:
        for informacao in despesa:
            propriedades = informacao.getchildren()
            if propriedades[18].tag == 'vlrLiquido':
                nome = propriedades[0].text
                categoria = propriedades[8].text
                valor_despesa = propriedades[18].text

                if "," not in valor_despesa:
                    valor_despesa = valor_despesa + ",00"

                valor_despesa = float(valor_despesa.replace(',','.'))

                if nome in dicionario_deputados:
                    dicionario = dicionario_deputados[nome]
                    if categoria in dicionario:
                        dicionario[categoria] += valor_despesa
                    else:
                        dicionario[categoria] = valor_despesa
                    
                    dicionario_deputados[nome] = dicionario
                else:
                    dic = {}
                    dic[categoria] = valor_despesa
                    dicionario_deputados[nome] = dic
    return dicionario_deputados

def formatar_valor(valor):
    locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')
    valor = locale.currency(valor, grouping=True, symbol=None)
    locale.setlocale(locale.LC_ALL, '')
    return valor

if __name__ == "__main__":
    dicionario = carregar_dados()

    while True:
        total_despesas = 0
        deputado = input("Informe o nome do deputado (ou 0 (zero) para sair): ").upper()
        if deputado == "0":
            break
        elif deputado in dicionario:
            for chave, valor in dicionario[deputado].items():
                total_despesas += valor
                valor = formatar_valor(valor)
                print(f"{chave}: {valor}")
            total_despesas = formatar_valor(total_despesas)
            print(f"Total despesas: {total_despesas}")
    

        else:
            input("Deputado não localizado! Pressione qualquer tecla para ver a lista de deputados. ")
            for nome in dicionario.keys():
                print(nome)

    
    print("-----------Obrigado por usar meu programa--------------")