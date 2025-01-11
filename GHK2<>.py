#Viết chương trình nhập vào một xâu kí tự có thể có nhiều dấu cách giữa các từ. Sau đó chỉnh sửa xâu kí tự đó sao cho giữa các từ chỉ có một dấu cách. In xâu kết quả ra màn hình?
s = input("Nhap vao xau can chuan hoa: ")
s = s.strip()
s = ' '.join(s.split())
print(s)