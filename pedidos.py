pedidos = []


def crear_pedido(cliente, items):
    """Crea un pedido. items es una lista de (producto, precio, cantidad)."""
    pedido = {"cliente": cliente, "items": items}
    pedidos.append(pedido)
    return pedido


def listar_pedidos():
    return pedidos


def calcular_total(items):
    """Suma precio * cantidad de cada item."""
    total = 0
    for producto, precio, cantidad in items:
        total += precio * cantidad
    return total
