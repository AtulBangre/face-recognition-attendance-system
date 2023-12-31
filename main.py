from tkinter import*
import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student_Details 
from train import Train 
from face_recognizer import Face_Recognition
from attendence import Attendence
import os

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.resizable(False,False)
        self.root.title("Face Recognition System")
        

        # 1st Image
        img=Image.open(r"images\tit.jpg")
        img=img.resize((1530,130))
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)

        # # 2nd Image
        # img2=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        # img2=img.resize((510,130))
        # self.photoimg2=ImageTk.PhotoImage(img2)
        # f_lbl=Label(self.root,image=self.photoimg2)
        # f_lbl.place(x=510,y=0,width=510,height=130)

        # # 3rd Image
        # img3=Image.open(r"G:\face recognition attendance system\images\tit1.jpg")
        # img3=img3.resize((510,130))
        # self.photoimg3=ImageTk.PhotoImage(img3)
        # f_lbl=Label(self.root,image=self.photoimg3)
        # f_lbl.place(x=1020,y=0,width=510,height=130)

        # bg Image
        bgimg=Image.open(r"images\bg.jpg")
        bgimg=bgimg.resize((1530,710))
        self.photoimgbg=ImageTk.PhotoImage(bgimg)
        bg_img=Label(self.root,image=self.photoimgbg)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # Main label
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Student Button
        img4=Image.open(r"images\bt1.jpg")
        img4=img4.resize((220,220))
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(bg_img,command=self.student_details,image=self.photoimg4, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)
        b1_1=Button(bg_img,command=self.student_details,text="Student Details", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        img5=Image.open(r"images\bt2.jpg")
        img5=img5.resize((220,220))
        self.photoimg5=ImageTk.PhotoImage(img5)
        b2=Button(bg_img,command=self.face_recognizer,image=self.photoimg5, cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)
        b2_1=Button(bg_img,command=self.face_recognizer,text="Face Detector", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)

        # Attendance Button
        img6=Image.open(r"images\bt3.jpg")
        img6=img6.resize((220,220))
        self.photoimg6=ImageTk.PhotoImage(img6)
        b3=Button(bg_img,command=self.attend,image=self.photoimg6, cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)
        b3_1=Button(bg_img,command=self.attend,text="Attendance", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)

        # Help Desk Button
        img7=Image.open(r"images\bt4.png")
        img7=img7.resize((220,220))
        self.photoimg7=ImageTk.PhotoImage(img7)
        b4=Button(bg_img,image=self.photoimg7, cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)
        b4_1=Button(bg_img,text="Help Desk", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)

        # Train data Button
        img8=Image.open(r"images\bt5.png")
        img8=img8.resize((220,220))
        self.photoimg8=ImageTk.PhotoImage(img8)
        b5=Button(bg_img,command=self.train_data,image=self.photoimg8, cursor="hand2")
        b5.place(x=200,y=390,width=220,height=220)
        b5_1=Button(bg_img,command=self.train_data,text="Train Data", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=590,width=220,height=40)

        # Developer Button
        img9=Image.open(r"images\bt6.jpg")
        img9=img9.resize((220,220))
        self.photoimg9=ImageTk.PhotoImage(img9)
        b6=Button(bg_img,command=self.open_img,image=self.photoimg9, cursor="hand2")
        b6.place(x=500,y=390,width=220,height=220)
        b6_1=Button(bg_img,command=self.open_img,text="Photos", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=590,width=220,height=40)

        # Developer Button
        img10=Image.open(r"images\bt7.jpg")
        img10=img10.resize((220,220))
        self.photoimg10=ImageTk.PhotoImage(img10)
        b7=Button(bg_img,image=self.photoimg10, cursor="hand2")
        b7.place(x=800,y=390,width=220,height=220)
        b7_1=Button(bg_img,text="Developer", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=800,y=590,width=220,height=40)

        # Exit Button
        img11=Image.open(r"images\bt8.jpg")
        img11=img11.resize((220,220))
        self.photoimg11=ImageTk.PhotoImage(img11)
        b8=Button(bg_img,command=self.iexite,image=self.photoimg11, cursor="hand2")
        b8.place(x=1100,y=390,width=220,height=220)
        b8_1=Button(bg_img,command=self.iexite,text="Exit", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=590,width=220,height=40)

    # ===================== Buttons Functions =====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student_Details(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognizer(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attend(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendence(self.new_window)

    def iexite(self):
        self.iExite=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExite >0:
            self.root.destroy()
        else:
            return


    def open_img(self):
        os.startfile("data")
        





if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()