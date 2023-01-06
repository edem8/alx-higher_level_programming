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
            raise TypeError("data must be ana integer")
        else:
            self.__data = value

    """ Implementation of next_node getter and setter """
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, None) or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Implementation of Singly linked list """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or self.head.data > value:
            new_node.next_node = self.__head
            self.head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = currrent.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = []
        while current:
            result.append(current.data)
            current = current.next_node
        return result.join('\n')
