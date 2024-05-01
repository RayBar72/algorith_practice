#!/usr/bin/env python3
from lists import LinkedList


def main():
    lista = [1, 2, 3, 4, 5]

    llist = LinkedList()
    for n in lista:
        llist.add_final(n)
        print('añadiendo {}'.format(n))
    print(llist)

    llist.borra_nodo(3)

    print(llist)

    llist.borra_nodo(5)

    print(llist)

    print(llist.number)

    print(llist.localiza(2))

    print(llist.localiza(5))

if __name__ == '__main__':
    main()
