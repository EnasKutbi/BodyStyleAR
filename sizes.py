
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import subprocess

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from center import center_window


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\WorkProjects\BodyStyleAR\assets\frame0") # مسار الفريم


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# دالة صفحة التفاحة
def open_apple():
    file_to_run_path = r"D:\WorkProjects\BodyStyleAR\apple.py" # مسار صفحة التفاحة
    window.destroy()
    subprocess.run(["python", file_to_run_path], check=True)

# صفحة الساعة الرملية
def open_hourglass():
    file_to_run_path = r"D:\WorkProjects\BodyStyleAR\hourglass.py" #مسار صفحة الساعة الرملية
    window.destroy()
    subprocess.run(["python", file_to_run_path], check=True)

# صفحة الكمثرى
def open_pears():
    file_to_run_path = r"D:\WorkProjects\BodyStyleAR\pears.py" #مسار صفحة الكمثرى
    window.destroy()
    subprocess.run(["python", file_to_run_path], check=True)

#صفحة المستطيل
def open_rectangle():
    file_to_run_path = r"D:\WorkProjects\BodyStyleAR\rectangle.py" #مسار صفحة المستطيل
    window.destroy()
    subprocess.run(["python", file_to_run_path], check=True)

def determine_body_shape():
    # نتأكد ان جميع الحقول غير فارغة
    if (entry_5.get() == "" or
        entry_shoulder.get() == "" or 
        entry_chest.get() == "" or 
        entry_waist.get() == "" or 
        entry_hip.get() == ""):
        messagebox.showwarning("خطأ", "عذراً، املأ جميع الحقول")
        return
    # نأخذ قيمة الحقول
    shoulder = float(entry_shoulder.get())
    chest = float(entry_chest.get())
    waist = float(entry_waist.get())
    hip = float(entry_hip.get())

    if shoulder > chest and chest > waist and waist < hip:
        open_hourglass() # يفتح صفحة الساعة الرملية
    elif shoulder < chest and waist < hip:
        open_apple() # صفحة التفاحة
    elif shoulder < chest and waist > hip:
        open_pears() # صفحة الكمثرى
    else:
        open_rectangle() # صفحة المستطيل

window = Tk()
window.title('Project') #عنوان الصفحة

window.geometry("396x688")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 688,
    width = 396,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
#زر التالي
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=determine_body_shape,
    relief="flat"
)
button_1.place(
    x=26.0,
    y=627.0,
    width=121.0,
    height=47.0
)
#حقل محيط الصدر
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    209.0,
    573.0,
    image=entry_image_1
)
entry_chest = Entry(
    bd=0,
    bg="#E8CFCF",
    fg="#000716",
    highlightthickness=0
)
entry_chest.place(
    x=61.0,
    y=548.0,
    width=296.0,
    height=48.0
)

canvas.create_text(
    177.0,
    512.0,
    anchor="nw",
    text="محيط الصدر",
    fill="#83787A",
    font=("Inter", 20 * -1)
)
#حقل محيط الورك
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    208.0,
    473.0,
    image=entry_image_2
)
entry_hip = Entry(
    bd=0,
    bg="#E8CFCF",
    fg="#000716",
    highlightthickness=0
)
entry_hip.place(
    x=60.0,
    y=448.0,
    width=296.0,
    height=48.0
)

canvas.create_text(
    176.0,
    412.0,
    anchor="nw",
    text="محيط الورك",
    fill="#83787A",
    font=("Inter", 20 * -1)
)
#حقل قياس الخصر
entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    208.0,
    373.0,
    image=entry_image_3
)
entry_waist = Entry(
    bd=0,
    bg="#E8CFCF",
    fg="#000716",
    highlightthickness=0
)
entry_waist.place(
    x=60.0,
    y=348.0,
    width=296.0,
    height=48.0
)

canvas.create_text(
    176.0,
    313.0,
    anchor="nw",
    text="قياس الخصر",
    fill="#83787A",
    font=("Inter", 20 * -1)
)
# حقل الكتف
entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    208.0,
    274.0,
    image=entry_image_4
)
entry_shoulder = Entry(
    bd=0,
    bg="#E8CFCF",
    fg="#000716",
    highlightthickness=0
)
entry_shoulder.place(
    x=60.0,
    y=249.0,
    width=296.0,
    height=48.0
)

canvas.create_text(
    176.0,
    213.0,
    anchor="nw",
    text="الكتف",
    fill="#83787A",
    font=("Inter", 20 * -1)
)
#حقل الطول
entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    208.0,
    182.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#E8CFCF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=60.0,
    y=157.0,
    width=296.0,
    height=48.0
)

canvas.create_text(
    176.0,
    121.0,
    anchor="nw",
    text="الطول",
    fill="#83787A",
    font=("Inter", 20 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    202.0,
    49.0,
    image=image_image_1
)
window.resizable(False, False)
center_window(window)
window.mainloop()
