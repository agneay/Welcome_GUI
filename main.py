import json
from tkinter import *
from PIL import ImageTk , Image
import AppOpener
 
f = open("~/.config/Welcome_GUI/config.json","r")
delta = f.read()

data = json.loads(delta)



# General Settings
bg_color = data["Background"]
Title = data["Title"]
Geometry = data["Geometry"]
Icon = data["Icon"]
Heading = data["Heading"]
Logo = data["Logo"]
Body = data["Body"]


#Buttons
btn_1_text = data["btn_1_text"]
btn_2_text = data["btn_2_text"]
btn_3_text = data["btn_3_text"]
btn_4_text = data["btn_4_text"]

#Heading settings
Heading_fg = data["Heading_fg"]
Heading_bg = data["Heading_bg"]
Heading_font = data["Heading_font"]
Heading_size = data["Heading_size"]
Heading_padx = int(data["Heading_padx"])
Heading_pady = int(data["Heading_pady"])

#Buttons color settings
btn1_fg = data["Btn_1_fg"]
btn2_fg = data["Btn_2_fg"]
btn3_fg = data["Btn_3_fg"]
btn4_fg = data["Btn_4_fg"]

btn1_bg = data["Btn_1_bg"]
btn2_bg = data["Btn_2_bg"]
btn3_bg = data["Btn_3_bg"]
btn4_bg = data["Btn_4_bg"]



#Body setttings
Body_fg = data["Body_fg"]
Body_bg = data["Body_bg"]
Body_font = data["Body_font"]
Body_size = data["Body_size"]
Body_padx = int(data["Body_padx"])
Body_pady = int(data["Body_pady"])


root = Tk()
root.title(Title)
root.geometry(Geometry)
root.config(bg=bg_color)
root.iconbitmap(Icon)

Label1 = Label(root,text=Heading,bg=Heading_bg,fg=Heading_fg,font=(Heading_font,Heading_size)).grid(row=0,column=0,padx=Heading_padx,pady=Heading_pady)
my_image = ImageTk.PhotoImage(Image.open(Logo))
Label2 = Label(image=my_image).grid(row=0,column=2)
Label3 = Label(root,text=Body,fg=Body_fg,bg=Body_bg,font=(Body_font,Body_size)).grid(row=1,column=0,columnspan=3,padx=Body_padx,pady=Body_pady)

def open1():
    AppOpener.open(btn_1_text)
def open2():
    AppOpener.open(btn_2_text)
def open3():
    AppOpener.open(btn_3_text)
def open4():
    AppOpener.open(btn_4_text)
btn1 = Button(root,text=btn_1_text,width=10,height=5,command=open1,padx=50,pady=10,fg=btn1_fg,bg=btn1_bg).grid(row=2,column=0)
btn2 = Button(root,text=btn_2_text,width=10,height=5,command=open2,padx=50,pady=10,fg=btn2_fg,bg=btn2_bg).grid(row=3,column=0)
btn3 = Button(root,text=btn_3_text,width=10,height=5,command=open3,padx=50,pady=10,fg=btn3_fg,bg=btn3_bg).grid(row=2,column=2)
btn4 = Button(root,text=btn_4_text,width=10,height=5,command=open4,padx=50,pady=10,fg=btn4_fg,bg=btn4_bg).grid(row=3,column=2)

#VALUE = IntVar()

#W = Checkbutton(root,text="Do Not Show Again",variable=VALUE,onvalue=1,offvalue=0).grid(row=400,column=0)
root.mainloop()
