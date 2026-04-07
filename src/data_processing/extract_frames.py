import cv2
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
video_path = "../../dataset/videos/video1.mp4"   # input video
output_folder = "../../dataset/frames"          # folder to save frames
frame_skip = 5                                   # save every 5th frame (change to 1 to save all)

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# -----------------------------
# OPEN VIDEO
# -----------------------------
cap = cv2.VideoCapture(video_path)

frame_count = 0
saved_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break  # end of video

    # Save every nth frame
    if frame_count % frame_skip == 0:
        frame_name = f"frame_{saved_count}.jpg"
        cv2.imwrite(os.path.join(output_folder, frame_name), frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"Total frames read: {frame_count}")
print(f"Frames saved: {saved_count}")