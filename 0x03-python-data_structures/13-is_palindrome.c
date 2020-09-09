#include "lists.h"
/**
 * is_palindrome - check if the string is palindrome.
 * @head: is the list.
 * Return: 1 if is palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head, *aux2;
	int i, j, count;

	if (!*head || !head)
		return (1);
	for (i = 0; aux->next; i++)
		aux = aux->next;
	aux2 = *head;
	count = i;
	while (i > count / 2)
	{
		aux = *head;
		for (j = 0; j < i; j++)
			aux = aux->next;
		if (aux->n != aux2->n)
			return (0);
		i--;
		aux2 = aux2->next;
	}
	return (1);
}
