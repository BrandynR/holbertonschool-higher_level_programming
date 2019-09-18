#include "lists.h"
/**
 * palin_link_check - checks if a linked list is a palindrome
 * @copy: copy of the head
 * @head: head of the linked list
 * Return: 1 if linked list, 0 if not
 */
int palindrome_link_check(listint_t **copy, listint_t *head)
{
	if (head == NULL)
		return (1);

	if (palin_link_check(copy, head->next) == 1 && (*copy)->n == head->n)
	{
		*copy = (*copy)->next;
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - returns 1 if linked list is a palindrome, 0 if not
 * @head: head of the linked list
 * Return: 1 if a linked list palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int palindrome;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	palindrome = palin_link_check(head, *head);
	return (palindrome);
}
