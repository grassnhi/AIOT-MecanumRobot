import tkinter as tk
import sys
from Adafruit_IO import MQTTClient
import time
import random
from ohstem_simplecamera import *
import requests
from PIL import Image, ImageTk  # Import PIL for image display

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "grassnhi"
AIO_KEY = "aio_ZaES78XvsIHKHsUZGYxYRD693IVq"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id:" + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 0
sensor_type = 0
counter_ai = 5
ai_result = ""
previous_result = ""

def display_captured_image(image_path, ai_result, confidence_score):
    image_canvas.destroy()

    img = Image.open(image_path)
    img = img.resize((300, 300))  # Adjust the size as needed
    img = ImageTk.PhotoImage(img)

    image_label.config(image=img)
    image_label.image = img

    # Update AI result label
    result_label.config(text=f"AI Result: {ai_result}")

    # Update confidence score label
    score_label.config(text=f"Confidence Score: {confidence_score:.2f}")

# Function to initiate the continuous processing loop
def start_processing():
    camera_ip = camera_ip_entry.get()
    print("Camera IP:", camera_ip)
    img_url = f'http://{camera_ip}/capture'
    control_url = f'http://{camera_ip}/control?ai_camera='
    
    global counter_ai  # Declare counter_ai as a global variable
    counter_ai = 5  # Initialize counter_ai here or within your application logic
    global ai_result  # Declare ai_result as a global variable
    ai_result = ""
    while capture_ongoing:
        counter_ai -= 1
        if counter_ai <= 0:
            counter_ai = 5
            previous_result = ai_result

            response = requests.get(img_url)
            if response.status_code:
                fp = open('Pics//greenland_' + str(counter_ai) + '.png', 'wb')
                fp.write(response.content)
                fp.close()

                image_path = 'Pics//greenland_' + str(counter_ai) + '.png'
        
                ai_result, image, confidence_score = image_detector(counter_ai)

                display_captured_image(image_path, ai_result, confidence_score)

                root.update()  # Update the GUI to reflect changes
                
                print("AI Output: ", ai_result)
                if previous_result != ai_result:
                    client.publish("ai", ai_result)
                    client.publish("image", image)

                requests.get(control_url + ai_result)

        time.sleep(1)

# Tkinter GUI setup
root = tk.Tk()
root.title("AI Image Processing")

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
button_width = 9  # Define the width for all buttons

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
auto_button = tk.Button(root, text="Automatic Run", width=30, bg="#FFC08D")
auto_button.place(x=349, y=200)

# Labels to display AI result and confidence score
frame = tk.Frame(root, width=220, height=25, bg="#7CDBAF", bd=2, relief=tk.GROOVE)  # Kích thước lớn hơn
frame.place(x=350, y=275)
frame = tk.Frame(root, width=220, height=25, bg="#7CDBAF", bd=2, relief=tk.GROOVE)  # Kích thước lớn hơn
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

# Change background color
root.configure(bg='#CCE5FF') 

# Run the GUI main loop
root.mainloop()