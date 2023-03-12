
from PIL import Image

filename = 'data.pdf'

key = open('key.txt','a+')

with open(filename,'rb') as d:
    data = d.read()
    
    total_pixel = len(data)
    print("total pixels requrie: ",total_pixel)
    key.write(f'total pixels = {total_pixel}\n')

    img_width = 1920
    print("image width = ",img_width)
    key.write(f'image width orig = {img_width}\n')

    img_height = 1080
    print("image height = ",img_height)
    key.write(f'image height orig = {img_height}\n')

    block = 10
    print("pixel block size = ",block)
    key.write(f'pixel block size = {block}\n')

    
    make_width = img_width//block
    make_height = img_height//block

    print("make width and height = ",make_width,make_height)
    key.write(f'make width and height = {make_width} , {make_height}\n')


    print("one orignal image pixels = ",make_height*make_width)
    key.write(f'one orignal image pixels = ,{make_height*make_width}\n')


    total_full_img = total_pixel//(make_width*make_height)
    print("total full images = ",total_full_img)
    key.write(f'total full images = {total_full_img}\n')

    last_pixels = total_pixel%(make_width*make_height)
    print("last pixels = ",last_pixels)
    key.write(f'last pixels = {last_pixels}\n')

    key.close()
    
    count = 0
    temp = 0
    for i in range(0,(total_pixel-last_pixels),(make_width*make_height)):
        if(i==0):
            continue
        img = Image.frombytes(mode='1',size=(make_width,make_height),data=data[temp:i])
        img = img.resize((img_width,img_height))
        img.save(f"data\\{count}.png")
        print(f'{count} is completed..')
        temp = i
        count = count + 1
    
    last_bytes = data[total_pixel-last_pixels:total_pixel]+ bytes(1)*((make_width*make_height)-last_pixels)
    last_img = Image.frombytes(mode='1',size=(make_width,make_height),data=last_bytes)
    last_img = last_img.resize((img_width,img_height))
    img.save(f"data\\last.png")
    print("last image created suceddfully....")

print("image collected successfully....")