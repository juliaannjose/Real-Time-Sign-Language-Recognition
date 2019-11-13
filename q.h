#include <unistd.h>
#include <stdlib.h>
#include "tcb.h"

typedef struct Queue {
struct TCB_t *header; 
} Queue;

void InitQueue(struct Queue*);
void AddQueue(struct Queue*, struct TCB_t*);
void RotateQ(struct Queue*);

struct TCB_t* DelQueue(struct Queue*); 
struct TCB_t* NewItem();

struct TCB_t* NewItem() 
{
struct TCB_t *item = (struct TCB_t*) malloc(sizeof(struct TCB_t));
if (!item) 
{
item->prev = NULL; 
item->next = NULL; 
}
return item;
}

void InitQueue(struct Queue *head)
{
head->header = NULL;
}

void AddQueue(struct Queue *head, struct TCB_t *item)
 {
if (head->header != NULL)
{
if (head->header->next != NULL)
{
item->prev = head->header->prev; 
item->next = head->header;
head->header->prev->next = item;
head->header->prev = item; 
} 
else 
{
head->header->next = item;
head->header->prev = item; 
item->next = head->header; 
item->prev = head->header;
}
} 
else 
{
head->header = item; 
item->prev = NULL; 
item->next = NULL;
}
}

void RotateQ(struct Queue *head) 
{
AddQueue(head, DelQueue(head));
}

struct TCB_t* DelQueue(struct Queue *head) 
{
struct TCB_t *item = head->header;
if (head->header != NULL) 
{
if (head->header->next != NULL) 
{
head->header->prev->next = head->header->next;
head->header->next->prev = head->header->prev;
head->header = head->header->next;
} 
else 
{
head->header = NULL;
}
}
return item;
}


