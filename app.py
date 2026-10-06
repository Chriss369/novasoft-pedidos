from pedidos import crear_pedido, listar_pedidos, calcular_total
from clientes import registrar_cliente, listar_clientes


def main():
    print("=== NovaSoft - Gestión de Pedidos ===")

    registrar_cliente("Ana Pérez")
    registrar_cliente("Luis Mora")

    crear_pedido("Ana Pérez", [("Teclado", 25.0, 2), ("Mouse", 10.0, 1)])
    crear_pedido("Luis Mora", [("Monitor", 120.0, 1)])

    print("\nClientes:")
    for cliente in listar_clientes():
        print(f"- {cliente}")

    print("\nPedidos:")
    for pedido in listar_pedidos():
        print(f"- {pedido['cliente']}: total ${calcular_total(pedido['items']):.2f}")


if __name__ == "__main__":
    main()
