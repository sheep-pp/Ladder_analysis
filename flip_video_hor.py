import os
import cv2

def flip_video_horizontally(input_path, output_path):
    video_input = cv2.VideoCapture(input_path)
    
    if not video_input.isOpened():
        print(f"Error opening video file: {input_path}")
        return

    fps = video_input.get(cv2.CAP_PROP_FPS)
    frame_width = int(video_input.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_input.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    while video_input.isOpened():
        ret, frame = video_input.read()
        if not ret:
            break
        flipped_frame = cv2.flip(frame, 1)  # 1 for horizontal flipping
        output_video.write(flipped_frame)

    video_input.release() 
    output_video.release()
    cv2.destroyAllWindows()

def process_videos(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith((".mp4", ".mov", ".avi")):  
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"flipped_{filename}")
            print(f"Processing {filename}...")
            flip_video_horizontally(input_path, output_path)
            print(f"Saved flipped video as {output_path}")

if __name__ == "__main__":
    input_folder = '/Volumes/Inssia_NR2/rest_video_toflip_15'
    output_folder = '/Volumes/Inssia_NR2/video_flipped_python'
    process_videos(input_folder, output_folder)
