class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__ (self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        if self.front == None:
            curr = Node(data)
            self.front = curr
            self.rear = curr
            # rear = Node(data)
        else:
            curr = Node(data)
            self.rear.next = curr
            self.rear = curr
            #curr.next = self.rear
            #self.rear = curr

    def dequeue(self):
        if self.front == None:
            return None
        else:
            curr = self.front
            self.front = self.front.next
            return curr.data

    def is_empty(self):
        return self.front == None
    
    
N, K = map(int, input().split())
q = Queue()
result = "<"
for i in range(1,N+1):
    q.enqueue(i)

while not q.is_empty():
    # K가 3이라면 dequeue enqueue 두 번, dequeue해서 result에 추가
    for _ in range(K-1):
        q.enqueue(q.dequeue())
    
    result += str(q.dequeue())
    result += ", "

result = result[:-2] + ">"
#result -= ", "
#result += ">"
print(result)