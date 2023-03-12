import cv2

video_file_name = ''

cam = cv2.VideoCapture(video_file_name)

c = 0
while(True):
    ret , frame = cam.read()
    cv2.imwrite(f"data1\\{c}.png",frame)
    c = c + 1
    print(f'{c} is extected.....')

#in this code last image name change with last.png

