
FPS = 60
img_width = 1920
img_height = 1080
total_images = 2291

video_name = 'output.mp4'

import cv2

video = cv2.VideoWriter(video_name,cv2.VideoWriter_fourcc(*'X256'),FPS,(img_width,img_height),isColor=False)

for i in range(total_images):
    img = cv2.imread(f'data\\{i}.png')
    video.write(img)
    print(f'{i} is added...')

img = cv2.imread(f'data\\last.png')
video.write(img)
print(f'last image is added...')

print("video created successfully....")

video.release()