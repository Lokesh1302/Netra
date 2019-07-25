import cv2
import numpy as np
import os
import face_recognition
import keyboard


################## Load database and encode all

known_face_encodings = []

images = os.listdir('D://Code_facial_recognition//images')

for image in images:
    # load the image
    current_image = face_recognition.load_image_file("D://Code_facial_recognition//images//" + image)
    # encode the loaded image into a feature vector
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    known_face_encodings.append(current_image_encoded)

##################

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

count = 0

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    
    while(ret == False):
        print("1")
        video_capture = cv2.VideoCapture(1)
        video_capture = cv2.VideoCapture(0)
        ret, frame = video_capture.read()
    
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)    
         # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
        else:
            cv2.imwrite("D://Code_facial_recognition//images//frame%d.jpg" % count, frame)
            current_image = face_recognition.load_image_file("D://Code_facial_recognition//images//frame%d.jpg" % count)
            # encode the loaded image into a feature vector
            current_image_encoded = face_recognition.face_encodings(current_image)[0]
            known_face_encodings.append(current_image_encoded)
            count += 1
        # Hit 'q' on the keyboard to quit!
        if keyboard.is_pressed('q'):
            break
    process_this_frame = not process_this_frame
    
video_capture.release()
cv2.destroyAllWindows()