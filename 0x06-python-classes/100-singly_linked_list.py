#!/usr/bin/python3
"""
A class node that defines a node of a singly linked list
    private instance attribute: data
    Getter and setter methods for data

    private instance attribute: next_node
    Getter and setter methods for next_node

A class singlyLunkedList that defines a singly linkedlist
    private instance attribute: head
"""


class Node:
    """ Implementation of a node class """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    """ Implementation of data getter and setter """
    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    """ Implementation of next_node getter and setter """
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Implementation of Singly linked list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return ("\n".join(result))
