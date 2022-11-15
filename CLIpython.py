
from typing import List, Dict
from time import sleep
from modelProduto import Product

list_product: List[Product] = [
    Product("Apple", 1.99),
    Product("Orange", 2.99),
    Product("Banana", 3.99),
    Product("Grapes", 4.99),
    Product("Pineapple", 5.99),
    Product("Watermelon", 6.99),
    Product("Mango", 7.99),
    Product("Papaya", 8.99),
    Product("Strawberry", 9.99),
    Product("Blueberry", 10.99),
    Product("Raspberry", 11.99),
    Product("Blackberry", 12.99),
    Product("Peach", 13.99),
    Product("Pear", 14.99),
    Product("Cherry", 15.99),
    Product("Pomegranate", 16.99),
    Product("Pomelo", 17.99),
    Product("Lemon", 18.99),
    Product("Lime", 19.99),
    Product("Coconut", 20.99),
]

cart: List[Dict[Product, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('=========== Welcome to Endless Shop ==========')
    print('Select a option below: ')
    print('1 - Add Item')
    print('2 - Remove Item')
    print('3 - View Cart')
    print('4 - Create Item')
    print('5 - Edit Item')
    print('6 - Delete Item')
    print('9 - Exit')

    option: int = int(input())

    if option == 1:
        add_item()
    elif option == 2:
        cart_products()
    elif option == 3:
        buy_product()
    elif option == 4:
        create_item()
    elif option == 5:
        fechar_pedido()
    elif option == 6:
        fechar_pedido()
    elif option == 9:
        print('Come back later!')
        sleep(2)
        exit(0)
    else:
        print('Invalid option!')
        sleep(1)
        menu()

def format_float_str_coin(value: float) -> str:
    return f'R$ {value:,.2f}'

def create_item() -> None:
    print('Create new Item')
    print('===================')

    name: str = input('Enter the item name: ')
    price: float = float(input('Enter the item price: '))
    list_product.append(Product(name, price))

    print(f'The item {name} was successfully registered!')
    sleep(2)
    menu()

def cart_products() -> None:
    if len(list_product) > 0:
        print('===== All products ======')
        print('--------------------')
        for product in list_product:
            print(product)
            print('----------------')
            sleep(1)
    else:
        print('There are no registered products yet.')
    sleep(2)
    menu()

def buy_product() -> None:
    if len(list_product) > 0:
        
        print('--------------------------------------------------------------')
        print('================== Produtos Disponíveis ======================')
        for product in list_product:
            print(product)
            print('---------------------------------------------------------')
            sleep(1)
        print('Enter the product code you want to add to the cart: ')
        codigo: int = int(input())

        produto: Product = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(
                            f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(
                        f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código {codigo} não foi encontrado.')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender.')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0

        print('Produtos do Carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('------------------------')
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print('Ainda não existem produtos no carrinho.')
    sleep(2)
    menu()


def pega_produto_por_codigo(codigo: int) -> Product:
    p: Product = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
