from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1370x768+0+0")
        self.root.title("Developers")
        self.root.configure(bg="#f4f4f4")

        # Developer data
        self.developers = [
            {
        "name": "Rajendra Paneru",
        "email": "rajendrap021362@nec.edu.np",
        "photo": "college-images/rajendra.jpg"
    },
    {
        "name": "Sandesh Dhakal",
        "email": "sandeshd021377@nec.edu.np",
        "photo": "college-images/sandesh.jpg"
    },
    {
        "name": "Sumiran Dahal",
        "email": "sumirand021388@nec.edu.np",
        "photo": "college-images/sumiran.jpg"
    }
        ]

        # Set large window size (90% of screen)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{int(screen_width * 0.9)}x{int(screen_height * 0.9)}")

        # Canvas and scrollbar
        canvas = Canvas(self.root, bg="#f4f4f4", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=int(screen_width * 0.9))
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Developer Cards
        for dev in self.developers:
            card = Frame(scrollable_frame, bg="white")  # No border
            card.pack(padx=30, pady=20, fill="both", expand=True)  # Bigger space between cards

            card.config(height=250)  # Taller cards
            card.columnconfigure(1, weight=1)

            # Developer Image
            try:
                img = Image.open(dev["photo"])
                img = img.resize((150, 150))  # Resize image to 150x150 pixels
                photo = ImageTk.PhotoImage(img)
                img_label = Label(card, image=photo, bg="white")
                img_label.image = photo  # Keep reference to image
            except Exception as e:
                img_label = Label(card, text="No Image", bg="white", font=("Arial", 12))

            img_label.grid(row=0, column=0, padx=30, pady=25, sticky="n")

            # Developer Info
            info_frame = Frame(card, bg="white")
            info_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=25)

            name = Label(info_frame, text=dev["name"], font=("Helvetica", 20, "bold"), bg="white", anchor="w")
            name.pack(anchor="w", pady=(0, 10))

            email = Label(info_frame, text=dev["email"], font=("Helvetica", 16), bg="white", fg="#555", anchor="w")
            email.pack(anchor="w")

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
