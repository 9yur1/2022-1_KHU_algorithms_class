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

#랜덤리스트 생성 확인
n = 40000
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


#insertion_sort 시간확인
insertion_sort_time = time.time() - start
print("insertion_sort_time : ", insertion_sort_time)
