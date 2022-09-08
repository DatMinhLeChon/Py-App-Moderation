import h_FCFS as fcfs # lien ket toi file thu vien h_FCFS.py, moi nguoi co the copy phan duoi dong nay bo qua file kia cho de

temp = input("so luong cong viec")

list_work = fcfs.FCFS()

list_work._init_List(temp);

list_work.calculate();

list_work.show();



    
