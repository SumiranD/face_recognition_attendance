from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from train import Train_Data
from face_detector import Face_Detector
from attendance import Attendance
from help import Help
from developer import Developer
import os

class Face_Detection_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Face Detection")
        
        
        
        #top bar
        img=Image.open(r"college-images\labeltop.jpg")
        img=img.resize((1370,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1370,height=100)   
        
        
        #background image
        img3=Image.open(r"college-images\background.jpg")
        img3=img3.resize((1370,568),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1370,height=568)
        
        #title
        title_lbl=Label(bg_img,text="Attendance Using Face Detection",font=("Arial",30,"bold"),bg="silver",fg="black")
        title_lbl.place(x=0,y=0,width=1370,height=50)
        
        #student details button
        img4=Image.open(r"college-images\student.jpg")
        img4=img4.resize((200,200),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=150,height=150)
        
    
        b1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=150,y=250,width=150,height=30)
        
         #face Detecton button
        img5=Image.open(r"college-images\face_detection.jpg")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,command=self.face_detector,image=self.photoimg5,cursor="hand2")
        b1.place(x=350,y=100,width=150,height=150)
        
    
        b1=Button(bg_img,text="Face Detector",command=self.face_detector,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=350,y=250,width=150,height=30)
        
         #attendance button
        img6=Image.open(r"college-images\attendance.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,command=self.Attend,image=self.photoimg6,cursor="hand2")
        b1.place(x=550,y=100,width=150,height=150)
        
    
        b1=Button(bg_img,text="Attendance",command=self.Attend,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=550,y=250,width=150,height=30)
        
         #help desk button 
        img7=Image.open(r"college-images\help_desk.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,command=self.help_desk,image=self.photoimg7,cursor="hand2")
        b1.place(x=750,y=100,width=150,height=150)
        
    
        b1=Button(bg_img,text="Help Desk",command=self.help_desk,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=750,y=250,width=150,height=30)
        
        ##second row buttons
        #train data button
        img8=Image.open(r"college-images\traindata.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,command=self.training,image=self.photoimg8,cursor="hand2")
        b1.place(x=150,y=300,width=150,height=150)
        
    
        b1=Button(bg_img,text="Train Data",command=self.training,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=150,y=450,width=150,height=30)
        
         #photos Detecton button
        img9=Image.open(r"college-images\photos.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b1.place(x=350,y=300,width=150,height=150)
        
    
        b1=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=350,y=450,width=150,height=30)
        
         #developer button
        img10=Image.open(r"college-images\developer.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,command=self.developers,image=self.photoimg10,cursor="hand2")
        b1.place(x=550,y=300,width=150,height=150)
        
    
        b1=Button(bg_img,text="Developer",command=self.developers,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=550,y=450,width=150,height=30)
        
         #exit button 
        img11=Image.open(r"college-images\exit.jpg")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,command=self.close_window,cursor="hand2")
        b1.place(x=750,y=300,width=150,height=150)
        
    
        b1=Button(bg_img,text="Exit",command=self.close_window,cursor="hand2",font=15,bg="silver",fg="black")
        b1.place(x=750,y=450,width=150,height=30)
        
        
        
        #bottom bar
        img2=Image.open(r"college-images\labeltop.jpg")
        img2=img2.resize((1370,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=615,width=1370,height=100)
        
        
        #----------------------function---------------------
        
     #---function to open images in folder------       
    def open_img(self):
        os.startfile("data")
    
    #-----function to close app    
    def close_window(self):
        os._exit(0)  
            
    #--function for student detail   
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)
            
    #---function for training of the data-----        
    def training(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Data(self.new_window)
        
    #-----function for face detector--
    def face_detector(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Detector(self.new_window)
        
    #------function for attendance------
    def Attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    #----------function for help-desk -----
    
    
    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)   
        
    #----------function developers -----
    
    def developers(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)             
                  
              
        
if __name__ == "__main__":
   root=Tk()
   obj=Face_Detection_System(root)
   root.mainloop()
    
    
        

#--------to remove virtual environment ---------write-- rm -r env  env or file name