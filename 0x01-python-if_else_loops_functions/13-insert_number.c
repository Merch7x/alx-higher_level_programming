#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: ref to start of list
 * @number: data to insert
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number);
{
	listint_t *new_node;
	listint_t *tmp;

	tmp = *head;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (tmp->next != NULL)
	{
		if ((runner->next)->n >= number)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
			return (new);
		}
		tmp = tmp->next;
	}

	new_node->next = NULL;
	tmp->next = new;
	return (new);
}


