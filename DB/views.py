from django.shortcuts import render
from .models    import *
import cv2
import numpy as np
from pytesseract import *

pytesseract.tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract.exe"


def main(request):

    return render(request,'main.html')


def maintest(request):

    return render(request,'maintest.html')

def kakaomap(request):
    hospital = Hospital.objects.all()

    return render(request,'kakaomap.html',{'hospital':hospital })


def camera(request):




    return render(request,'camera.html')


def history(request):

    img = image.objects.all()

    return render(request,'history.html',{'img':img})


def result(request):


    prescription = image.objects.create(
       sample=request.FILES.get('camera'),
   )

    pic = prescription.sample

    pic = "./media/"+ str(pic)

    img = cv2.imread("test4.jpg")
    orig = img.copy() #원본 이미지 복사

    rect_img = img[355:660, 60:317]

    #r = 800.0 / img.shape[0]
    #dim = (int(img.shape[1] * r), 800)
    #img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    #print("STEP 1: Edge Detection")

    #cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    #cv2.namedWindow('edged', cv2.WINDOW_NORMAL)

    #print(str(pytesseract.image_to_string(img)))
    custom_config = 'outputbase nobatch digits'

    number = pytesseract.image_to_string(rect_img,config=custom_config)

    dist = ""
    db = []

    for num in number:
        dist += num
        if(num == "\n"):
            try:
                db.append(Medicine.objects.get(m_Code=int(dist)))
            except:
                continue

    count = len(db)





    return render(request,'result.html',{'db':db, 'count':count})
