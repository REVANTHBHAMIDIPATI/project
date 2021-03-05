from tkinter import *
from tkinter import messagebox
import cv2
from PIL import Image
from PIL import ImageTk
import threading
import random
from pyzbar import pyzbar

class DetectionView:

    stop = False

    def load(self):

        window = Tk()
        window.title("Cheating Detection App")

        frame = Frame(window,padx=20,pady=20,bg="#7bed9f")
        frame.grid(row=0,column=0,padx=10,pady=10)

        self.l1 = Label(frame)
        self.l1.grid(row=1,column=0,columns=3)

        b1 = Button(frame,text="start",command= self.startCamera,pady=10)
        b1.grid(row=2,column=0,sticky='nsew',pady=10)

        b2 = Button(frame, text="stop",command=self.stopCamera,pady=10)
        b2.grid(row=2, column=1,sticky='nsew',pady=10)

        b3 = Button(frame, text="Capture", command=self.capturePhoto, pady=10)
        b3.grid(row=2, column=2, sticky='nsew', pady=10)

        self.l2 = Label(frame,text='STATUS - Camera Started',font=("Courier", 30))
        self.l2.grid(row=3,column=0,columns=3,sticky='nsew',pady=(10,0))

        self.startCamera()

        window.mainloop()

    def startCamera(self):
        self.stop = False

        self.cascade = cv2.CascadeClassifier('lib/nose.xml')
        self.cap = cv2.VideoCapture(0)
        t = threading.Thread(target= self.webcam, args=())
        t.start()

    def webcam(self):
        try:
            ret, image_frame = self.cap.read()
            image_frame = cv2.resize(image_frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
            barcodes = pyzbar.decode(image_frame)
            print(barcodes)

            self.img = Image.fromarray(image_frame)

            colorimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2RGB)
            grayimage = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

            # core functionality - Face ddetection
            r = self.cascade.detectMultiScale(grayimage,1.7,11)
            if len(r) != 0:
                for (x,y,w,h) in r:
                    cv2.rectangle(colorimage,(x,y),(x+w,y+h),(0,255,0),3)
                    self.l2.config(text="Face mask is not there")
            else:
                self.l2.config(text="Face is covered with mask")

            self.img = Image.fromarray(colorimage)
            img = ImageTk.PhotoImage(self.img)
            self.l1.configure(image=img)
            self.l1.image = img

            if self.stop == False:
                self.l1.after(10, self.webcam)
            else:
                self.l1.image = None


        except:
            print("Some error")

    def capturePhoto(self):
        image = self.img
        name = random.randint(0,9999)
        try:
            image.save(f'images/{name}.jpg')
            messagebox.showinfo('Alert','Image is saved')
        except:
            memoryview.showinfo('Alert','Some error in saving the image')




    def stopCamera(self):
        self.stop = True