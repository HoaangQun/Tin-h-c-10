#Cho danh sách A gồm n phần tử có kiểu nguyên. Viết chương trình thực hiện các yêu cầu sau:
#   a. Liệt kê các số chẵn có trong danh sách A
#   b. Tính và đưa ra màn hình tổng các số là bội của 3 có trong danh sách
n = int(input("Nhap vao so phan tu cua A: "))
A = []
for i in range (n):
    A.append(i)
b = 0
for i in range (n):
    if A[i]%2==0:
        print(A[i])
    if A[i]%3==0:
        b+= A[i]
print(f"tong cac so la boi cua 3 = {b}")
