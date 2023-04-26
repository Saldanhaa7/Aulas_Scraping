#Primeiro desafio do curso!

#Nesse desafio terei que fazer um programa que leia o nome dos deputados do arquivo que foi passado,
#e devolvendo como resposta as despesas desse deputado.

#Primeiramente vou importar o pacote etree da biblioteca lxml e a biblioteca locale

#o arquivo que foi usado é muito grande para coloca-lo aqui no repositório no git hub
from lxml import etree
import locale

#Agora tenho que carregar o arquivo xml
def carregar_lista_deputados():
    dados = etree.parse("Ano-2017.xml")
    lista_despesas = dados.findall('DESPESAS')

    lista_deputado = []
    for despesa in lista_despesas:
        for informacao in despesa:
            registros = informacao.getchildren()
            deputado = registros[0].text
            if deputado not in lista_deputado:
                lista_deputado.append(deputado)

    return lista_deputado

def carregar_despesas(deputado):
    categorias = {} # CRIANDO DICIONÁRIO DE CATEGORIAS
    dados = etree.parse("Ano-2017.xml") # CARREGA O ARQUIVO XML
    todas_despesas = dados.findall("DESPESAS") # GERA UM OBJETO LISTA COM VÁRIOS ELEMENTOS "DESPESAS"
    for despesas in todas_despesas: # PERCORRENDO A LISTA DE ELEMENTOS "DESPESAS", OBTENDO UM OBJETO "DESPESAS" ESPECÍFICO
        for despesa in despesas: # NAVEGAR DENTRO DO OBJETO DESPESA
            desp = despesa.getchildren() # CARREGAR OS FILHOS DO OBJETO DESPESA
            if desp[0].text == deputado: # COMPARAR O NOME DO DEPUTADO DE txNomeParlamentar COM O NOME RECEBIDO POR PARÂMETRO
                if desp[18].tag == 'vlrLiquido':
                    categoria_despesa = desp[8].text # PEGAR O NOME DA CATEGORIA DA DESPESA
                    valor_despesa = desp[18].text # PEGAR O VALOR DA DESPESA

                    if "," not in valor_despesa: # SE NÃO TIVER VÍRGULA NO VALOR DA DESPESA
                        valor_despesa = valor_despesa + ",00" # ADICIONAR ",00"
                    valor_despesa = float(valor_despesa.replace(',','.')) # SUBSTITUIR A VÍRGULA POR PONTO E CONVERTER PARA FLOAT

                    if categoria_despesa in categorias: # SE A CATEGORIA DA DESPESA (txtDescricao) ESTIVER DENTRO DO DICIONÁRIO DE CATEGORIAS
                        categorias[categoria_despesa] = float(categorias[categoria_despesa]) + valor_despesa # SOMAR O VALOR DA DESPESA QUE ESTÁ NO DICIONÁRIO COM O NOVO valor_despesa
                    else:
                        categorias[categoria_despesa] = valor_despesa # SE A CATEGORIA DA DESPESA NÃO EXISTIR, CRIAR ESTA CHAVE NO DICIONÁRIO COM O VALOR DA DESPESA

    total_despesas = 0
    for chave, valor in categorias.items(): # PERCORRER OS ITENS DO DICIONÁRIO DE CATEGORIAS, PEGANDO CHAVE E VALOR
        total_despesas += valor # ACRESCENTAR AO todas_despesas O VALOR DA DESPESA
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # MUDAR A CONFIGURAÇÃO DE MOEDA, NÚMEROS, ETC PARA pt_BR
        valor = locale.currency(valor, grouping=True, symbol=None) # FORMATAR A VARIÁVEL valor COMO MOEDA, SEM SÍMBOLO (R$) E COLOCANDO O PONTO PARA MILHAR
        locale.setlocale(locale.LC_ALL, '') # RETORNANDO A CONFIGURAÇÃO PADRÃO DO SISTEMA
        print("Categoria:", chave, "- Valor:", valor) # IMPRIMINDO A CATEGORIA E TOTAL DAS DESPESAS

    # MUDANDO A CONFIGURAÇÃO PARA pt_BR
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    # FORMATANDO O TOTAL DE DESPESAS
    total_despesas = locale.currency(total_despesas, grouping=True, symbol=None) 
    # RETORNANDO A CONFIGURAÇÃO PADRÃO DO SISTEMA
    locale.setlocale(locale.LC_ALL, '')

    # IMPRIMINDO O TOTAL DE DESPESAS FORMATADO
    print(f"Total despesas: {total_despesas}")


if __name__ == "__main__":
    lista_deputados = carregar_lista_deputados()

    while True:
        deputado = input("Informe o nome do deputado (ou 0 (zero) para sair): ").upper()
        if deputado == "0":
            break
        elif deputado in lista_deputados:
            carregar_despesas(deputado)
        else:
            input("Deputado não localizado! Pressione qualquer tecla ver a lista de deputados.")
            print(lista_deputados)

    print("---Obrigado por utilizar o sistema---")