#include "lists.h"
/**
 * check_cycle - checks if there are no loops in the list.
 * @list: linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *aux = list;

	if (list == NULL || list->next == NULL)
		return (0);
	while (list && aux)
	{
		list = list->next;
		aux = aux->next->next;
		if (aux == list)
			return (1);
	}
	return (0);
}
