import cv2

# Replace [IP_ADDRESS] with the actual IP address of your ESP32-CAM
url = "http://192.168.100.176:80"

# Open a connection to the video stream
cap = cv2.VideoCapture(url)

# Check if the connection is successful
if not cap.isOpened():
    print("Error: Couldn't open the video stream")
    exit()

# Read and display frames from the video stream
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Couldn't read frame")
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
