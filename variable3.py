# lista del clientes

clientes = ({'Nombre': 'John', 'Correo': 'john@correo.com'},
            {'Nombre': 'Anna', 'Correo': 'anna@correo.com'},
            {'Nombre': 'Bob', 'Correo': 'bob@correo.com'},
            )

print(clientes)
# quiero obtener el primer cliente
print(clientes[0])
# del segundo cliente, quiero obtener el nombre
print(clientes[1]['Nombre'])

clientes[1]['Nombre'] = 'Anna Modificada'
print(clientes[1]['Nombre'])
