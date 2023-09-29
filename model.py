import face_recognition
import cv2
import numpy as np

# Load the known face encodings
known_face_encodings = []
known_face_names = []

filename = "Ayush_train.jpg"
name = filename.split(".")[0]
image = face_recognition.load_image_file(filename)
face_encoding = face_recognition.face_encodings(image)[0]
known_face_encodings.append(face_encoding)
known_face_names.append(name)

# Load the input image
input_image = cv2.imread("Ayush_test.jpg")

# Convert the input image from BGR to RGB format
input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

# Detect all faces in the input image
face_locations = face_recognition.face_locations(input_image_rgb)

# Check if there is at least one face detected
if len(face_locations) > 0:

    # Compute the face encodings for each detected face
    face_encodings = face_recognition.face_encodings(input_image_rgb, face_locations)

    # Compare the face encodings to the known face encodings
    recognized_face_names = []
    for face_encoding in face_encodings:
        # Calculate the distance between the face encoding and each known face encoding
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        print(distances)
        # Get the index of the known face encoding with the smallest distance
        best_match_index = np.argmin(distances)

        # If the distance is less than a certain threshold, the face is recognized
        if distances[best_match_index] < 0.6:
            recognized_face_names.append(known_face_names[best_match_index])
        else:
            recognized_face_names.append("Unknown")

    # Draw a rectangle around each detected face and write the name of the person on top of the rectangle
    for (top, right, bottom, left), name in zip(face_locations, recognized_face_names):
        cv2.rectangle(input_image, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(input_image, name, (left, top - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Display the output image
    cv2.imshow("Face Recognition", input_image)
    cv2.waitKey(0)

else:
    print("No faces detected in the input image.")
