# Face-recognition-based-attendance-system
A face recognition-based smart student attendance system using OpenCV, MySQL, and Tkinter.

## Features
- Face detection using Haar Cascades
- Face recognition using LBPH algorithm
- Real-time webcam-based attendance marking
- Student data entry with image samples
- CSV export of attendance reports
- GUI built with Python Tkinter

## Technologies Used

- **Python**
- **OpenCV** (for face detection & recognition)
- **Tkinter** (for GUI)
- **MySQL** (for storing student info)
- **NumPy**, **PIL**, **CSV**

## Project Structure
├── main.py               # Main window with buttons
├── student.py            # Student registration + photo capture
├── train.py              # Train LBPH classifier using collected images
├── face_recognition.py   # Real-time face recognition and attendance
├── attendance.py         # View/export attendance records
├── data/                 # Stored images of students
├── classifier.xml        # Trained LBPH model
├── sayantan.csv          # Attendance CSV file
└── README.md
