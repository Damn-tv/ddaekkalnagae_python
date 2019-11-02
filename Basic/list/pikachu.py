list_1 = []


def enqueue(num, p, queue):
    if(p < 5):
        queue.append(num)
        p = (p + 1)
    else:
        print('overflow')
    return(num, p, queue)

def dequeue():
    if(len(queue) != 0):
        del queue[0]

    else:
        print('underflow')

queue = []

p = 0

while(True):
    input_string = input()
    if(input_string == 'in'):
        num = int(input())
        num, p, queue = enqueue(num, p, queue)
    elif(input_string == 'out'):
        dequeue()


