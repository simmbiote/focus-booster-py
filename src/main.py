# Step 1: Import Libraries

import tkinter as tk
from tkinter import ttk
import time
import pygame

pygame.init()

sound_start = pygame.mixer.Sound("./assets/focus.wav")
sound_about_to_finish = pygame.mixer.Sound("./assets/warning.wav")
sound_finish = pygame.mixer.Sound("./assets/focus_end.wav")


# Step 3: Create Timer Function
## TODO reset timer so that the buttons don't stack on top of each other
## TODO add a sound when the timer is done
## TODO add a progress bar
## TODO add a pause button
## TODO add a reset button

def start_timer(duration):
    global is_about_to_finish_played  # To ensure the 5-second warning only plays once
    
    if duration == 25 * 60:  # When a timer is started
        sound_start.play()
        
    if duration == 5:  # 5 seconds before it's about to finish
        if not is_about_to_finish_played:
            sound_about_to_finish.play()
            is_about_to_finish_played = True
    
    if duration == 0:  # When it finishes
        sound_finish.play()
        lbl.config(text="Done!")
        return
    
    mins, secs = divmod(duration, 60)
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    lbl.config(text=timeformat)
    
    root.after(1000, start_timer, duration-1)

# Step 2: Initialize Tkinter Window

root = tk.Tk()
root.title("Focus Booster Clone")
is_about_to_finish_played = False

# Step 4: Create GUI Elements

lbl = ttk.Label(root, text="25:00", font=("Helvetica", 48))
lbl.pack()

btn_start = ttk.Button(root, text="Start", command=lambda: start_timer(25 * 60))
btn_start.pack()

btn_break = ttk.Button(root, text="Short Break", command=lambda: start_timer(5 * 60))
btn_break.pack()

btn_long_break = ttk.Button(root, text="Long Break", command=lambda: start_timer(15 * 60))
btn_long_break.pack()

# Step 5: Run the Tkinter Event Loop

root.mainloop()


