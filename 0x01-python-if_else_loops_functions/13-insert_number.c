#include"lists.h"
/**
 * insert_node - insert node
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
		*head = new;
	else
	{
		while ((current->next)->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
