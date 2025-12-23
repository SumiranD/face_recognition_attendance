from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Face Detection")
        
        #-----------variable declaration-----------
        
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_ID=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()

       

        
        
        
        
        
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
        title_lbl=Label(bg_img,text="Student Details",font=("Arial",30,"bold"),bg="aliceblue",fg="black")
        title_lbl.place(x=0,y=0,width=1370,height=50)
        
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1368,height=530)
        
        ##-----left frame
        
        left_frame=LabelFrame(main_frame,bd=2,text="Student Details",font=("arial",12,"bold"),relief=RIDGE,bg="aliceblue",fg="black")
        left_frame.place(x=50,y=10,width=560,height=475)
        
        img_left=Image.open(r"college-images\student.jpg")
        img_left=img_left.resize((75,75),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=20,y=5,width=75,height=75)
        
        #current course information
        current_course_frame=LabelFrame(left_frame,bd=2,text="Current Info:",font=("arial",10,"bold"),bg="aliceblue",fg="black")
        current_course_frame.place(x=10,y=80,width=540,height=150)
        
        
                                    #department
        dep_label=Label(current_course_frame,text="Departent",font=("arial",10),bg="aliceblue",fg="black")
        dep_label.grid(row=0,column=0,padx=10)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("arial",10,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer","Civil","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=8)
        
                                     #year 
        year_label=Label(current_course_frame,text="Year",font=("arial",10,),bg="aliceblue",fg="black")
        year_label.grid(row=1,column=0,padx=10)                            
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("arial",10,"bold"),state="readonly")
        year_combo["values"]=("Select Year","First","Second","Third","Forth")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=8,sticky=W)
        
        
                                       #sem
        sem_label=Label(current_course_frame,text="Semester",font=("arial",10),bg="aliceblue",fg="black")
        sem_label.grid(row=2,column=0,padx=10)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem,font=("arial",10,"bold"),state="readonly")
        sem_combo["values"]=("Select Semester","Semester:1","Semester:2","Semester:3","Semester:4","Semester:5","Semester:6","Semester:7","Semester:8")
        sem_combo.current(0)
        sem_combo.grid(row=2,column=1,padx=2,pady=8,sticky=W)
        
        #student information
        Student_info_frame=LabelFrame(left_frame,bd=2,text="Student Info:",font=("arial",10,"bold"),bg="aliceblue",fg="black")
        Student_info_frame.place(x=10,y=250,width=540,height=200)
        
        #-studentID
        studentID_label=Label(Student_info_frame,text="RollNo",font=("arial",10),bg="aliceblue",fg="black")
        studentID_label.grid(row=0,column=0,padx=5)
        
        studentID_entry=ttk.Entry(Student_info_frame,textvariable=self.var_ID,font=("arial",10))
        studentID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #-Student name
        
        student_name_label=Label(Student_info_frame,text="Student Name",font=("arial",10),bg="aliceblue",fg="black")
        student_name_label.grid(row=1,column=0,padx=5)
        
        student_name_entry=ttk.Entry(Student_info_frame,textvariable=self.var_name,font=("arial",10))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #=student_phone
        student_phone_label=Label(Student_info_frame,text="Phone",font=("arial",10),bg="aliceblue",fg="black")
        student_phone_label.grid(row=0,column=2,padx=5)
        
        student_phone_entry=ttk.Entry(Student_info_frame,textvariable=self.var_phone,font=("arial",10))
        student_phone_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        
        #-student email
        
        student_email_label=Label(Student_info_frame,text="Student Email",font=("arial",10),bg="aliceblue",fg="black")
        student_email_label.grid(row=1,column=2,padx=5)
        
        student_email_entry=ttk.Entry(Student_info_frame,textvariable=self.var_email,font=("arial",10))
        student_email_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Student_info_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=3,column=0)
        
        
        radiobtn2=ttk.Radiobutton(Student_info_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=3,column=1)
        
        #buttons frame
        
        btn_frame=Frame(Student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=100,width=550,height=32)
        
        save_btn=Button(btn_frame,text="Save",width=16,command=self.add_data,font=("arial",10,"bold"),bg="lightblue",fg="black")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",width=16,command=self.update_function,font=("arial",10,"bold"),bg="lightblue",fg="black")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("arial",10,"bold"),bg="lightblue",fg="black")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("arial",10,"bold"),bg="lightblue",fg="black")
        reset_btn.grid(row=0,column=3)
        
        
        btn_frame2=Frame(Student_info_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=140,width=342,height=32)
        
        take_photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo",width=20,font=("arial",10,"bold"),bg="lightblue",fg="black")
        take_photo_btn.grid(row=0,column=0)
        
        update_photo_btn=Button(btn_frame2,command=self.update_dataset,text="Update Photo",width=20,font=("arial",10,"bold"),bg="lightblue",fg="black")
        update_photo_btn.grid(row=0,column=1)
        
        
        ##-----right frame
        
        right_frame=LabelFrame(main_frame,bd=2,text="Student Details",font=("arial",12,"bold"),relief=RIDGE,bg="aliceblue",fg="black")
        right_frame.place(x=750,y=10,width=560,height=475)
        
        img_right=Image.open(r"college-images\student.jpg")
        img_right=img_right.resize((75,75),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=20,y=5,width=75,height=75)
        
        
        
        #bottom bar
        img2=Image.open(r"college-images\label2.jpg")
        img2=img2.resize((1370,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=635,width=1370,height=100)
        
        
        #-------------search system--------------------
        '''
        search_frame=LabelFrame(right_frame,bd=2,text="Search System",font=("arial",10,"bold"),bg="aliceblue",fg="black")
        search_frame.place(x=10,y=80,width=540,height=70)
        
        search_label=Label(search_frame,text="Search By:",font=("arial",12,"bold"),fg="aliceblue",bg="orange")
        search_label.grid(row=0,column=0,pady=10,padx=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("arial",10),state="readonly")
        search_combo["values"]=("Select","studentID","dep")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=8,sticky=W)
        
        search_entry=ttk.Entry(search_frame,font=("arial",10),width=18)
        search_entry.grid(row=0,column=2,padx=2,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",width=6,font=("arial",10,"bold"),bg="lightblue",fg="black")
        search_btn.grid(row=0,column=3,padx=3)
        
        show_All_btn=Button(search_frame,text="Show All",width=7,font=("arial",10,"bold"),bg="lightblue",fg="black")
        show_All_btn.grid(row=0,column=4)
        '''
        
        #------------------table frame----------------
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=90,width=540,height=350) 
        
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("name","dep","ID","year","sem","email","phone","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        #-----------student tables-----------
        
        self.student_table.heading("name",text="Name")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("ID",text="RollNo")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("email",text="Student Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("Photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("name",width=110)
        self.student_table.column("dep",width=110)
        self.student_table.column("ID",width=110)
        self.student_table.column("year",width=110)
        self.student_table.column("sem",width=110)
        self.student_table.column("email",width=110)
        self.student_table.column("phone",width=110)
        self.student_table.column("Photo",width=110)
         
        self.student_table.pack(fill=BOTH,expand=1)
        
        #---cursor and fetching of data-----------
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
        
    #-----function for adding data to database----------
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()==0:
            messagebox.showerror("Error","All fileds needed to be filled.",parent=self.root)
        else:
            try: 
                conn=mysql.connector.connect(host="localhost",username="root",password="suju@123",database="project2")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student_table values(%s,%s,%s,%s,%s,%s,%s,%s)",(       
                                                                                                self.var_name.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_ID.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_sem.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_radio1.get()
                                                                                                
                                                                                            ))
                
                
                
                
                    
                conn.commit()
                
                #-----data fetch into table
                self.fetch_data()
                
                conn.close()
                messagebox.showinfo("success","Data added sucessfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}")
                
                
                
            
       #----------------fetch data into table--------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="suju@123",database="project2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student_table order by ID asc")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(* self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit() 
        conn.close()       


    
    #----------------get cursor function---------
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_name.set(data[0])
        self.var_dep.set(data[1])
        self.var_ID.set(data[2])
        self.var_year.set(data[3])
        self.var_sem.set(data[4])
        self.var_email.set(data[5])
        self.var_phone.set(data[6])
        self.var_radio1.set(data[7])

