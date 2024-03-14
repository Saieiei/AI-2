import cv2
import dlib

# Load the face detector from dlib
detector = dlib.get_frontal_face_detector()

# Load the pre-trained face recognition model from dlib
face_recognition_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model.dat")

# Load the image of the person to recognize
known_image = cv2.imread("known_person.jpg")

# Convert the image to grayscale
known_image_gray = cv2.cvtColor(known_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the known image
known_faces = detector(known_image_gray)

# Compute facial embeddings for the known faces
known_face_embeddings = [face_recognition_model.compute_face_descriptor(known_image_gray, face) for face in known_faces]

# Load the test image
test_image = cv2.imread("test_image.jpg")

# Convert the test image to grayscale
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

# Detect faces in the test image
test_faces = detector(test_image_gray)

# Iterate over each detected face in the test image
for test_face in test_faces:
    # Compute facial embeddings for the test face
    test_face_embedding = face_recognition_model.compute_face_descriptor(test_image_gray, test_face)
    
    # Compare the test face embeddings with the known face embeddings
    distances = [cv2.norm(test_face_embedding, known_face_embedding, cv2.NORM_L2) for known_face_embedding in known_face_embeddings]
    
    # Find the index of the closest match
    closest_match_index = np.argmin(distances)
    
    # Determine the threshold for considering the match
    threshold = 0.6
    
    # If the closest match is below the threshold, it's a match
    if distances[closest_match_index] < threshold:
        recognized_person = "Known Person"
    else:
        recognized_person = "Unknown"
    
    # Draw a rectangle around the face and display the recognized person's name
    x, y, w, h = test_face.left(), test_face.top(), test_face.width(), test_face.height()
    cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(test_image, recognized_person, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the output image with recognized faces
cv2.imshow("Facial Recognition Output", test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
