import string
from future.moves.tkinter import filedialog
from tkinter import *
import os
from cryptography.fernet import Fernet

"""function to turn text into caesar cipher"""
"""it takes the text input, the 'shift' input and the range of characters/etc. it needs to turn into caesar cipher"""


def caesarize(text, shift, alphabets):
    def shift_text(alphabets):
        return alphabets[shift:] + alphabets[:shift]

    shifted_alphabets = tuple(map(shift_text, alphabets))
    # print(shifted_alphabets)
    final_alphabets = ''.join(alphabets)
    final_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabets, final_shifted_alphabets)
    text2 = str(text.translate(table))
    text2 = list(text2)

    return str(text.translate(table))


"""function to show the result of the encryption in the output label.
it checks if a valid input exists in the "shift" field and outputs the result or an error message."""


def t_Insert():
    # print(str(shift.get("1.0", "end")))
    try:
        int(shift.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        output.config(
            text=(caesarize(textbox.get("1.0", "end"), int(shift.get("1.0", "end")),
                            [string.ascii_letters, string.digits])))

        return
    else:
        output.config(
            text="error - wrong shift input")
        print(str(shift.get("1.0", "end")).rstrip("\n"))


"""function to show the result of the decryption in the output label.
it checks if a valid input exists in the "shift" field and outputs the result or an error message."""


def t_Insert2():
    # print(str(shift.get("1.0", "end")))
    try:
        int(shift.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        output.config(
            text=(caesarize(textbox.get("1.0", "end"), int(shift.get("1.0", "end")) * -1,
                            [string.ascii_letters, string.digits])))
        return
    else:
        output.config(
            text="error - wrong shift input")
        print(str(shift.get("1.0", "end")).rstrip("\n"))


"""Import file dialog function"""


def import_dialog():
    file1 = filedialog.askopenfilename()
    if not file1.endswith('.txt'):
        textbox.delete('1.0', END)
        textbox.insert("1.0", "Wrong file type, please use text files.")
    else:
        file2 = open(file1, "r")
        if file2.readable():
            textbox.delete('1.0', END)
            textbox.insert("1.0", file2.read())
            file2.close()


"""Save output from 'output' box to file - dialog function"""


def save_dialog():
    if len(textbox.get("1.0", "end-1c")) == 0:
        output.config(
            text="error - no text was given")
        return

    s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if s_file is None:
        return
    file_text = str(output.cget("text"))
    s_file.write(file_text)


"""Output encrypted result to file - dialog function"""


def save_dialog_en():

    if len(textbox.get("1.0", "end-1c")) == 0:
        output.config(
            text="error - no text was given")
        return

    try:
        int(shift.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        text_var = (caesarize(textbox.get("1.0", "end"), int(shift.get("1.0", "end")),
                              [string.ascii_letters, string.digits]))

        s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if s_file is None:
            return
        s_file.write(text_var)

        only_file_name = os.path.basename(s_file.name)

        output.config(
            text=("File saved successfully - file name: " + only_file_name))

    else:
        output.config(
            text="error - wrong shift input")


"""Output decrypted result to file - dialog function"""


def save_dialog_de():

    if len(textbox.get("1.0", "end-1c")) == 0:
        output.config(
            text="error - no text was given")
        return

    try:
        int(shift.get("1.0", "end"))
        is_dig = True
    except:
        is_dig = False

    if is_dig:
        text_var = (caesarize(textbox.get("1.0", "end"), int(shift.get("1.0", "end")) * -1,
                              [string.ascii_letters, string.digits]))

        s_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if s_file is None:
            return
        s_file.write(text_var)

        # filtering the file name from file path
        only_file_name = os.path.basename(s_file.name)

        output.config(
            text=("File saved successfully - file name: " + only_file_name))

    else:
        output.config(
            text="error - wrong shift input")


"""just a test:"""
# text = "Hello World, 123, 890. @#$ Elad Or zZ!"
# print(caesarize(text, 1, [string.ascii_letters, string.digits]))

"""creating the tkinter window"""
window = Tk()
window.title("Elad - Encryption Project")
window.wm_geometry("780x550")  # app size
window.resizable(0, 0)

photo = PhotoImage(file="BGTK.png")
background_label = Label(window, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Label(window, text="Write the text you want to cipher/decipher:", bg="LightSteelBlue4", fg="white",
      font="none 12 bold").grid(
    row=1, column=0, sticky=W)

"""creating a text widget for the input text"""
textbox = Text(window, width=40, height=3, bg="LightSteelBlue1")
textbox.grid(row=2, column=0, sticky=W)

"""import file button"""
f_btn = Button(window, width=11, height=2, bg="turquoise2", command=import_dialog, text="Import file")
f_btn.grid(row=2, column=1, sticky=W)

en_btn = Button(window, width=20, height=2, bg="DeepSkyBlue2", command=save_dialog_en, text="Encrypt To File")
en_btn.grid(row=3, column=1, sticky=W)

de_btn = Button(window, width=20, height=2, bg="DeepSkyBlue3", command=save_dialog_de, text="Decrypt To File")
de_btn.grid(row=4, column=1, sticky=W)

Label(window, text="How many numbers forward or backwards (minus) do you want to shift it:", bg="LightSteelBlue4",
      fg="white",
      font="none 12 bold").grid(row=3, column=0, sticky=W)

"""text widget for shift input"""
shift = Text(window, width=7, height=1, bg="LightSkyBlue1", font="none 16")
shift.grid(row=4, column=0, sticky=W)

"""calculation button"""
btn = Button(window, width=11, height=2, bg="SteelBlue1", command=t_Insert, text="Encrypt")
btn.grid(row=5, column=0, sticky=W)

btn2 = Button(window, width=11, height=2, bg="SteelBlue2", command=t_Insert2, text="Decrypt")
btn2.grid(row=6, column=0, sticky=W)

btn3 = Button(window, width=11, height=2, bg="SteelBlue3", command=t_Insert2, text="Try Force")
btn3.grid(row=7, column=0, sticky=W)

"""the result label"""
output = Label(window, text="", width=85, height=4, bg="mint cream")
output.grid(row=8, column=0, sticky=W)

"""save output to file button"""
s_btn = Button(window, width=11, height=2, bg="deep sky blue", command=save_dialog, text="Save To File")
s_btn.grid(row=9, column=0, sticky=W)

"""exit button"""
btn = Button(window, width=11, height=2, bg="blue", command=window.destroy, text="Exit")
btn.grid(row=10, column=0, sticky=W)

window.mainloop()
