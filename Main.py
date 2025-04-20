from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("Error", "Please enter the secret key")
    elif password == "1234":  # Same key used in encrypt()
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        try:
            base64_bytes = message.encode("ascii")
            decode_bytes = base64.b64decode(base64_bytes)
            decrypt_msg = decode_bytes.decode("ascii")

            Label(screen2, text="DECRYPTED", font=("Arial", 15), fg="white", bg="#00bd56").place(x=10, y=0)

            text2 = Text(screen2, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)
            text2.insert(END, decrypt_msg)
        except Exception as e:
            messagebox.showerror("Decryption Error", "Invalid encrypted message or key.")
    else:
        messagebox.showerror("Invalid", "Incorrect Password")


def encrypt():
    password = code.get()

    if password == "":
        messagebox.showerror("Error", "Please enter the secret key")
    elif password == "1234":  # You can change this to your secure key
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_byte = base64.b64encode(encode_message)
        encrypt_msg = base64_byte.decode("ascii")

        Label(screen1, text="ENCRYPTED", font=("Arial", 15), fg="white", bg="#ed3833").place(x=10, y=0)

        text2 = Text(screen1, font="Roboto 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        text2.insert(END, encrypt_msg)
    else:
        messagebox.showerror("Invalid", "Incorrect Password")

def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("Secure_App")

    try:
        image_icon = PhotoImage(file="key.png")
        screen.iconphoto(False, image_icon)
    except Exception as e:
        print("Icon not loaded:", e)

    def reset():
        text1.delete("1.0", END)
        code.set("")

    Label(text="Enter text for Encryption and Decryption", fg="black", font=("Arial", 13)).place(x=10, y=10)

    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for Encryption and Decryption", fg="black", font=("Arial", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height=2, width=23, bg="#ED3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height=2, width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height=2, width=50, bg="#1089FF", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()

main_screen()
