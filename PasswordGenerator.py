import random
import string
from tkinter import *
import tkinter.font as font

# ###########################################
digits = list(string.digits*10 + string.ascii_lowercase*10)
uppercase = list(string.ascii_uppercase + string.ascii_lowercase)*30
lowercase = list(string.ascii_lowercase)*30
punct = list(string.ascii_lowercase*10 + string.punctuation*5)

upp_dig = list(string.digits*10 + string.ascii_lowercase*10 + string.ascii_uppercase*10)
upp_dig_pun = list(string.digits*10 + string.ascii_lowercase*10 + string.ascii_uppercase*10 + string.punctuation*5)
digits_pun = list(string.ascii_lowercase*10 + string.digits*10 + string.punctuation*5)
upp_pun = list(string.ascii_lowercase*10 + string.ascii_uppercase*10 +string.punctuation*5)
# ###########################################


# GUI
uppercase_status = False
digits_status = False
punct_status = False
back = '#B9B9B9'
def change_uppercase():
    global uppercase_status
    if uppercase_status == False:
        uppercase_status = True
    else:
        uppercase_status = False
    pass

def change_digits():
    global digits_status
    if digits_status == False:
        digits_status = True
    else:
        digits_status = False
    pass

def change_punct():
    global punct_status
    if punct_status == False:
        punct_status = True
    else:
        punct_status = False
    pass

def generate():
    clear()
    ########################## FUNCTIONS
    def simplegen():
        global rand_simp
        rand_simp = random.sample(lowercase, length_value)
        return rand_simp

    def uppergen():
        global rand_up
        rand_up = random.sample(uppercase, length_value)
        return rand_up

    def digigen():
        global rand_dig
        rand_dig = random.sample(digits, length_value)
        return rand_dig

    def pungen():
        global rand_pun
        rand_pun = random.sample(punct, length_value)
        return rand_pun

    def upper_dig():
        global rand_up_dig
        rand_up_dig = random.sample(upp_dig, length_value)
        return rand_up_dig

    def upper_dig_pun():
        global rand_up_dig_pun
        rand_up_dig_pun = random.sample(upp_dig_pun, length_value)
        return rand_up_dig_pun

    def dig_pun():
        global rand_dig_pun
        rand_dig_pun = random.sample(digits_pun, length_value)
        return rand_dig_pun

    def upper_pun():
        global rand_up_pun
        rand_up_pun = random.sample(upp_pun, length_value)
        return rand_up_pun
    ##########################
    length_value = scale_length.get()
    #### IF ALL ARE FALSE:
    if uppercase_status == False and digits_status == False and punct_status == False:
        simplegen()
        password_low = ''.join(rand_simp)
        maintext.insert('1.999999999', password_low)
        pass
    if uppercase_status == True and digits_status == False and punct_status == False:
        uppergen()
        password_up = ''.join(rand_up)
        maintext.insert('1.999999999', password_up)
        pass
    if uppercase_status == False and digits_status == True and punct_status == False:
        digigen()
        password_dig = ''.join(rand_dig)
        maintext.insert('1.999999999', password_dig)
        pass
    if uppercase_status == False and digits_status == False and punct_status == True:
        pungen()
        password_pun = ''.join(rand_pun)
        maintext.insert('1.999999999', password_pun)
        pass
    if uppercase_status == True and digits_status == True and punct_status == False:
        upper_dig()
        password_up_dig = ''.join(rand_up_dig)
        maintext.insert('1.999999999', password_up_dig)
        pass

    if uppercase_status == True and digits_status == True and punct_status == True:
        upper_dig_pun()
        password_up_dig_pun = ''.join(rand_up_dig_pun)
        maintext.insert('1.999999999', password_up_dig_pun)
        pass
    if uppercase_status == False and digits_status == True and punct_status == True:
        dig_pun()
        password_dig_pun = ''.join(rand_dig_pun)
        maintext.insert('1.999999999', password_dig_pun)
        pass
    if uppercase_status == True and digits_status == False and punct_status == True:
        upper_pun()
        password_up_pun = ''.join(rand_up_pun)
        maintext.insert('1.999999999', password_up_pun)
        pass
    pass

def copy():
    text_copy = str(maintext.get(1.0,END))
    root.clipboard_clear()
    root.clipboard_append(text_copy)
    root.update()
    pass

def clear():
    maintext.delete('0.0', END)
    pass

root = Tk()
root.title('Password Generator')
img = PhotoImage(file = 'icon.png')
root.tk.call('wm','iconphoto', root._w, img)
root.geometry(("700x300"))
root.minsize(700,300)
root.maxsize(700,300)
canvas = Canvas(root,width = 700,height = 300, bg = back)
canvas.pack()

maintext = Text(root, wrap = WORD)
maintext_font = font.Font(size = 20)
maintext['font'] = maintext_font
maintext.place(width = 550, height = 140,x = 700-550-75-50,y = 150)


check_for_uppercases = Checkbutton(root ,text = "Uppercase", bg = back)
check_for_uppercases.config(command = change_uppercase)
check_for_uppercases.place(height = 46,x = 10, y = 5)



check_for_digits = Checkbutton(root, text = "Digits", justify = "left", bg = back)
check_for_digits.config(command = change_digits)
check_for_digits.place(height = 50,x = 10, y = 50)


check_for_punct = Checkbutton(root, text = "Punctuation", bg = back)
check_for_punct.config(command = change_punct)
check_for_punct.place(height = 50,x = 10, y = 95)


generate_button = Button(root, text = "Generate", bg = back)
generate_button.config(command = generate)
generate_button.place(x = 590, y = 150, width = 100)

save_to_button = Button(root, text = "Copy", bg = back)
save_to_button.config(command = copy)
save_to_button.place(x = 590, y = 190, width = 100)

clear_button = Button(root, text = 'Clear', bg = back)
clear_button.config(command = clear)
clear_button.place(x = 590, y = 230 , width = 100)

copyright = Label(root, text = '©Unbewohnte', bg = back)
copyright.place(x = 590 ,y = 280)

scale_length = Scale(root, orient = "horizontal", length = 200, from_ = 1, bg = back)
scale_length.place(x = 370,y = 0)
label_length = Label(root, text = "The length :", bg = back)
label_length.place(x = 270,y = 20)


# ©Unbewohnte

root.mainloop()
