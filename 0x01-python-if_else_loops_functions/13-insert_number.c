#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the initial linked list pointer
 * @number: number to insert
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;
	int x, y;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number, tmp = *head;
	if (!(*head))
		return (*head = new, new->next = NULL, new);
	for (x = 0; tmp; x++)
	{
		if (number > tmp->n)
		{
			if (!tmp->next)
				return (tmp->next = new, new->next = NULL, new);
			tmp = tmp->next;
			continue;
		}
		else
		{
			new->next = tmp;
			if (tmp == *head)
			{
				*head = new;
				break;
			}
			tmp = *head;
			for (y = 0; y < x; y++)
			{
				if (y == (x - 1))
				{
					tmp->next = new;
					break;
				}
				tmp = tmp->next;
			}
			break;
		}
	}
	return (new);
}
