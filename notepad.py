from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
from tkinter.messagebox import showinfo

def cut():
    global text_area
    text_area.event_generate(("<<Cut>>"))

def help():
    showinfo("x-PAD","THIS SHOFTWARE MADE BY -: AMAN SHARMA")

def copy():
    global text_area
    text_area.event_generate(("<<Copy>>"))

def paste():
    global text_area
    text_area.event_generate(("<<Paste>>"))
    
def new():
    global text_area,file,root
    text_area.delete(1.0,END)
    root.title("Untitled -:x-PAD")
    

def open():
    global text_area,file
    file =askopenfilename(defaultextension =".txt",filetype =[("All files","*.*"),("Text document",".txt")])
    if file =="":
        file =NONE
    else:    
        root.title(os.path.basename(file)+" x-PAD")
        text_area.delete(1.0,END)
        with open(f"{file}","r")as f:
            text_area.insert(0.0,f.read())
            #f.close()


def save():
    global text_area,file,root
    if file ==NONE:
        file =asksaveasfilename(initialfile ="Untitled.txt",defaultextension =".txt",filetype =[("All files","*.*"),("Text document",".txt")])
        if file =="":
            file =NONE
        else:
            with open(file,"w") as f:
                f.write(text_area.get(1.0,END)) 
                f.close()

            root.title(os.path.basename(file) +" x-pad")    
        
def notepad():
    global root
    root = Tk()
    root.geometry("1000x600")
    root.minsize(800,500)
    # root.wm_iconbitmap("icons8-supplier-100.png")
    root.title("Untitled -:x-PAD")
    global text_area,file
    text_area = Text(root,font ="lucide 15")
    file =NONE
    text_area.pack(expand =True,fill =BOTH)

    scroll_bar =Scrollbar(text_area)
    scroll_bar.pack(side =RIGHT,fill =Y)
    scroll_bar.config(command =text_area.yview)
    text_area.config(yscrollcommand =scroll_bar.set)

    main_menu = Menu(root)
    sub_menu = Menu(main_menu,tearoff =0)

    sub_menu.add_command(label ="New...",command =new)
    sub_menu.add_command(label ="Open...",command =open)
    sub_menu.add_command(label ="Save..",command =save)
    sub_menu.add_separator()
    sub_menu.add_command(label ="Exit",command =quit)
    main_menu.add_cascade(label ="File",menu =sub_menu)

    edit_menu =Menu(main_menu,tearoff =0)
    edit_menu.add_command(label ="Cut",command =cut)
    edit_menu.add_command(label ="Copy",command =copy)
    edit_menu.add_command(label ="Paste",command =paste)

    main_menu.add_cascade(label ="Edit",menu =edit_menu)
    main_menu.add_cascade(label ="Help",command =help)

    root.config(menu =main_menu)
    root.mainloop()

if __name__ == "__main__":
    notepad()    