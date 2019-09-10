#include "lists.h"
/**
 * check_cycle - checks to see if a cycle exists in a linked list
 * @list: start of linked list
 * Return: 1 if cycle, 0 if no cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cycle, *cycle2;

	cycle = list;
	cycle2 = list;

	while (cycle && cycle2 && cycle2->next)
	{
		cycle = cycle->next;
		cycle2 = cycle2->next->next;
		if (cycle == cycle2)
			return (1);
	}
	return (0);
}
