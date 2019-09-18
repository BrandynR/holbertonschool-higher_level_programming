#include "lists.h"
/**
 * is_palindrome - finds palindrome in singly linked list
 * @head: pointer to first node
 * Return: retunr 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int count = 0, len = 0, iter = 0;
	int buffer[9000];

	if (!head || !*head || !temp->next)
		return (1);

	while (temp)
	{
		buffer[count] = temp->n;
		count++;
		temp = temp->next;
	}

	len = count - 1;
	while (iter <= len)
	{
		if (buffer[i] != buffer[len])
			return (0);
		i++;
		len--;
	}
	return (1);
}
