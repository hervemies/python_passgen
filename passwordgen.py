# importing libraries
import secrets
import customtkinter as ctk
import string

# app settings
app = ctk.CTk()
app.resizable(width=False, height=False)
app.geometry('400x400')
app.title('password generator')

#declaring function for length
length = 16

length_var = ctk.StringVar(value='16')

strength_var = ctk.StringVar()

# password generation function
def generation():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(secrets.choice(alphabet) for _ in range(length))
    print(key)
    entry.configure(state='readonly')
    entry.configure(state='normal')
    entry.delete(0, 'end')
    entry.insert(0, key)
    entry.configure(state='readonly')
    entry.configure(state='normal')

    


# function for changing the length of the passwords generated
def set_length(choice):
    global length # making the length variable global, although it is bad practice
    length = int(choice)
    print(f'length changed, {length}')
    length_var.set(int(choice))



    if length <= 9:
        strength_var.set('Weak')
    elif length <= 16:
        strength_var.set('Good')
    elif length <= 23:
        strength_var.set('Strong')
    else:
        strength_var.set('Very Strong')




# declaring the entry variable and giving it a entry
entry = ctk.CTkEntry(app, width=350, height=50, font=('', 20))
entry.pack(pady=20)

label1 = ctk.CTkLabel(app, text='Character length:')
label1.pack()

length_text = ctk.CTkLabel(app, textvariable=length_var)
length_text.pack()


slider = ctk.CTkSlider(app, from_=4, to=30, command=set_length, width=350)
slider.pack(pady=20)

label2 = ctk.CTkLabel(app, text='Password Strength:')
label2.pack()

strength_text = ctk.CTkLabel(app, textvariable=strength_var)
strength_text.pack()

button = ctk.CTkButton(app, text='Generate Password!', command=generation, width=330, height=50, font=('', 30))
button.pack(pady=40)

# app appearance
ctk.set_appearance_mode('dark')

app.mainloop()



