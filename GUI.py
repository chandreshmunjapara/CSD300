from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from PIL import ImageTk,Image
import os

# Create tkinter frame
win = Tk()
win.title("Steganography")

# Set the geometry of tkinter frame
win.geometry("1000x562")
bg  = ImageTk.PhotoImage(Image.open("249790.jpg"))
  
# Show background image using label
label0 = Label( win, image = bg)
label0.place(x = 0, y = 0)

#Select Host Image
def open_file_Host():
   file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.jpg,*.png')])
   if file:
      filepath_Host = os.path.abspath(file.name)

#Select Secret Image  
def open_file_Secret():
   file = filedialog.askopenfile(mode='r', filetypes=[('Image Files', '*.jpg,*.png')])
   if file:
      filepath_Secret = os.path.abspath(file.name)

#New window to show stego image  
def openNewWindow():
   newWindow = Toplevel(win)
 
    
   newWindow.title("Stego")
 
   newWindow.geometry("300x300")
   frame = Frame(newWindow, width=256, height=256)
   frame.grid(row=0,column=0)
   frame.place(anchor='center', relx=0.5, rely=0.5)
  
   img = ImageTk.PhotoImage(Image.open("new.jpg"))

  
   label = Label(frame, image = img)
   label.grid(row=1,column=1)

   newWindow.mainloop()

#Download Image
def saveimg():
    im1 = Image.open('new.jpg')
    destinationdirectory = filedialog.askdirectory()
    im1 = im1.save(destinationdirectory +str("\stego.png"))
   


# Add a Label widget
label1 = Label(win, text="Click the Button to select Host Image", font=('Georgia 13'),bg="orange")
label1.place(x = 50, y = 150)

#Create Button
ttk.Button(win,text="Browse",command=open_file_Host).place(x = 175, y = 185)

# Add a Label widget
label2 = Label(win, text="Click the Button to select Secret Image", font=('Georgia 13'),bg="orange")
label2.place(x = 600, y = 150)


# Create a Button
ttk.Button(win, text="Browse", command=open_file_Secret).place(x = 750, y = 185)

# Add a Label widget
label3 = Label(win, text="Click the Button to view Stego Image", font=('Georgia 13'),bg="orange")
label3.place(x = 350, y = 350)

# Create a Button
ttk.Button(win, text="View Stego", command=openNewWindow).place(x = 475, y =385)

# Add a Label widget
label1 = Label(win, text="Click the Button to download stego image", font=('Georgia 13'),bg="orange")
label1.place(x = 350, y = 465)

# Create a Button
ttk.Button(win, text="Download", command=saveimg).place(x = 475, y = 500)


win.mainloop()
