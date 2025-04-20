from tkinter import *
from tkinter import messagebox
import os
import base64

def main_screen():

      screen =  Tk()
      screen.geometry("375x398")
      #icon
      image_icon = PhotoImage(file = "key.png")
      screen.iconphoto(False, image_icon)
      screen.title("Secure_App")

      screen.mainloop()

main_screen()