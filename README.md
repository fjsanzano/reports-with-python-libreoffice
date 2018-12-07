# reports-with-python-libreoffice
Repositorio de ejemplos de reportes utilizando Python, Py3o.template y LibreOffice

Primero creamos el archivo “hola_mundo.py” con el contenido siguiente:

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

Después creamos la plantilla en LibreOffice con el nombre “hola_mundo_template.odt”, dentro del documento insertamos un campo de usuario (Ctrl+F2) en la pestaña “Variables” con el nombre py3o.document.hola como se muestra en la imagen siguiente.

Después de realizar estos pasos guardar todo y ejecutar “hola_mundo.py” para generar el informe.

