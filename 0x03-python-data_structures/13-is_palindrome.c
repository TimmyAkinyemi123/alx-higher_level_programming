#include "lists.h"

lisint_t *reverse_list(listint_t **head);
int is_palindrome(lisint_t **head);

/**
 * reverse_list - reverses a linked list
 * @head: current head pointer
 * Return: pointer to head of reversed list
 */
listint_t *reverse_list(lisint_t **head)
{
	lisint_t *current = *head;
	lisint_t *previous = NULL;
	listint_t *temp;

	while (temp != NULL)
	{
		temp = current->next;
		current->next = previous;
		previous = current;
		current = temp;
	}
	*head = previous;
	return (*head);
}
