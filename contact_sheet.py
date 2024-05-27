import PIL
from PIL import Image
from PIL import ImageDraw

from PIL import ImageFont


# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# Split the image into red, green, and blue channels
r, g, b = image.split()
intensity=[0.1,0.5,0.9]
chanels=[0,1,2]
images=[]
for ch in chanels:
    for i in intensity:
        if ch==0:
            re=r.point(lambda x:x*i)
            new_image=Image.merge("RGB",(re, g, b))
            font = ImageFont.truetype("readonly/fanwood-webfont.ttf",50)
            draw=ImageDraw.Draw(new_image)
            draw.rectangle((0,390,800,450),fill="BLACK")
            draw.text((0,410), "channel 0 Intensity {}".format(i),font=font)
            images.append(new_image)
            
        elif ch==1:
            gr=g.point(lambda x:x*i)
            new_image=Image.merge("RGB",(r, gr, b))
            font = ImageFont.truetype("readonly/fanwood-webfont.ttf",50)
            draw=ImageDraw.Draw(new_image)
            draw.rectangle((0,390,800,450),fill="BLACK")
            draw.text((0,410), "channel 1 Intensity {}".format(i),font=font)
            images.append(new_image)
           
            
        elif ch==2:
            bl=b.point(lambda x:x*i)
            new_image=Image.merge("RGB",(r, g, bl))
            font = ImageFont.truetype("readonly/fanwood-webfont.ttf",50)
            draw=ImageDraw.Draw(new_image)
            draw.rectangle((0,390,800,450),fill="BLACK")
            draw.text((0,410), "channel 0 Intensity {}".format(i),font=font)
            images.append(new_image)
            


# create a contact sheet 
first_image=images[0]
contact_sheet=PIL.Image.new("RGB", (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)