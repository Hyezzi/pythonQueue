def push(queue, data):
    queue.append(data);
    return queue;

def size(queue):
    if queue == None:
        return 0;
    else:
        return(len(queue));

def empty(queue):
    if len(queue) == 0:
        return 1;
    else:
        return 0;

def pop4queue(queue):
    if empty(queue):
        print(-1);
        return queue;
    else:
        print(queue[0]);
        queue = queue[1:];
        return queue;
        
def front(queue):
    if empty(queue):
        print(-1);
    else:
        print(queue[0]);

def back(queue):
    if empty(queue):
        print(-1);
    else:
        print(queue[len(queue)-1]);



N = int(input());
queue = [];

for n in range (N):
    order = input().split(" ");

    if len(order) == 2:
        push(queue, order[1]);
    else:
        if order[0] == "front":
            front(queue);
        elif order[0] == "back":
            back(queue);
        elif order[0] == "size":
            print(size(queue));
        elif order[0] == "empty":
            print(empty(queue));
        elif order[0] == "pop":
            queue = pop4queue(queue);
            

        
