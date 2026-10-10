clientes = []


def registrar_cliente(nombre):
    """Registra un cliente nuevo si no existe."""
    if nombre not in clientes:
        clientes.append(nombre)
    return nombre


def listar_clientes():
    return clientes
