import tkinter as tk
import sys
import time
import random
from mqtt_client import *
from image_processing import *
import requests
from PIL import Image, ImageTk
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
    img = img.resize((300, 300))
    img = ImageTk.PhotoImage(img)

    image_label.config(image=img)
    image_label.image = img

    result_label.config(text=f"AI Result: {ai_result}")
    score_label.config(text=f"Confidence Score: {confidence_score:.2f}")

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

            # if ai_result == 'background':
            #     client.publish("ai", ai_result)
            #     client.publish("image", image)
            #     client.publish("score", str(confidence_score))


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

window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Label for the image display (For demonstration purposes)
image_label = tk.Label(root, width=300, height=300, bg="#CCE5FF")
image_label.place(x=20, y=20)
image_canvas = tk.Canvas(root, width=300, height=300, bg="#CCE5FF")
image_canvas.place(x=20, y=20)

# Buttons for car control
button_width = 9

right_button = tk.Button(root, text="Right", width=button_width, bg="#FFC08D")
right_button.place(x=495, y=145)
left_button = tk.Button(root, text="Left", width=button_width, bg="#FFC08D")
left_button.place(x=350, y=145)
up_button = tk.Button(root, text="Up", width=button_width, bg="#FFC08D")
up_button.place(x=422, y=120)
down_button = tk.Button(root, text="Down", width=button_width, bg="#FFC08D")
down_button.place(x=422, y=145)
return_button = tk.Button(root, text="Return", width=button_width, bg="#FFC08D")
return_button.place(x=422, y=170)
auto_button = tk.Button(root, text="Automatic", width=20, bg="#FFC08D")
auto_button.place(x=349, y=200)
stop_button = tk.Button(root, text="Stop", width=button_width, bg="#FFC08D")
stop_button.place(x=495, y=200)

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

# Labels to display AI result and confidence score
frame = tk.Frame(root, width=220, height=25, bg="#7CDBAF", bd=2, relief=tk.GROOVE)  
frame.place(x=350, y=275)
frame = tk.Frame(root, width=220, height=25, bg="#7CDBAF", bd=2, relief=tk.GROOVE)
frame.place(x=350, y=298)

result_label = tk.Label(root, text="AI Result: ", bg="#7CDBAF")
result_label.place(x=351, y=277)
score_label = tk.Label(root, text="Confidence Score: ", bg="#7CDBAF")
score_label.place(x=351, y=300)

# Button to start continuous processing
capture_button = tk.Button(root, text="Start Capturing", command=start_processing, width=30, bg="#7CDBAF")
capture_button.place(x=350, y=50)

capture_ongoing = False  # Flag to determine if capturing is ongoing

# Function to toggle capturing
def toggle_capture():
    global capture_ongoing
    if capture_ongoing:
        capture_ongoing = False
        capture_button.config(text="Start Capturing")
    else:
        capture_ongoing = True
        capture_button.config(text="End Capturing")
        start_processing()

capture_button.config(command=toggle_capture)

# Entry for entering the camera IP
camera_ip_label = tk.Label(root, text="Camera IP: ", bg="#7CDBAF")
camera_ip_label.place(x=350, y=20)

camera_ip_entry = tk.Entry(root, bg="#7CDBAF", font=('Arial', 12), width=17)
camera_ip_entry.place(x=415, y=20)

root.configure(bg='#CCE5FF') 
root.mainloop()