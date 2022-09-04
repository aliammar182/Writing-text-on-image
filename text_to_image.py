from PIL import Image, ImageDraw, ImageFont
import textwrap
import pandas as pd
import os

in_dir =  input("Enter path where the script is located : ")

in_file = input("\n\nEnter the name of the file without extension: ")

#font_path =  input("Enter path where the fonts are located : ")



newpath = os.path.join(in_dir, "Text Written")
if not os.path.exists(newpath):
    os.makedirs(newpath)
destination_folder = os.path.join(newpath, "")



spread = input('\nPlease enter the spread of text\n(Higher the number, less text will be centered aligned) \nRecommended number is 25:\n')

height = input ('\n\nPlease enter height of text\nLower the number, lower it will move in the image\nRecommended number is between 3.5 to 4.0:\n')

width =  input ('\n\nPlease enter width of text\n-ve number will move text to left and vice versa for +ve\nRecommended number is 0:\n')

line_spacing = input ('\n\nPlease enter line spacing for text\nRecommended number is 10:\n')

line_spacing = int(line_spacing)

font = input ('\n\nPlease enter the font of the text:\nFor instance arial:\n')

size_font = input ('\n\nPlease enter font size of text\nFor instance 50:\n')

color_fill = input ('\n\nPlease enter color fill of text\nFor instance #000000:\n').lstrip('#')

RGB =  tuple(int(color_fill[i:i+2], 16) for i in (0, 2, 4))
list_val = list(RGB)

opacity = input ('\n\nPlease enter opacity of text\nAny number between 0 and 255, with 0 being full transparent:\n')
list_val.insert(len(list_val), int(opacity))
final_color = tuple(list_val)

#opa_val = list(RGB)
#opa_val.insert(len(list_val), 0)
#final_opa = tuple(opa_val)

df = pd.read_excel(in_file+'.xlsx',header = 'infer')
df['Text'] = df['Text'].astype('string')

for i in range(0,df['Text'].size):
  astr = '''{}'''.format(df[['Text']].values[i][0])


#astr = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
#incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation.
#'''



  for file in os.listdir(in_dir):
        if file.endswith(".png"):

#greater the number, more it will move outside the parameters
          para = textwrap.wrap(astr, width=int(spread))



          im = Image.open(file)
          txt = Image.new("RGBA", im.size, (255,255,255,0))
          MAX_W, MAX_H = im.size[0]+int(width),im.size[1]
#         draw = ImageDraw.Draw(im)
          draw = ImageDraw.Draw(txt)





#Font name and size
          newpath = os.path.join(in_dir, font)
          arial = ImageFont.truetype(font =newpath+'.ttf',size = int(size_font))
          #arial = ImageFont.truetype(font+".ttf", 60)


          current_h, pad = (im.size[1]/float(height)), line_spacing # lower the number, lower it will move in the picture
          for line in para:
            w, h = draw.textsize(line, font=arial)
            draw.text(((MAX_W - w) / 2, current_h), line, font=arial,fill=final_color)
            current_h += h + pad
          im = Image.alpha_composite(im, txt)
          im.save(destination_folder+in_file+'_Cellno_'+str(i+1)+'_'+file.rpartition('.')[0]+'_text_written.png')
print('\n\nText successfuly written')
