"""문제 3 - 두 번째로 큰 수 찾기

정수 N을 입력받고, 이어서 N개의 정수를 입력받는다.

두 번째로 큰 수를 출력하라.

입력 예시
5
7
2
9
4
5
출력
7"""

num = int(input())
max_num = int(input())
sec_num = 0

for _ in range(num-1):
    new_num = int(input())
    if new_num > max_num:
        sec_num = max_num
        max_num = new_num
    elif new_num > sec_num:
        sec_num = new_num
    
print(sec_num)
