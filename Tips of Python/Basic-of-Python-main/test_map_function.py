print("# # # # # START # # # # #\n\n\n")



# map 함수 : map(함수, 함수를 적용할 자료형)
a = [10, 20, 30, 40, 50]

def plusone(n):
    return n + 1

b = list(map(plusone, a))

print(list(a))
print(list(b))



print("\n\n\n# # # # # END # # # # #")
