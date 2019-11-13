#include "q.h"

struct Queue *runQ;

void start_thread(void (*function)(void));
void run();
void yield();

void start_thread(void (*function)(void)) 
{
TCB_t *temp = NewItem();
void *stack = (void *) malloc(8192);
init_TCB(temp, function, stack, 8192);
AddQueue(runQ, temp);
}

void run() 
{
ucontext_t from, to;
ucontext_t parent;
from = parent;
getcontext(&parent);
to = (runQ->header->context);
swapcontext(&parent, &(runQ->header->context));
}

void yield() 
{
ucontext_t from, to;
getcontext(&from);
runQ->header->context = from;
RotateQ(runQ);
to = runQ->header->context;
swapcontext(&from, &to);
}