#-------------update function---------------------    
    
    def update_function(self):
      # Validation: Ensure all required fields are filled
        if self.var_dep.get().strip() == "Select Department" or self.var_name.get().strip() == "" or str(self.var_ID.get()).strip() == "":
            messagebox.showerror("Error", "All fields need to be filled.", parent=self.root)
            return
    
        try:
        # Confirm update action
            update_confirm = messagebox.askyesno("Update", "Do you want to update student details?", parent=self.root)
            if not update_confirm:
                return  # User canceled the update

        # Connect to database
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="suju@123",
            database="project2"
            )
            my_cursor = conn.cursor()

        # Execute update query using parameterized query to prevent SQL injection
            sql_update = """UPDATE student_table 
                        SET name=%s, dep=%s, year=%s, sem=%s, email=%s, phone=%s, PhotoSample=%s 
                        WHERE ID=%s"""
            values = (
            self.var_name.get().strip(),
            self.var_dep.get().strip(),
            self.var_year.get().strip(),
            self.var_sem.get().strip(),
            self.var_email.get().strip(),
            self.var_phone.get().strip(),
            self.var_radio1.get().strip(),
            self.var_ID.get()
            )

            my_cursor.execute(sql_update, values)
            conn.commit()

            # Close connection
            my_cursor.close()
            conn.close()

        # Refresh table data
            self.fetch_data()
            messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)

        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to update data: {e}", parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error", f"An unexpected error occurred: {ex}", parent=self.root)
            
    #------------delete data----------
    def delete_data(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="suju@123",database="project2")
                    my_cursor=conn.cursor()
                    sql="delete from student_table where ID=%s" 
                    val=(self.var_ID.get(),)
                    my_cursor.execute(sql,val)  
                else:
                    if not delete:
                        return
                    
                conn.commit() 
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete"<"Sucessfully delete message",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Deu To:{str(es)}",parent=self.root)
    #---------------reset button----------
    def reset_data(self):
        self.var_name.set("Select Student Name")
        self.var_dep.set("Select Department")  
        self.var_ID.set("")  
        self.var_year.set("Select Year")  
        self.var_sem.set("Select Semesster")  
        self.var_email.set("")  
        self.var_phone.set("")
        self.var_radio1.set("")   
        
        
    #----------------generate datasets function---------------     
    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_ID.get()==0:
            messagebox.showerror("Error","All fileds needed to be filled.",parent=self.root)
        else:
            try:               
                conn=mysql.connector.connect(host="localhost",username="root",password="suju@123",database="project2")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student_table")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student_table set name=%s,dep=%s,year=%s,sem=%s,email=%s,phone=%s,PhotoSample=%s where ID=%s",(
                                                                                                                        self.var_name.get(),
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_sem.get(),
                                                                                                                        self.var_email.get(),
                                                                                                                        self.var_phone.get(),
                                                                                                                        self.var_radio1.get(),
                                                                                                                        self.var_ID.get()==id+1
                                                                                                                        
                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()    
                conn.close()
                
                #-------load predefined data for frontal face from opencv----------------
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #---sacling factor=1.3
                    #--minimun nighbour=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id==100):
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generstion of data set completed!!!")  
                
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)      
                
                
                
    #-------------------risky code is here ---
    def update_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_ID.get() == 0:
            messagebox.showerror("Error", "All fields needed to be filled.", parent=self.root)
        else:
            try:
                # Delete existing images
                import os
                for filename in os.listdir("data"):
                    if filename.startswith("user." + str(self.var_ID.get())):
                        os.remove(os.path.join("data", filename))

            # Update database records
                conn = mysql.connector.connect(host="localhost", username="root", password="suju@123", database="project2")
                my_cursor = conn.cursor()
                my_cursor.execute("update student_table set name=%s, dep=%s, year=%s, sem=%s, email=%s, phone=%s, PhotoSample=%s where ID=%s", (
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_radio1.get(),
                    self.var_ID.get()
                ))
                conn.commit()

                # Capture new images
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(self.var_ID.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id == 100):
                        break
                cap.release()
                cv2.destroyAllWindows()

                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Result", "Update of dataset completed!!!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
            
                
                
                                  
        
if __name__ == "__main__":
   root=Tk()
   obj=Student(root)
   root.mainloop()        
