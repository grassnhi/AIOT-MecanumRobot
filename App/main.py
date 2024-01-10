import tkinter as tk
from tkinter import ttk
import sys
import time
import random
from mqtt_client import *
from image_processing import *
import requests
from PIL import Image, ImageTk
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 192.168.160.18
counter = 0
sensor_type = 0
counter_ai = 5
ai_result = ""
previous_result = ""
consecutive_high_scores = 0

def display_captured_image(image_path, ai_result, confidence_score):
    image_canvas.destroy()

    img = Image.open(image_path)
    img = img.resize((400, 400))
    img = ImageTk.PhotoImage(img)

    image_label.config(image=img)
    image_label.image = img

    display_gauge(confidence_score, ai_result)


# Function to initiate the continuous processing loop
def start_processing():
    camera_ip = camera_ip_entry.get()
    print("Camera IP:", camera_ip)
    img_url = f'http://{camera_ip}/capture'
    control_url = f'http://{camera_ip}/control?ai_camera='
    
    global counter_ai  
    counter_ai = 5
    global ai_result
    ai_result = ""
    global previous_result, consecutive_high_scores
    consecutive_high_scores = 3
    result_published = False
    while capture_ongoing:
        # counter_ai -= 1
        # if counter_ai <= 0:
        #     counter_ai = 5

        response = requests.get(img_url)
        if response.status_code:
            fp = open('Pics//greenland_' + str(counter_ai) + '.png', 'wb')
            fp.write(response.content)
            fp.close()

            image_path = 'Pics//greenland_' + str(counter_ai) + '.png'

            ai_result, image, confidence_score = image_detector(counter_ai)

            display_captured_image(image_path, ai_result, confidence_score)
            root.update()

            if confidence_score > 0.8:
                if ai_result == previous_result:
                    consecutive_high_scores += 1
                else:
                    consecutive_high_scores = 1 
                    result_published = False

            if consecutive_high_scores >= 3 and not result_published:
                print("AI Output: ", ai_result)
                print("AI Score: ", confidence_score)

                client.publish("ai", ai_result)
                client.publish("image", image)
                client.publish("score", str(confidence_score))

                result_published = True  
                consecutive_high_scores = 0 

            previous_result = ai_result
            requests.get(control_url + ai_result)

        time.sleep(1)

# Tkinter GUI setup
root = tk.Tk()
root.title("AI Image Processing")
root.iconbitmap('icon.ico')

window_width = 1020
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

button_bg_color = "#B0C4DE"
button_fg_color = "green"
button_highlight_color = "#666666"

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Label for the image display
image_label = tk.Label(root, width=400, height=400, bg="#FFFFFF")
image_label.place(x=50, y=40)
image_canvas = tk.Canvas(root, width=400, height=400, bg="#666666")
image_canvas.place(x=50, y=40)

# Car control button
button_width = 12
button_font = ('Comic Sans MS', 11, 'bold')

right_button = tk.Button(root, text="Right", width=button_width, bg=button_bg_color, fg=button_fg_color,
                         highlightbackground=button_highlight_color, font=button_font, padx=8, pady=6, bd=3)
right_button.place(x=820, y=110)
left_button = tk.Button(root, text="Left", width=button_width, bg=button_bg_color, fg=button_fg_color,
                        highlightbackground=button_highlight_color, font=button_font, padx=8, pady=6, bd=3)
left_button.place(x=520, y=110)
up_button = tk.Button(root, text="Up", width=button_width, bg=button_bg_color, fg=button_fg_color,
                      highlightbackground=button_highlight_color, font=button_font, padx=8, pady=6, bd=3)
up_button.place(x=670, y=45)
down_button = tk.Button(root, text="Down", width=button_width, bg=button_bg_color, fg=button_fg_color,
                        highlightbackground=button_highlight_color, font=button_font, padx=8, pady=6, bd=3)
down_button.place(x=670, y=175)
return_button = tk.Button(root, text="Return", width=button_width, bg=button_bg_color, fg=button_fg_color,
                          highlightbackground=button_highlight_color, font=button_font, padx=8, pady=6, bd=3)
return_button.place(x=820, y=175)
auto_button = tk.Button(root, text="Automatic", width=button_width, bg=button_bg_color, fg=button_fg_color,
                        highlightbackground=button_highlight_color, font=button_font, padx=8, pady=6, bd=3)
auto_button.place(x=520, y=175)
stop_button = tk.Button(root, text="Stop", width=button_width, bg=button_bg_color, fg=button_fg_color,
                        highlightbackground=button_highlight_color, font=button_font, padx=8, pady=6, bd=3)
stop_button.place(x=670, y=110)

def on_enter(event):
    event.widget.config(bg="#3E4451", fg="#FFFFFF") 

