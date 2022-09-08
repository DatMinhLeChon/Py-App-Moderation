import string
# variable and class

def cal_time(val_a, val_b):
    if int(val_b) - int(val_b) > 0:
        return 0
    else:
        return int(val_b) - int(val_a)

class work:
    ## khoi tao
    def _init_(self, val_a, val_b, val_c):
        self.name_work = val_a;
        self.time_work = val_b;
        self.time_end = val_c;

    def get_name_work(self):
        return self.name_work
    
    def get_time_work(self):
        return self.time_work

    def get_time_end(self):
        return self.time_end

class FCFS:
    ## khoi tao
    def _init_List(self, val_a):
        self.volume = val_a;
        self.list_work = [];
        for i in range(0, int(self.volume)):
            self.list_work.append(work());
            print("Cong viec thu");
            temp1 = input("nhap ten cong viec" );
            temp2 = input("nhap thoi gian cong viec" );
            temp3 = input("nhap thoi gian toi han cua cong viec" );
            self.list_work[i]._init_(temp1, temp2, temp3);
            
    def calculate(self):
        self.total_time =0;
        self.total_late_time =0;
        self.process = [];
        for i in range(0, int(self.volume)):
            self.total_time = 2*int(self.total_time) + int(self.list_work[i].time_work);
            self.total_late_time = int(self.total_late_time) + int(cal_time(self.list_work[i].time_end, self.total_time));
            self.process.append(self.list_work[i].name_work);
    
    def show(self):
        print(self.total_time);
        print(self.total_late_time);
        print(self.process);
        









    
     
