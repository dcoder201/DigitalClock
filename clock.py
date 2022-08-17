# To apply modern GUI for tkinter
import customtkinter
from tkinter.ttk import *
# For Time format display
from time import strftime

# setting custom appearance for application
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# setting color schemes for UI
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
# create CTk window like you do with the Tk window
app = customtkinter.CTk()
# setting title for application
app.title("Digital Clock")
# setting custom width and height for application
app.geometry("650x150")

# function to display in proper time format
def display_time():
    # storing time format in a variable
    var = strftime("%I:%M:%S  %p")
    # configuring label section with variable
    timer.config(text=var)
    # calling function after 1s to refresh timer
    timer.after(1000, display_time)

# setting custom font for display by storing settings in a variable
display_font = ("ds-digital", 95, "normal")
# setting label properties to configure display
timer = Label(app, background="black", foreground="red")
# setting custom font
timer.configure(font=display_font)
# aligning contents to center
timer.pack(anchor="center")
# calling function to display time
display_time()

# getting everything ready for display as we configured
app.mainloop()


