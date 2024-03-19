from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('ImageViewer')

img1=ImageTk.PhotoImage(Image.open('iball.jpeg'))
img2=ImageTk.PhotoImage(Image.open('hall.png'))
img3=ImageTk.PhotoImage(Image.open('hall1.png'))
img4=ImageTk.PhotoImage(Image.open('hall2.jpeg'))

img_ls=[img1,img2,img3,img4]

label=Label(image=img_ls[0])
label.grid(row=0,column=0,columnspan=3)

class Next:
    def __init__(self):
        self.ind=0
        self.label=label
        
    def next(self):
        if self.ind<len(img_ls)-1:
            self.ind+=1
            self.label=self.label.grid_forget()
            self.label=Label(image=img_ls[self.ind])
            self.label.grid(row=0,column=0,columnspan=3)
            status=Label(root,text=f'Image {obj.ind+1} of {len(img_ls)}',bd=1,relief=SUNKEN,anchor=E)
            status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    
    def back(self):
        if self.ind>0:
            self.ind-=1
            self.label=self.label.grid_forget()
            self.label=Label(image=img_ls[self.ind])
            self.label.grid(row=0,column=0,columnspan=3)
            status=Label(root,text=f'Image {obj.ind+1} of {len(img_ls)}',bd=1,relief=SUNKEN,anchor=E)
            status.grid(row=2,column=0,columnspan=3,sticky=W+E)

obj=Next()

button1=Button(root,text='Quit',command=root.quit)
button2=Button(root,text='Back',command=lambda:obj.back())
button3=Button(root,text='Next',command=lambda:obj.next())
status=Label(root,text=f'Image {obj.ind+1} of {len(img_ls)}',bd=1,relief=SUNKEN,anchor=E)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)

root.mainloop()