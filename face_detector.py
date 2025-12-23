from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import numpy as np

class Face_Detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1370x768+0+0")
        self.root.title("Face Detector")

        # ---- Title and Background Image -----
        img1 = Image.open(r"college-images\background2.jpg")
        img1 = img1.resize((1370, 568))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0, y=100, width=1370, height=568)
        title_lbl = Label(bg_img, text="Face Detector", font=("Arial", 30, "bold"), bg="silver", fg="black")
        title_lbl.place(x=0, y=0, width=1370, height=50)

        # ---- Face Detector Image and Button -----
        img_left = Image.open(r"college-images\facedetector.jpg")
        img_left = img_left.resize((356, 356))
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(bg_img, image=self.photoimg_left, cursor="hand2")
        f_lbl.place(x=500, y=75, width=356, height=356)

        b1 = Button(bg_img, text="Detect Face", command=self.face_recog, cursor="hand2",
                    font=("arial", 20, "bold"), bg="darkgreen", fg="white")
        b1.place(x=500, y=430, width=358, height=50)
           
           
           #--------for adding to xlm file-------------
    def mark_attendance(self, name, student_id, department):
      with open("raju.csv", "r+", newline="\n") as f:
        myDataList = f.readlines()
        name_list = []
        for line in myDataList:
            entry = line.split((","))  
            name_list.append(entry[0])
        if ((name not in name_list) and (student_id not in name_list) and (department not in name_list)):
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name},{student_id},{department},{dtString},{d1},Present")
      
           
    def face_recog(self):
        def draw_boundaries(img, classifier, scalefactor, minNeighbors, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scalefactor, minNeighbors)

            for (x, y, w, h) in features:
                # Adjusted Rectangle Position & Thickness
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                # Connect to Database
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="suju@123", database="project2")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Name FROM student_table WHERE ID=%s", (id,))
                    name = my_cursor.fetchone()
                    name = name[0] if name else "Unknown"

                    my_cursor.execute("SELECT ID FROM student_table WHERE ID=%s", (id,))
                    student_id = my_cursor.fetchone()
                    student_id = student_id[0] if student_id else "Unknown"

                    my_cursor.execute("SELECT dep FROM student_table WHERE ID=%s", (id,))
                    department = my_cursor.fetchone()
                    department = department[0] if department else "Unknown"

                    conn.close()
                except mysql.connector.Error as e:
                    print(f"Database Error: {e}")
                    name, student_id, department = "Error", "Error", "Error"

                # Adjusted Text Positions
                if confidence > 77:
                    cv2.putText(img, f"RollNo: {student_id}", (x, y - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(img, f"Name: {name}", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    cv2.putText(img, f"Dept: {department}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                    self.mark_attendance(name, student_id, department)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

            return img

        def recognize(img, clf, faceCascade):
            return draw_boundaries(img, faceCascade, 1.1, 10, clf)

        # Load Haar Cascade for Face Detection
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        # Load the trained model
        clf = cv2.face.LBPHFaceRecognizer_create()
        try:
            clf.read("classifier.xml")
        except:
            messagebox.showerror("Error", "Classifier file not found!")
            return

        # Start Camera
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to access camera!")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Detector(root)
    root.mainloop()
