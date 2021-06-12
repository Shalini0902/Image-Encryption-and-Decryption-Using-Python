from tkinter import *
from tkinter import filedialog

root=Tk()
root.minsize(width=250,height=250)
root.maxsize(width=300,height=350)

def encrypt_image():
    file=filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])

    if file is not None:    
        file_name=file.name
        key=entry1.get(1.0,END)
        f=open(file_name,'rb')
        image=f.read()
        f.close()
        image=bytearray(image)
        
        for index,values in enumerate(image):
            image[index]=values^int(key)
        f1=open(file_name,'wb')
        f1.write(image)
        f1.close()
        
button = Button(root,text="encrypt and decrypt",command=encrypt_image)
button.pack()

entry1=Text(root,height=1,width=10)
entry1.place(x=80,y=70)

root.mainloop()
