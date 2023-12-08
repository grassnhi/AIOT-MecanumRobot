from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import base64

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("E:\\Coding\\MecanumRobot(AI-IoT)\\Preparation\\LAB_MANUALS\\keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture("http://192.168.0.105:81/stream")

def image_detector():
    # Grab the webcamera's image.
    ret, image = camera.read()

    if ret: # Check if the frame was read successfully
        # ... (Rest of the function remains unchanged)

        # get image and convert to base64
        res, frame = cv2.imencode('.jpg', image)
        data = base64.b64encode(frame)
        # if image > 100KB
        if len(data) > 102400:
            print("Image is too big!")
            print(len(data))
        else:
            print("Publish image:")
            print(len(data))

        # Resize the raw image into (224-height,224-width) pixels
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

        # Show the image in a window
        cv2.imshow("Webcam Image", image)

        # Make the image a numpy array and reshape it to the models input shape.
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

        # Normalize the image array
        image = (image / 127.5) - 1

        # Predicts the model
        prediction = model.predict(image)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]

        # Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

        return class_name[2:], data
    # # Listen to the keyboard for presses.
    # keyboard_input = cv2.waitKey(1)

    # # 27 is the ASCII for the esc key on your keyboard.
    # if keyboard_input == 27:
    #     break
    else:
        print("Failed to retrieve frame from the camera.")

# def image_detector():
#     # Grab the webcamera's image.
#     ret, image = camera.read()

#     width = 800
#     height = 600
#     resized_image = cv2.resize(image, (width, height))

#     # Compress and encode the resized image to JPEG
#     # You can adjust the compression quality (0-100) as needed.
#     compression_params = [int(cv2.IMWRITE_JPEG_QUALITY), 50]  # Adjust the quality (50 is just an example)
#     ret, frame = cv2.imencode('.jpg', resized_image, compression_params)
#     data=base64.b64encode(frame)

#     if len(data)>102400:
#         print("image is too big")
#         print(len(data))
#     else:
#         print("publish image")
#         print(len(data))

#     # Resize the raw image into (224-height,224-width) pixels
#     image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

#     # Show the image in a window
#     # cv2.imshow("Webcam Image", image)

#     # Make the image a numpy array and reshape it to the models input shape.
#     image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

#     # Normalize the image array
#     image = (image / 127.5) - 1

#     # Predicts the model
#     prediction = model.predict(image)
#     index = np.argmax(prediction)
#     class_name = class_names[index]
#     confidence_score = prediction[0][index]

#     # Print prediction and confidence score
#     print("Class:", class_name[2:], end="")
#     print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
#     return class_name[2:],data

camera.release()
cv2.destroyAllWindows()
