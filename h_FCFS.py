# File thu vien h_FCFS
# Khai bao thu vien chuan
import string

# Function, variable and class
# Ham tra ve gia tri thoi gian tre han cua cong viec
def cal_time(val_a, val_b):
    if int(val_b) - int(val_b) > 0:
        return 0
    else:
        return int(val_b) - int(val_a)

# Dinh nghia mot cong viec - define a work
class work:
    # Khoi tao gia tri
    def _init_(self, val_a, val_b, val_c):
        self.name_work = val_a; # Ten cong viec
        self.time_work = val_b; # Thoi gian thuc hien cong viec
        self.time_end = val_c; # Thoi gian toi han

    def get_name_work(self):
        return self.name_work # Tra ve gia tri
    
    def get_time_work(self):
        return self.time_work # Tra ve gia tri

    def get_time_end(self):
        return self.time_end # Tra ve gia tri

# Dinh nghia mot danh sach cac cong viec - define a list of work
class FCFS:
    # Khoi tao gia tri
    def _init_List(self, val_a):
        self.volume = val_a;
        self.list_work = []; # Tao danh sach rong
        for i in range(0, int(self.volume)):
            self.list_work.append(work()); # Them mot phan tu kieu work vao danh sach
            print("Cong viec thu");
            temp1 = input("nhap ten cong viec" );
            temp2 = input("nhap thoi gian cong viec" );
            temp3 = input("nhap thoi gian toi han cua cong viec" );
            self.list_work[i]._init_(temp1, temp2, temp3); # Khoi tao gia tri cho phan tu vua them vao danh sach
    
    # Tinh cac chi so va thu tu cong viec theo FCFS
    def calculate(self):
        self.total_time =0;
        self.total_late_time =0;
        self.process = [];
        for i in range(0, int(self.volume)):
            # Tinh Tong thoi gian cong viec tai thoi diem cong viec thu i duoc thuc hien
            self.total_time = 2*int(self.total_time) + int(self.list_work[i].time_work); 
            # Tinh tong thoi gian du thua cho den thoi diem cong viec i
            self.total_late_time = int(self.total_late_time) + int(cal_time(self.list_work[i].time_end, self.total_time));
            # Them ten cong viec i vao thu tu thuc hien
            self.process.append(self.list_work[i].name_work);
    
    # Xuat ra command
    def show(self):
        print(self.total_time);
        print(self.total_late_time);
        print(self.process);
        
     
