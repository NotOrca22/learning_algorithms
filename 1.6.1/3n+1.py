# numbers = [1,1000]
# lengths = []
# for i in range(int(numbers[0]), int(numbers[1])):
#     length = 1
#     while i != 1:
#         if i % 2 == 1:
#             i *= 3
#             i += 1
#         else:
#             i = i / 2
#         length += 1
#     lengths.append(length)
#
# print(max(lengths))
arr = [1,2,3,4,5]
arr.insert(0,6)
print(arr)
for i in arr:
    print(i)
    if i == 2:
        # arr.insert(0,6)
        print(arr)