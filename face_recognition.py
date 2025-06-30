from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
from time import strftime
from datetime import datetime
import threading


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="Face Recognition", font=("times new roman", 30, "bold"), bg="white", fg="Red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\jgtf.jpg")
        img_top = img_top.resize((650, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        img_bottom = Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\khhg.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Face Recognition Button
        b1_1 = Button(f_lbl2, text="Face Recognition", cursor="hand2",
                      command=lambda: threading.Thread(target=self.face_recog).start(),
                      font=("times new roman", 15, "bold"), bg="darkgreen", fg="yellow")
        b1_1.place(x=350, y=600, width=300, height=40)

        # Exit Button
        b1_2 = Button(f_lbl2, text="Exit", cursor="hand2", command=self.exit_app,
                      font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_2.place(x=350, y=650, width=300, height=40)

    # Exit function
    def exit_app(self):
        self.root.destroy()

    # Mark Attendance
    def mark_attendance(self, id, roll, name, dep):
        with open("sayantan.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if ((id not in name_list) and (roll not in name_list) and (name not in name_list) and (dep not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{roll},{name},{dep},{dtString},{d1},Present")

    # Face Recognition Function
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                face_img = gray_image[y:y + h, x:x + w]
                face_img = cv2.resize(face_img, (200, 200))

                id, predict = clf.predict(face_img)
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="India@sayantan04", database="face_recognize"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student WHERE Student_id=%s", (str(id),))
                result = my_cursor.fetchone()

                if result and confidence > 70:
                    id, name, roll, dep = result
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                    cv2.putText(img, f"Student_id: {id}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Dept: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    self.mark_attendance(id, roll, name, dep)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                coord = [x, y, w, h]
                conn.close()

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        try:
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)
            while True:
                ret, img = video_cap.read()
                if not ret:
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Face Recognition", img)

                # Press Enter to exit
                if cv2.waitKey(1) == 13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            if 'video_cap' in locals():
                video_cap.release()
            cv2.destroyAllWindows()


# Main loop
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
