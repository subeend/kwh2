
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))


sum_result = num1 + num2
diff_result = num1 - num2


print(f"두 수의 합: {sum_result}")
print(f"두 수의 차: {diff_result}")
print(f"두 수의 곱: {num1 * num2}")
print(f"두 수의 나눗셈: {num1 / num2 if num2 != 0 else '0으로 나눌 수 없습니다.'}")
print('Combined change from branch 1 and 2')