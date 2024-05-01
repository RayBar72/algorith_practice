#!/usr/bin/env python3
from nodes import Node


# Métodos que necesito:
#       add inicio. Done
#       add final. Done
#       número de elementos. Done
#       borrar. Done
#       string que represente la lista. Done
#       localizar y la posición del elemento
class LinkedList:
    def __init__(self):
        self.head = None
        self.number = 0

    def add_inicial(self, data):
        nodo = Node(data)
        if not self.head:
            self.head = nodo
        else:
            nodo.next = self.head
            self.head = nodo
        self.number += 1

    def add_final(self, data):
        nodo = Node(data)
        if not self.head:
            self.head = nodo
        else:
            move = self.head
            while move.next:
                move = move.next
            move.next = nodo
        self.number += 1

    def borra_nodo(self, value):
        if not self.head:
            print('No puede borrarse el valor. La lista está vacía')
        intermedio = None
        if self.head.data == value:
            intermedio = self.head.next
            del self.head
            self.head = intermedio
            self.number -= 1
            return None
        avanza = self.head.next
        intermedio = self.head
        while avanza:
            if avanza.data == value:
                intermedio.next = avanza.next
                del avanza
                self.number -= 1
                return None
            else:
                avanza = avanza.next
                intermedio = intermedio.next
        print('Valor no encontrado')

    def __str__(self):
        retorno = ''
        recorre = self.head
        if not self.head:
            return retorno
        while recorre:
            retorno = retorno + '[{}]'.format(recorre.data)
            if recorre.next:
                retorno = retorno + ' --> '
            else:
                retorno = retorno + '\n'
            recorre = recorre.next
        return retorno

    def localiza(self, value):
        avanza = self.head
        counter = 0
        while avanza:
            counter += 1
            if avanza.data == value:
                return counter
            avanza = avanza.next
        print('Elemento no localizado')
