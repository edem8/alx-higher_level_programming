#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: the beginning of the list
 * @number: number to insert
 * Return: return NULL or pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);


	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n >= number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			current = current->next;
		}
		if (current->next == NULL && current->n <= number)
			current->next = new;
	}
	return (new);
}
