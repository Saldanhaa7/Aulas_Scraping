from lxml import etree

elemento = etree.Element("teste")
elemento.text = "este é o texto da tag teste!"
print(etree.tostring(elemento))
print(elemento.tag)