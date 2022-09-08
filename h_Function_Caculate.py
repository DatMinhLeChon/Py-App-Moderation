import h_FCFS as fcfs

temp = input("so luong cong viec")

list_work = fcfs.FCFS()

list_work._init_List(temp);

list_work.calculate();

list_work.show();



    