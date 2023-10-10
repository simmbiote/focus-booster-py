import tkinter as tk
from tkinter import ttk
import pygame

def start_timer(duration):
    global is_about_to_finish_played, sound_start, sound_about_to_finish, sound_finish
    
    if duration == 25 * 60:
        sound_start.play()
        
    if duration == 5:
        if not is_about_to_finish_played:
            sound_about_to_finish.play()
            is_about_to_finish_played = True
    
    if duration == 0:
        sound_finish.play()
        lbl.config(text="Done!")
        return
    
    mins, secs = divmod(duration, 60)
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    lbl.config(text=timeformat)
    
    root.after(1000, start_timer, duration-1)

pygame.init()

root = tk.Tk()
root.title("Focus Booster Clone")

sound_start = pygame.mixer.Sound("assets/focus.wav")
sound_about_to_finish = pygame.mixer.Sound("assets/warning.wav")
sound_finish = pygame.mixer.Sound("assets/focus_end.wav")

is_about_to_finish_played = False

lbl = ttk.Label(root, text="25:00", font=("Helvetica", 48))
lbl.pack()

btn_start = ttk.Button(root, text="Start", command=lambda: start_timer(25 * 60))
btn_start.pack()

btn_break = ttk.Button(root, text="Short Break", command=lambda: start_timer(5 * 60))
btn_break.pack()

btn_long_break = ttk.Button(root, text="Long Break", command=lambda: start_timer(15 * 60))
btn_long_break.pack()

root.mainloop()