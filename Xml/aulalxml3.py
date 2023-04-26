from lxml import etree

dados = etree.parse("Ano-2017.xml")
todas_despesas = dados.findall("DESPESAS")
parlamentar = 'ABEL MESQUITA JR.'

for despesas in todas_despesas:
    for despesa in despesas:
        desp = despesa.getchildren()

        if desp[0].text == parlamentar:
            print("Despesa:", desp[8].text, "- Valor:", desp[18].text)