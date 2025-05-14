import cv2
import imutils
import numpy as np
import argparse

# Function to detect people in an image or video
def detect(frame):
    # Detect people using HOG (Histogram of Oriented Gradients)
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    
    # Start counting people
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        # Draw bounding box around the detected person
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f'Person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    # Add status text and total people count
    cv2.putText(frame, 'Status: Detecting', (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.putText(frame, f'Total Persons: {person - 1}', (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    cv2.imshow('Output', frame)  # Show the frame with the bounding boxes

    # Print the number of detected people in the terminal
    print(f"Total Persons Detected: {person - 1}")
    
    return frame

# Detect people in a video from a specified path
def detectByPathVideo(path, writer):
    video = cv2.VideoCapture(path)
    check, frame = video.read()

    if not check:
        print('Video not found. Please enter a valid path (Full path of the video should be provided).')
        return

    print('Detecting people...')
    while video.isOpened():
        check, frame = video.read()

        if check:
            frame = imutils.resize(frame, width=min(800, frame.shape[1]))
            frame = detect(frame)

            if writer is not None:
                writer.write(frame)

            key = cv2.waitKey(1)
            if key == ord('q'):  # Exit when 'q' is pressed
                break
        else:
            break

    video.release()
    cv2.destroyAllWindows()

# Detect people via webcam
def detectByCamera(writer):
    video = cv2.VideoCapture(0)  # Access the webcam
    print('Detecting people...')

    while True:
        check, frame = video.read()

        frame = detect(frame)
        if writer is not None:
            writer.write(frame)

        key = cv2.waitKey(1)
        if key == ord('q'):  # Exit when 'q' is pressed
            break

    video.release()
    cv2.destroyAllWindows()

# Detect people in an image
def detectByPathImage(path, output_path):
    image = cv2.imread(path)

    if image is None:
        print(f"Failed to load image from path: {path}")
        return

    image = imutils.resize(image, width=min(800, image.shape[1]))

    result_image = detect(image)

    if output_path is not None:
        cv2.imwrite(output_path, result_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main function to parse arguments and call appropriate detection function
def humanDetector(args):
    image_path = args["image"]
    video_path = args['video']
    if str(args["camera"]) == 'true':
        camera = True
    else:
        camera = False

    print(f'Image path: {image_path}')  # Add this print statement to ensure the path is passed correctly

    writer = None
    if args['output'] is not None and image_path is None:
        writer = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'MJPG'), 10, (600, 600))

    if camera:
        print('[INFO] Opening Web Cam.')
        detectByCamera(writer)
    elif video_path is not None:
        print('[INFO] Opening Video from path.')
        detectByPathVideo(video_path, writer)
    elif image_path is not None:
        print('[INFO] Opening Image from path.')
        detectByPathImage(image_path, args['output'])

# Argument parser function to handle command-line arguments
def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-v", "--video", default=None, help="path to Video File")
    arg_parse.add_argument("-i", "--image", default=None, help="path to Image File")
    arg_parse.add_argument("-c", "--camera", default=False, help="Set true if you want to use the camera.")
    arg_parse.add_argument("-o", "--output", type=str, help="path to optional output video file")
    args = vars(arg_parse.parse_args())

    return args

# Main block of code to execute the program
if __name__ == "__main__":
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    args = argsParser()
    humanDetector(args)
