class SinhVien:
    def __init__(self,ten_sinh_vien,ma_sinh_vien):
        self.student_name = ten_sinh_vien
        self.student_id = ma_sinh_vien
        return
    def sleep(self):
        print("Sinh vien {} dang ngu".format(self.student_name))
    def eat(self):
        print("Sinh vien {} co ma sinh vien {} dang an".format(self.student_name,self.student_id))

sinh_vien_a = SinhVien("Nguyen Van A","SV001")
print("Ten sinh vien la: ",sinh_vien_a.student_name)
sinh_vien_a.sleep()
sinh_vien_a.eat()
