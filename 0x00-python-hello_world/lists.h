#ifndef LISTS_H
#define LISTS_H
#include <stdlib.h>

/**
  * struct listint - singly linked lst
  * @m: int
  * @nxt: points next code
  *
  * Description: node structure
  *
  */
typedef struct listint
{
	int m;
	struct listint *nxt;
}listint;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
