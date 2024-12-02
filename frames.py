import cv2
import os

# Specify the path to your video file
path = r"C:\Users\sammj\Downloads\IR.mp4"
video_capture = cv2.VideoCapture(path)

frame_count = 0  # Counter for frames

# Specify the output folder on the desktop
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
output_folder = os.path.join(desktop_path, 'frames_output')
os.makedirs(output_folder, exist_ok=True)

while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Specify the frame time interval in milliseconds (e.g., 500ms for every half second)
    frame_interval = 1000  # Change this value to the desired frame time interval

    # Save frames at specified intervals into the output folder on the desktop
    if frame_count % (video_capture.get(cv2.CAP_PROP_FPS) * (frame_interval / 1000)) == 0:
        frame_path = os.path.join(output_folder, f'frame_{frame_count}.jpg')
        cv2.imwrite(frame_path, frame)

    frame_count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
video_capture.release()
cv2.destroyAllWindows()
