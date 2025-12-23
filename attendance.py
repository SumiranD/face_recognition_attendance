from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Attendance")
        
        #-------variables 
        self.var_attend_id=StringVar()
        self.var_attend_name=StringVar() 
        self.var_attend_dep=StringVar() 
        self.var_attend_time=StringVar() 
        self.var_attend_date=StringVar() 
        self.var_attend_attendance=StringVar()  
        
        
         #top bar
        img=Image.open(r"college-images\label2.jpg")
        img=img.resize((1370,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1370,height=100) 
        
        #background image
        img3=Image.open(r"college-images\background2.jpg")
        img3=img3.resize((1370,568),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1370,height=568)
        
         #title
        title_lbl=Label(bg_img,text="Attendance Record",font=("Arial",30,"bold"),bg="aliceblue",fg="black")
        title_lbl.place(x=0,y=0,width=1370,height=50)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1368,height=530)
        
        ##-----left frame
        
        left_frame=LabelFrame(main_frame,bd=2,text="Student Attendance Details",font=("arial",12,"bold"),relief=RIDGE,bg="aliceblue",fg="black")
        left_frame.place(x=50,y=10,width=605,height=475)
        
        img_left=Image.open(r"college-images\student.jpg")
        img_left=img_left.resize((75,75),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=20,y=5,width=75,height=75)
        
        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=0,y=135,width=600,height=318)
        
        #-- labels and entry
        
         #-attendance ID 
        attendanceID_label=Label(left_inside_frame,text="AttendanceID:",bg="white", font="comicsansns 11 bold")
        attendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_attend_id,font="comicsansns 11 bold")
        attendanceID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        
        # Name
        nameLabel=Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_attend_name, width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel=Label(left_inside_frame, text="Department:", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_attend_dep, width=22, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timeLabel=Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_attend_time, width=22, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        


        # Date
        dateLabel=Label(left_inside_frame, text="Date:", bg="white", font="comicsansns 11 bold")
        dateLabel.grid(row=2, column=2)

        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_attend_date, width=22, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        # attendance
        attendanceLabel=Label(left_inside_frame, text="Attendance Status:", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox(left_inside_frame, width=20,textvariable=self.var_attend_attendance, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

         #buttons frame
        
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=180,width=418,height=32)
        
        save_btn=Button(btn_frame,text="Impost csv",command=self.importCsv,width=16,font=("arial",10,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=16,font=("arial",10,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=1)
        
        #delete_btn=Button(btn_frame,text="Update",width=16,font=("arial",10,"bold"),bg="lightblue",fg="black")
        #delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("arial",10,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=2)
        
        
         ##-----right frame
        
        right_frame=LabelFrame(main_frame,bd=2,text="Student Details",font=("arial",12,"bold"),relief=RIDGE,bg="aliceblue",fg="black")
        right_frame.place(x=750,y=10,width=560,height=475)
        
        img_right=Image.open(r"college-images\student.jpg")
        img_right=img_right.resize((75,75),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=20,y=5,width=75,height=75)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=545,height=445)
        
        #---------------- scroll bar
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("name","id","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("id",text="Attendance ID")
        #self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("id",width=100)
        #self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        #----------fetch data     
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
                       
    #--------export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)  
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                                  
        
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_name.set(rows[1])
        self.var_attend_dep.set(rows[2])
        self.var_attend_time.set(rows[3])
        self.var_attend_date.set(rows[4])
        self.var_attend_attendance.set(rows[5])
        
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")
            
        
          
        
        
if __name__ == "__main__":
   root=Tk()
   obj=Attendance(root)
   root.mainloop() 