def on_leave(event):
    event.widget.config(bg=button_bg_color, fg=button_fg_color)

# Bind the events to the buttons
right_button.bind("<Enter>", on_enter)
right_button.bind("<Leave>", on_leave)

left_button.bind("<Enter>", on_enter)
left_button.bind("<Leave>", on_leave)

up_button.bind("<Enter>", on_enter)
up_button.bind("<Leave>", on_leave)

down_button.bind("<Enter>", on_enter)
down_button.bind("<Leave>", on_leave)

return_button.bind("<Enter>", on_enter)
return_button.bind("<Leave>", on_leave)

auto_button.bind("<Enter>", on_enter)
auto_button.bind("<Leave>", on_leave)

stop_button.bind("<Enter>", on_enter)
stop_button.bind("<Leave>", on_leave)

def move_right():
    client.publish("ai", "right")
    print("Right button pressed")

def move_left():
    client.publish("ai", "left")
    print("Left button pressed")

def move_up():
    client.publish("ai", "straight")
    print("Up button pressed")

def move_down():
    client.publish("ai", "down")
    print("Down button pressed")

def return_position():
    client.publish("ai", "return")
    print("Return button pressed")

def automatic_run():
    toggle_capture()
    client.publish("ai", "automatic")
    print("Automatic pressed")

def stop_car():
    client.publish("ai", "stop")
    print("Stop button pressed")

# Update button commands to call the respective functions
right_button.config(command=move_right)
left_button.config(command=move_left)
up_button.config(command=move_up)
down_button.config(command=move_down)
return_button.config(command=return_position)
auto_button.config(command=automatic_run)
stop_button.config(command=stop_car)

result_label = tk.Label(root, text="AI Result", bg="#FFFFFF", font=('Trebuchet MS', 16, 'bold'), fg="orange")
result_label.place(x=520, y=245)

def display_gauge(confidence_score, ai_result):
    fig, ax = plt.subplots(figsize=(3, 3), subplot_kw={'projection': 'polar'})
    ax.set_ylim(0, 1)
    ax.set_yticklabels([])
    ax.set_xticks(np.radians([0, 90, 180, 270]))  # Set ticks at 0%, 25%, 50%, 75%
    ax.set_xticklabels(['0%', '25%', '50%', '75%'])  # Set percentage labels

    angle = confidence_score * 360 if confidence_score < 1 else 360

    ax.fill_between(np.radians(np.linspace(0, angle, 100)), 0, 1, color='orange', alpha=0.7)
    # ax.annotate(f"{ai_result} - {confidence_score:.2f}", xy=(1, 1), ha='center', va='center', fontsize=14, fontfamily='Trebuchet MS', fontweight='bold', color='orange')
    result_text = f"AI Result: {ai_result} - {confidence_score:.2f}"

    result_label.config(text=result_text)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().place(x=600, y=280)

display_gauge(0, "")

# Function for entry field
def on_entry_click(event):
    if camera_ip_entry.get() == 'Enter camera IP':
       camera_ip_entry.delete(0, "end")
       camera_ip_entry.insert(0, '')
       camera_ip_entry.config(fg = 'black')

def on_focusout(event):
    if camera_ip_entry.get() == '':
        camera_ip_entry.insert(0, 'Enter camera IP')
        camera_ip_entry.config(fg = 'grey')
    elif camera_ip_entry.get() != 'Enter camera IP':
        camera_ip_entry.config(fg = 'black')

camera_ip_entry = tk.Entry(root, bg="#FFFFFF", fg = 'grey', font=('Trebuchet MS', 13), width=44, relief=tk.FLAT, bd=2, insertbackground="#FFFFFF", highlightthickness=1, highlightbackground='black', highlightcolor='black')
camera_ip_entry.insert(0, 'Enter camera IP')
camera_ip_entry.place(x=50, y=470)
camera_ip_entry.bind('<FocusIn>', on_entry_click)
camera_ip_entry.bind('<FocusOut>', on_focusout)

# Capture btton
capture_button = tk.Button(root, text="Start Capturing", command=start_processing, width=42, bg="#7CDBAF", font=('Trebuchet MS', 12, 'bold'), fg="#FFFFFF", padx=8, pady=6, bd=2)
capture_button.place(x=50, y=520)

capture_ongoing = False 

def toggle_capture():
    global capture_ongoing
    if capture_ongoing:
        capture_ongoing = False
        capture_button.config(text="Start Capturing")
    else:
        capture_ongoing = True
        capture_button.config(text="End Capturing")
        start_processing()

capture_button.config(command=toggle_capture, bg=button_bg_color, fg=button_fg_color, highlightbackground=button_highlight_color)


root.configure(bg='#FFFFFF') 
root.mainloop()