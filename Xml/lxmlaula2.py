from lxml import etree

clientes = etree.Element("clientes")
cliente1 = etree.SubElement(clientes, "cliente")
nome1 = etree.SubElement(cliente1, "nome")
nome1.text = "nome do primeiro cliente!"
idade1 = etree.SubElement(cliente1, "idade")
idade1.text = "20"
sexo1 = etree.SubElement(cliente1, "sexo")
sexo1.text = "masculino"
cpf1 = etree.SubElement(cliente1, "cpf")
cpf1.text = "123.456.789-00"

cliente2 = etree.SubElement(clientes, "cliente2")
nome2 = etree.SubElement(cliente2, "nome")
nome2.text = "nome do segundo cliente!"
idade2 = etree.SubElement(cliente2, "idade")
idade2.text = "19"
sexo2 = etree.SubElement(cliente2, "sexo")
sexo2.text = "masculino"
cpf2 = etree.SubElement(cliente2, "cpf")
cpf2.text = "123.456.789-01"

cliente3 = etree.SubElement(clientes, "cliente3")
nome3 = etree.SubElement(cliente3, "nome")
nome3.text = "nome do terceiro cliente!"
idade3 = etree.SubElement(cliente3, "idade")
idade3.text = "23"
sexo3 = etree.SubElement(cliente3, "sexo")
sexo3.text = "feminino"
cpf3 = etree.SubElement(cliente3, "cpf")
cpf3.text = "123.456.789-02"

print(etree.tostring(clientes, pretty_print=True).decode("utf-8"))

print("total de cliente: ", len(clientes))

cliente_dois = clientes[1]
print("tag_cliente[1]", cliente_dois.tag)

for x in clientes:
    print(x.tag)

fatia1 = clientes[0:3]
for x in fatia1:
    print(x.tag)

print(clientes is clientes[1].getparent())