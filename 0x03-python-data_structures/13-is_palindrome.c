#include "lists.h"

/**
 * is_palindrome - chcks where a linked list is a palindrome.
 * @head: reference to start of string.
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;

	if (*head == NULL)
	{
		return (1);
	}

	while (current != NULL)
	{
		current = current->next;
	}

	if ((*head)->n == current->n)
	{
		return (1);
	}

	return (0);
}
