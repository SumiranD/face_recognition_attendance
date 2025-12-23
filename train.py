from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import os
import numpy as np
import cv2


class Train_Data:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Face Detection")
        
         #top bar
        img=Image.open(r"college-images\label2.jpg")
        img=img.resize((1370,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1370,height=100) 
        
        #background image
        img3=Image.open(r"college-images\train.jpg")
        img3=img3.resize((1370,450),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1370,height=568)
        
        
        #--------photo sample training-------
        
        title_lbl=Label(bg_img,text="Photo Sample Training",font=("Arial",30,"bold"),bg="aliceblue",fg="black")
        title_lbl.place(x=0,y=0,width=1370,height=50)
        
        
        b1=Button(bg_img,text="Train data",command=self.train_classifier,cursor="hand2",font=("arial",20,"bold"),bg="peru",fg="black")
        b1.place(x=500,y=250,width=350,height=100)
        
        
        
         #bottom bar
        img2=Image.open(r"college-images\label2.jpg")
        img2=img2.resize((1370,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=0,y=615,width=1370,height=100)
        
        
        
        
        
        #--LBPH algorithms for the training---------------
            
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]    
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')   #--grey scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id) 
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)
            
        #-----train the classifier and save----
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed")
        
        
        
        
if __name__ == "__main__":
   root=Tk()
   obj=Train_Data(root)
   root.mainloop()        
   
   
   
#----------Install cv2 properly-------

#---------training is also not working------------   