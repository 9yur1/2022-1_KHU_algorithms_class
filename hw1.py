import random
import time

#시작 시간 저장
start = time.time()

#랜덤리스트 생성 함수 정의
def random_List(size):
    result = []

    for i in range(size):
        result.append(random.randint(0,1000))

    return result

#랜덤리스트 생성 확인(n=5000)
n = 5000
result = random_List(n)

#insertion sort 함수 정의
def insertion_sort(result):
    for i in range(1,len(result)):
        for j in range(i, 0, -1):
            if result[j]<result[j-1]:
                result[j], result[j-1] = result[j-1], result[j]
                i = -1
            else:
                break
    return result

print(insertion_sort(result))

#insertion_sort 시간확인
insertion_sort_time = time.time() - start
print("insertion_sort_time : ", insertion_sort_time)


#quick sort 함수 정의
def quick_sort(result):
    if len(result) <= 1:
        return result
    
    pivot = result[0]
    tail = result[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(result))

#quick_sort 시간확인
quick_sort_time = time.time() - insertion_sort_time
print("quick_sort_time : ", quick_sort_time)

#랜덤리스트 생성 확인(n=10000)
n = 10000
result = random_List(n)

#insertion sort 함수 정의
def insertion_sort(result):
    for i in range(1,len(result)):
        for j in range(i, 0, -1):
            if result[j]<result[j-1]:
                result[j], result[j-1] = result[j-1], result[j]
                i = -1
            else:
                break
    return result

print(insertion_sort(result))

#quick sort 함수 정의
def quick_sort(result):
    if len(result) <= 1:
        return result
    
    pivot = result[0]
    tail = result[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(result))
