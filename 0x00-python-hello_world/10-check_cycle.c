#include "lists.h"
/**
 * check_cycle - checks whether th list has a cycle
 * @list: list of type listint_t
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;

	if (list == NULL)
	{
		return (0);
	}
	slow = list;
	fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}
