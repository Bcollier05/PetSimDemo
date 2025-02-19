import tkinter as tk
from PIL import Image, ImageTk

# Global Variables
x = 200  # Start position
cycle = 0
check = 0  # Start in idle position

window = tk.Tk()
window.configure(background='black')  # Set window background color
window.geometry("600x500")

# Create a Canvas to Hold the GIF (Only for background, not for label movement)


# Load GIF Frames
idle_frames = [tk.PhotoImage(file='PetSimDemo/assets/idle.gif', format='gif -index %i' % i) for i in range(5)]
idle_to_sleep_frames = [tk.PhotoImage(file='PetSimDemo/assets/changing.gif', format='gif -index %i' % i) for i in range(8)]
sleep_frames = [tk.PhotoImage(file='PetSimDemo/assets/sleeping.gif', format='gif -index %i' % i) for i in range(3)]
sleep_to_idle_frames = [tk.PhotoImage(file='PetSimDemo/assets/waking.gif', format='gif -index %i' % i) for i in range(8)]
walk_left_frames = [tk.PhotoImage(file='PetSimDemo/assets/left.gif', format='gif -index %i' % i) for i in range(8)]
walk_right_frames = [tk.PhotoImage(file='PetSimDemo/assets/right.gif', format='gif -index %i' % i) for i in range(8)]
yarn_frames = [tk.PhotoImage(file='PetSimDemo/assets/yarn.gif', format='gif -index %i' % i) for i in range(8)]



# Label to Display the GIF
label = tk.Label(window)
label.place(x=x, y=250)

# Function to Loop GIF Frames
def gif_work(cycle, frames):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
    return cycle

# Update Function
def update():
    global cycle, check, x

    if check == 0:  # Idle
        frame = idle_frames[cycle]
        cycle = gif_work(cycle, idle_frames)

    elif check == 1:  # Idle to Sleep Transition
        frame = idle_to_sleep_frames[cycle]
        cycle = gif_work(cycle, idle_to_sleep_frames)
        if cycle == 0:
            check = 2  # Move to sleep mode

    elif check == 2:  # Sleeping
        frame = sleep_frames[cycle]
        cycle = gif_work(cycle, sleep_frames)

    elif check == 3:  # Waking Up
        frame = sleep_to_idle_frames[cycle]
        cycle = gif_work(cycle, sleep_to_idle_frames)
        if cycle == 0:
            check = 0  # Go back to idle

    elif check == 4:  # Walking Left
        frame = walk_left_frames[cycle]
        cycle = gif_work(cycle, walk_left_frames)
        if x > 0:
            x -= 5

    elif check == 5:  # Walking Right
        frame = walk_right_frames[cycle]
        cycle = gif_work(cycle, walk_right_frames)
        if x < 500:
            x += 5
    
    elif check == 6:
        pass
        

    # Update the label with the new frame and position
    label.configure(image=frame)
    label.image = frame
    label.place(x=x, y=250)

    # Keep updating animation
    window.after(100, update)

# User Interaction Functions
def set_idle():
    global check
    check = 0

def walk_left():
    global check
    check = 4

def walk_right():
    global check
    check = 5

def idle_to_sleep():
    global check
    check = 1  # Start Idle → Sleep transition

def wake_up():
    global check
    if check == 2:
        check = 3  # Start waking up transition

def play_game():
    pass

# User interface
label = tk.Label(window, font=("Courier", 100), bg="black", fg="white")
label.pack(pady=10)  # Add padding to separate it from Text widget

# Text Widget (Resized to Fit Window)
T = tk.Text(window, bg='black', fg='white', bd=0, height=5, width=40)  # Reduced size
T.configure(font=("Courier", 14, "bold"))
T.place(x=100, y=100)
T.insert(tk.END, "Hello! I'm your virtual pet kitty💜")

# Add Buttons for Interaction
btn_idle = tk.Button(window, text="Idle", command=set_idle)
btn_idle.place(x=155, y=400)

btn_left = tk.Button(window, text="Walk Left", command=walk_left)
btn_left.place(x=195, y=400)

btn_right = tk.Button(window, text="Walk Right", command=walk_right)
btn_right.place(x=265, y=400)

btn_sleep = tk.Button(window, text="Sleep", command=idle_to_sleep)
btn_sleep.place(x=345, y=400)

btn_wake = tk.Button(window, text="Wake Up", command=wake_up)
btn_wake.place(x=395, y=400)

#btn_play = tk.Button(window, text="Play", command=play_game)
#btn_play.place(x=285, y=450)

# Start the animation loop
update()
window.mainloop()


