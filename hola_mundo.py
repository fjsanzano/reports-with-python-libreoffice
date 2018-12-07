# importar la libreria
from py3o.template import Template

# creando la platilla para generar el informe
t = Template("hola_mundo_template.odt", "hola_mundo_output.odt")

# clase item auxiliar necesaria para pasar los parametros a la libreria py3o
class Item(object):
    pass

# creando el objeto
document = Item()

# seteando los valores
document.hola = 'Hola mundo'

# conviertiendo los valores a dict
data = dict(document=document)

# generando el informe con los valores anteriores
t.render(data)
