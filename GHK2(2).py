#Cho trước xâu kí tự S bất kì. Viết đoạn chương trình có chức năng sau:
#   a) Đếm số các kí tự là chữ số trong S.
#   b) Đếm số các kí tự là chữ cái tiếng Anh trong S.
S = input("Nhap mot xau bat ki: ")
#a)
dem = 0
for nt in S:
    if '0' <= nt <= '9':
        dem += 1
print(f"co {dem} chu so")
#b)
dem = 0
for tr in S:
    if 'a' <= tr <= 'z' or 'A' <= tr <= 'Z':
        dem += 1
print(f"co {dem} chu cai")  