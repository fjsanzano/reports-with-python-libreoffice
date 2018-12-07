from py3o.template import Template

t = Template("reclamacion_template.odt", "reclamacion_output.odt")

class Item(object):
    pass

items = list()

#
item1 = Item()
item1.cliente = 'Empresa de Prueba'
item1.especialista = 'Ing. Fidel Jimenez Sanzano'
subitem1 = Item()
subitem1_list = list()
subitem1.nro = 320018001
subitem1.servicio = 'Consultoria informatica'
subitem1.fecha = '2018-11-25'
subitem1_list.append(subitem1)

subitem2 = Item()
subitem2.nro = 320018012
subitem2.servicio = 'Instalacion de servidores'
subitem2.fecha = '2018-11-20'
subitem1_list.append(subitem2)
item1.subitems=subitem1_list

items.append(item1)
#
item2 = Item()
item2.cliente = '2da Empresa de Prueba'
item2.especialista = 'Ing. Yoannis Dominguez'
sub1item2 = Item()
subitem2_list = list()
sub1item2.nro = 320018010
sub1item2.servicio = 'Despliegue Agenda Express 3.0'
sub1item2.fecha = '2018-10-15'
subitem2_list.append(sub1item2)

sub2item2 = Item()
sub2item2.nro = 320018020
sub2item2.servicio = 'Desarrollo del sistema X'
sub2item2.fecha = '2018-10-21'
subitem2_list.append(sub2item2)
item2.subitems=subitem2_list
items.append(item2)

document = Item()
document.total = '9999999999999.999'

data = dict(objects=items, document=document)
t.render(data)
