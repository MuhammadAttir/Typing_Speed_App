from tkinter import *
from tkinter import messagebox
from data import random_line  

# Initialize main window
window = Tk()
window.title('Typing Speed App')
window.geometry('1024x700')
window.config(bg='#2e2e2e')

# Global variables
seconds = 0
time_id = None

# ----------------------------------------------------Functions------------------------------------------------------------

def start_timer():
    global seconds, time_id

    text.config(state=NORMAL)
    text.focus()
    start.config(state=DISABLED)
    submit.config(state=NORMAL)

    mins = seconds // 60
    secs = seconds % 60
    time.config(text=f"{mins:02}:{secs:02}")

    seconds += 1
    time_id = window.after(1000, start_timer)

def stop_timer():
    global time_id
    if time_id:
        window.after_cancel(time_id)
        time_id = None

def reset_screen():
    global seconds
    stop_timer()
    seconds = 0

    time.config(text='00:00')
    start.config(state=NORMAL)
    submit.config(state=DISABLED)

    text.config(state=NORMAL)
    text.delete('1.0', END)
    text.config(state=DISABLED)

    calculate.config(text='Words per minute (wpm): ---\nAccuracy: ---')
    text_label.config(text=random_line())

def results():
    global seconds
    stop_timer()

    text.config(state=DISABLED)
    start.config(state=DISABLED)
    submit.config(state=DISABLED)

    user_text = text.get('1.0', END).strip()
    words = len(user_text.split())
    reference_text=text_label['text']
    
    correct_chars = 0
    for i in range(min(len(reference_text), len(user_text))):
        if reference_text[i] == user_text[i]:
            correct_chars += 1
            
    typed_chars=len(user_text)
    accuracy = round((correct_chars / typed_chars) * 100, 2) if typed_chars > 0 else 0


    if seconds == 0:
        seconds = 1  # avoid division by zero
        messagebox.showinfo('Instructions', 'Result may not be accurate if you typed under 1 minute')
         
    minutes = seconds / 60
    wpm = round(words / minutes,1)

    calculate.config(text=f"Words per minute (wpm): {wpm}\n Accuracy% : {accuracy}%")

# -------------------------------------------------------UI-------------------------------------------------------------


# Time Label
time = Label(
    text='00:00',
    font=("Segoe UI", 28, "bold"),
    bg='#2e2e2e',
    fg='#FF8800',
    bd=2
)
time.pack(pady=10)

# Instruction Label
read_label = Label(
    text='Type the following text:',
    font=("Segoe UI", 18, "bold"),
    bg='#2e2e2e',
    fg='#00FFCC'
)
read_label.pack(pady=5)

# Text to Write Label
text_label = Label(
    text=random_line(),
    font=("Consolas", 14),
    bg='#2e2e2e',
    fg='white',
    wraplength=750,
)
text_label.pack(pady=5)

# Typing Input Box (initially enabled)
text = Text(
    width=70,
    height=8,
    font=("Consolas", 14),
    bg='#1e1e1e',
    fg='#00FFCC',
    insertbackground='white',
    bd=2,
    relief="flat",
    wrap="word",
    state=DISABLED
)
text.pack(pady=10)

# Frame for Buttons
frame = Frame(window, bg='#2e2e2e')
frame.pack(pady=10)

start = Button(frame,
               text='Start',
               font=("Helvetica", 16, "italic"),
               bg='green',
               fg='white',
               width=15,
               height=2,
               activebackground='green',
               command=start_timer)
start.pack(side=LEFT, pady=10, padx=20)

reset = Button(frame,
               text='Reset',
               font=("Helvetica", 16, "italic"),
               bg='green',
               fg='white',
               width=15,
               height=2,
               activebackground='green',
               command=reset_screen)
reset.pack(side=LEFT, pady=10, padx=20)

submit = Button(frame,
                text='Submit',
                font=("Helvetica", 16, "italic"),
                bg='green',
                fg='white',
                width=15,
                height=2,
                activebackground='green',
                command=results,
                state=DISABLED)
submit.pack(side=LEFT, pady=10, padx=20)

# Result Labels
result_label = Label(
    text='Results',
    font=("Segoe UI", 18, "bold"),
    bg='#2e2e2e',
    fg="#FFFB00"
)
result_label.pack(pady=5)

calculate = Label(
    text='Words per minute (wpm): ---\nAccuracy: ---',
    font=("Consolas", 14),
    bg='#2e2e2e',
    fg="#00F7FF"
)
calculate.pack(pady=5)

window.mainloop()
