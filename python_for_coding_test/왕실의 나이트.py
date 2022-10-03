input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

steps = [(-2,-1), (-1, -2), (1, -2), (2, -1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps:
    next_row = row+step[0]
    next_column = column+step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result+=1

print(result)

# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord("a")) + 1
# # ord(문자) 문자 > 정수 ("a" > 97)
# # chr(정수) 정수 > 문자 (97 > "a")

# steps = [(-2,-1), (-1, -2), (1, -2), (2, -1), (2,1), (1,2), (-1,2), (-2,1)]

# result = 0
# for step in steps:
#     next_row = row+step[0]
#     next_column = column + step[1]
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result+=1

# print(result)