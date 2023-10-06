

from datetime import datetime

from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSV

sv1=SinhVienChinhQuy(1957690,"Tran Van A",datetime.strftime("23/6/1999","%d/%m/%Y"),80)
sv2=SinhVienChinhQuy(1957691,"Nguyen Van C",datetime.strftime("5/12/1999","%d/%m/%Y"),90)
sv3=SinhVienChinhQuy(1957692,"Thai Thi Thu",datetime.strftime("15/8/1998","%d/%m/%Y"),60)
sv4=SinhVienChinhQuy(1957693,"Tran Thanh Tam",datetime.strftime("27/8/2000","%d/%m/%Y"),70)
sv5=SinhVienPhiCQ(1957694,"Nguyen Thanh Tra",datetime.strftime("17/5/2000","%d/%m/%Y"),"Cao dang",2)
sv6=SinhVienPhiCQ(1957695,"Nguyen Thanh Nam",datetime.strftime("7/12/1999","%d/%m/%Y"),"Cao dang",2)
sv7=SinhVienPhiCQ(1957696,"Nguyen Thanh Thanh",datetime.strftime("29/10/1999","%d/%m/%Y"),"Trung cap",2.5)
sv8=SinhVienPhiCQ(1957697,"Vo Hoai Nam",datetime.strftime("4/1/2000","%d/%m/%Y"),"Trung cap",2.5)

dssv=DanhSachSV()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)
dssv.xuat()

vt=dssv.timSVTheoMs(1957690)
print(f"Sinh vien o vi tri thu {vt+1} trong ds")
kq=dssv.timSVTheoLoai("chinhquy")
print("Danh sach sinh vien chinh quy:")
kq.xuat()
