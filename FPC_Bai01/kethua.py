class Person:
    def __init__(self,ten,dia_chi):
        self.ten = ten
        self.dia_chi = dia_chi
        return
class SinhVien(Person):
    def __init__(self,ten,dia_chi,lop):
        super(SinhVien,self).__init__(ten,dia_chi)
        self.lop = lop


sinh_vien_a = SinhVien("Nguyen Van A","Ha Noi","HTTT")

print("Sinh vien {} co dia chi {}".format(sinh_vien_a.ten,sinh_vien_a.dia_chi))
try:
    print(sinh_vien_a.gpa)
except Exception as loi:
    print("Chuong trinh co loi: ",loi)