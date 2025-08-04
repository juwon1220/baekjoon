class Casually_Stack:
    def __init__(self):
        self.s = []
    def push(self, data):
        self.s.append(data)
    def pop(self):
        return self.s.pop() # return self.s[-1], 근데 삭제를 또 해줘야 될 듯
    def is_empty(self):
        return len(self.s) == 0
    
    def peek(self):
        if self.is_empty() == 1:
            return "비어 있습니다"
        else:
            return self.s[-1]
        # 비어 있으면 "비어 있습니다"
        # 비어 있지 않으면 가장 윗 값
    def __str__(self):
        return str(self.s)
    
T = int(input())
b_list = []
for i in range(T):
    b_list.append(input())
for test_case in b_list:
    #test_case = "()()()()(()()())()"
    b_stack = Casually_Stack()
    
    is_valid = True
    
    for b in test_case:
        if b == "(":
            b_stack.push(b)
        else :
            if b_stack.is_empty(): #")"가 들어왔는데 비어있으면(")"가 없으면)
                is_valid = False
                break
                
            else:
                if b_stack.pop() == "(":
                    continue
                else :
                    is_valid = False
                    break
    if not b_stack.is_empty():
        is_valid = False
    
    print("YES" if is_valid else "NO")