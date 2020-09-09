#include "lists.h"
/**
 * is_palindrome - check if the string is palindrome.
 * @head: is the list.
 * Return: 1 if is palindrome else 0.
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int *s;
	int i, j = 0;

	if (!*head || !head)
		return (1);
	for (i = 0; aux->next; i++)
		aux = aux->next;
	s = malloc(sizeof(int) * i);
	if (!s)
		return (0);
	while (*head)
	{
		s[j] = (*head)->n;
		head = &(*head)->next;
		j++;
	}
	for (j = 0; j < i; j++, i--)
		if (s[j] != s[i])
			return (0);
	return (1);
}
