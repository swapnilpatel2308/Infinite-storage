from PIL import Image

total_images = 2291
file = 'output.pdf'
last_pixels = 1226
make_width = 192
make_height= 108

with open(file,'wb') as writer:
    for i in range(total_images):
        img1 = Image.open('data1\\0.png')
        img1 = img1.convert('1')
        img1 = img1.resize((make_width,make_height))
        arr1 = img1.tobytes()
        writer.write(arr1)
        print(f'{i} image is writed...')

last_img = 'data1\\last.png'  #data1 fonder last image path
img1 = last_img.convert('1')
img1 = img1.resize((make_width,make_height))
arr1 = img1.tobytes()[:last_pixels]
writer.write(arr1)
print("file decoded successfully....")