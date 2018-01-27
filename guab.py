import pytesseract
import cv2
import os
import requests

os.system("adb shell screencap -p /sdcard/DCIM/demo/demo.png")
os.system("adb pull /sdcard/DCIM/demo/demo.png C:/Users/Phun/Desktop/guab")

a = cv2.imread('demo.png')
flag = 0


for i in range(420,440):
    for j in range(86,130):
        # print(a[i,j,0])
        if a[i,j,0] != 255:
           flag = 1
           break

if flag == 0:    
    title = a[268:485,75:1005]
    ans_1 = a[500:600,105:970]
    ans_2 = a[640:740,105:970]
    ans_3 = a[780:880,105:970]
# cv2.imshow('view',ans_3)
# cv2.waitKey(0)

elif flag == 1:
    title = a[328:531,75:1005]
    ans_1 = a[570:670,105:970]
    ans_2 = a[710:810,105:970]
    ans_3 = a[850:950,105:970]
    

title_fin=pytesseract.image_to_string(title,lang='chi_sim').replace(" ","")
ans_1_fin=pytesseract.image_to_string(ans_1,lang='chi_sim').replace(" ","")
ans_2_fin=pytesseract.image_to_string(ans_2,lang='chi_sim').replace(" ","")
ans_3_fin=pytesseract.image_to_string(ans_3,lang='chi_sim').replace(" ","")

url = "https://www.so.com/s?&q=" + title_fin
# print(url)
r = requests.get(url,timeout=30)
text = r.text
# print(type(ans_1_fin))
if ans_1_fin != "":
    print(ans_1_fin,text.count(ans_1_fin))
if ans_2_fin != "":
    print(ans_2_fin,text.count(ans_2_fin))
if ans_3_fin != "":
    print(ans_3_fin,text.count(ans_3_fin))
