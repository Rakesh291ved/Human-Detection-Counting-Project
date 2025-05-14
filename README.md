# Human-Detection-Counting-Project
Human Detection &amp; Counting Project
🕵️ Human Detection & Counting System
Real-time People Detector using OpenCV's HOG + SVM!
Track, detect, and count people from images, videos, or your webcam—perfect for surveillance, crowd analysis, or AI-powered automation.

<div align="center"> <img src="https://img.shields.io/badge/OpenCV-RealTime-blue?logo=opencv" /> <img src="https://img.shields.io/badge/Python-3.8+-green?logo=python" /> <img src="https://img.shields.io/badge/HOG%2BSVM-HumanDetection-orange" /> </div>
👁️‍🗨️ Overview
This Python-based project uses the Histogram of Oriented Gradients (HOG) descriptor with a pre-trained SVM classifier to:

🔍 Detect humans in real-time

📦 Draw bounding boxes on each person

🔢 Count total people in view

💾 Optionally save output video or image

🔥 Features
✅ Human detection in images, videos, or webcam

🔲 Bounding box annotations with labels

📊 Real-time person counting

💽 Save results (image/video)

🧠 Simple CLI interface for flexible input types

⚡ Fast and lightweight (no deep learning model required!)

🧠 How It Works
Loads HOGDescriptor with OpenCV’s default SVM person detector

Accepts input from:

📷 Image file

🎥 Video file

💻 Live webcam feed

Resizes frames and runs detectMultiScale for people detection

Draws bounding boxes and labels each person

Displays the total count

Optionally writes results to an output file

🖼️ Demo Screenshots
<p align="center"> <img src="https://user-images.githubusercontent.com/human-detector/demo-frame.png" width="600"/> <br> <em>People detected with bounding boxes and live count</em> </p>
📦 Requirements
Install dependencies with pip:

bash
Copy code
pip install opencv-python imutils numpy
🚀 Usage
🔍 Detect from Image
bash
Copy code
python detect.py -i path/to/image.jpg -o output.jpg
🎥 Detect from Video
bash
Copy code
python detect.py -v path/to/video.mp4 -o output.avi
📹 Detect from Webcam
bash
Copy code
python detect.py -c true
📁 Project Structure
bash
Copy code
.
├── detect.py               # Main detection script
├── demo/                   # Folder to store demo images/videos
├── output/                 # Folder to store output results
├── README.md
⚙️ CLI Arguments
Argument	Description
-i, --image	Path to input image
-v, --video	Path to input video
-c, --camera	Set to true to use webcam
-o, --output	Path to save output (image/video)

📌 Notes
Press q to stop webcam/video detection.

Input must be a valid path (use full path if needed).

Resize operations ensure processing speed.

💡 Applications
🏙️ Crowd Monitoring

🛍️ Store Traffic Analysis

🏛️ Public Place Surveillance

🧪 Computer Vision Projects

🤖 Robot Vision & Automation

🙌 Credits
Powered by OpenCV and Python

Detection via HOG + SVM (no deep learning required)

📃 License
MIT License. Free for personal and commercial use.

👨‍💻 Author
[Vedanth] — Always looking for patterns in people 👥
