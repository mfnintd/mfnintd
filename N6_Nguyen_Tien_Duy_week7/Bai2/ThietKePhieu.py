class SinhVien:
    def __init__(self, MaSinhVien="None", TenSinhVien="None", Lop="None", Khoa: int = None):
        self.__MaSinhVien = MaSinhVien
        self.__TenSinhVien = TenSinhVien
        self.__Lop = Lop
        self.__Khoa = Khoa

    def Nhap(self):
        self.__MaSinhVien = input("Nhap ma sinh vien: ")
        self.__TenSinhVien = input("Nhap ten sinh vien: ")
        self.__Lop = input("Nhap ten lop: ")
        self.__Khoa = int(input("Nhap khoa: "))

    def Xuat(self):
        print("{:<15}{:>10}     {}".format("Ma Sinh Vien: ", self.__MaSinhVien, "Ho va ten sinh vien: " + self.__TenSinhVien))
        print("{:<15}{:>10}     {}".format("Lop: ", self.__Lop, "Khoa: " + str(self.__Khoa)))


class Mon:
    def __init__(self, TenMon="None", SoTrinh: int = None, Diem: int = None):
        self.TenMon = TenMon
        self.SoTrinh = SoTrinh
        self.Diem = Diem

    def Nhap(self):
        self.TenMon = input("Nhap ten mon: ")
        self.SoTrinh = int(input("Nhap so trinh: "))
        self.Diem = int(input("Nhap diem: "))
        return Mon(self.TenMon, self.SoTrinh, self.Diem)

    def Xuat(self):
        print("{:<30}{:<30}{:<30}".format(self.TenMon, self.SoTrinh, self.Diem))


class PhieuBaoDiem:
    __SV = SinhVien()
    __SoLuongMon: int = None
    __DanhSachMon = list()

    def Nhap(self):
        self.__SV.Nhap()
        self.__SoLuongMon = int(input("Nhap so luong mon: "))
        for i in range(1, self.__SoLuongMon + 1):
            print("Nhap thong tin mon {}:".format(i))
            ThongTinMon = Mon()
            ThongTinMon.Nhap()
            self.__DanhSachMon.append(ThongTinMon)

    def __DiemTrungBinh(self):
        return sum([x.SoTrinh * x.Diem for x in self.__DanhSachMon]) / sum([x.SoTrinh for x in self.__DanhSachMon])

    def Xuat(self):
        print("{:^60}".format("PHIEU BAO DIEM"))
        self.__SV.Xuat()
        print("{:<30}{:<30}{:<30}".format("Bang diem:", "So trinh", "Diem"))
        for iMon in self.__DanhSachMon:
            iMon.Xuat()
        print("Diem trung binh: {:.5f}".format(self.__DiemTrungBinh()))
