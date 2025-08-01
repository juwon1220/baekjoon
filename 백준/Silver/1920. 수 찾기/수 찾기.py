N = int(input())
array = []

temp = input().split()

for i in range(N):
    array.append(int(temp[i]))
    #array.append(int(input()))
array.sort()

M = int(input())
data = []

temp2 = input().split()

for i in range(M):
    data.append(int(temp2[i]))

for i in range(M):
    search = data[i]

    low_index, high_index = 0, N-1
    is_find = False # 찾았는지 못 찾았는지 정보!!

    while low_index <= high_index:
        mid_index = (low_index + high_index)//2
        if search > array[mid_index]:
            #왼쪽을 버리자
            low_index = mid_index + 1
        elif search < array[mid_index]:
            high_index = mid_index - 1
        else:
            print(1)
            is_find = True
            break
    if is_find == False:
        print(0)