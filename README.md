🎓 Face Recognition Based Attendance System

A smart student attendance system that uses face recognition for automated attendance marking. Built with OpenCV, Tkinter, and MySQL, this project provides a complete solution from student registration to real-time attendance tracking.

✨ Features

📷 Face Detection using Haar Cascade classifier

🧑‍🎓 Face Recognition with the LBPH algorithm

🎥 Real-time attendance marking via webcam

📝 Student Data Entry with image dataset generation

📊 Attendance Report Export in CSV format

🖥️ User-friendly GUI built with Tkinter

🛠️ Technologies Used

Python

OpenCV → Face detection & recognition

Tkinter → Graphical User Interface

MySQL → Student database management

NumPy, PIL, CSV → Data handling and storage

📂 Project Structure
├── main.py               # Main window with GUI buttons
├── student.py            # Student registration + photo capture
├── train.py              # Train LBPH classifier using collected images
├── face_recognition.py   # Real-time face recognition & attendance marking
├── attendance.py         # Attendance viewing/export to CSV
├── data/                 # Captured student images
├── classifier.xml        # Trained LBPH model file
├── sayantan.csv          # Sample attendance CSV
└── README.md             # Project documentation

⚙️ Installation & Setup
Prerequisites

Python 3.x

MySQL Server

Required libraries:

pip install opencv-python pillow numpy mysql-connector-python

Steps to Run

Clone the repository

git clone https://github.com/your-username/Face-recognition-based-attendance-system.git
cd Face-recognition-based-attendance-system


Set up MySQL Database

CREATE DATABASE attendance;
USE attendance;

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    roll_no VARCHAR(20),
    name VARCHAR(50),
    department VARCHAR(50),
    batch VARCHAR(20)
);


Run the main application

python main.py

🚀 Usage

Register Students → Add details & capture face samples

Train Model → Train LBPH classifier with collected data

Mark Attendance → Real-time recognition via webcam

Export Records → Save attendance as CSV file

📸 Screenshots

<img width="1902" height="1016" alt="image" src="https://github.com/user-attachments/assets/b72271f9-e2ca-4b97-9f25-56c0fd2aeb83" />
<img width="1883" height="1017" alt="image" src="https://github.com/user-attachments/assets/ed4b29c9-7c6c-4ee7-a43b-d544e2a45c65" />
<img width="1907" height="1012" alt="image" src="https://github.com/user-attachments/assets/6ac7ac52-7cd7-49c4-8f7c-e1fdfdd6d355" />

👨‍💻 Author

Sayantan Sadhukhan
