print("# # # # # START # # # # #\n\n\n")



import os

# 파일부분과 폴더부분을 서로 잘라준다.
a = 'c:\temp\test\python\hello.exe'
b = os.path.split(a)
print(a)
print(b)



print("\n\n\n# # # # # END # # # # #")