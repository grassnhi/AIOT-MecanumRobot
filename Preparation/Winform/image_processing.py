import time
import requests
from PIL import Image, ImageTk, ImageOps
from keras.models import load_model
import numpy as np
import cv2
import base64

model = load_model('keras_model.h5')

def image_detector(counter):
    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open('Pics//greenland_' + str(counter) +'.png')
    image_path = 'Pics//greenland_' + str(counter) +'.png'

    with open(image_path, 'rb') as f:
        image_data = f.read()

    encoded_image = base64.b64encode(image_data)
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.LANCZOS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)

    #get the 1D array
    output = prediction[0]
    #assign default value for max confidence
    max_index = 0
    max_confidence = output[0]
    #find the maximum confidence and its index
    for i in range(1, len(output)):
        if max_confidence < output[i]:
            max_confidence = output[i]
            max_index = i
    print(max_index, max_confidence)

    file = open("labels.txt",encoding="utf8")
    data = file.read().split("\n")
    print("AI Result: ", data[max_index])
    #client.publish("ai", data[max_index])
    return data[max_index], encoded_image, max_confidence

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
