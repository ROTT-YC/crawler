from PIL import Image, ImageFont, ImageDraw
import textwrap

# Different text on same pic
def draw_text(img_path, wm_text):
    img = Image.open("/pic/img_path")
    img = img.convert('RGB')
    W, H = img.size
    font = ImageFont.truetype(font="/font/font_type.ttf", size=70)
    draw = ImageDraw.Draw(img)
    txt = "\n".join(textwrap.wrap(wm_text,26))
    draw.text((W/8, H/3.5), txt, fill='red', font=font, stroke_width=3, stroke_fill='white')
    img.save(img_path)

    # # Word wrap
    # font_size = 50
    # txt = "\n".join(textwrap.wrap(wm_text,22)).split("\n")
    # for i in range(len(txt)):
    #     w = len(txt[i])*font_size
    #     draw.text((450, 180 + i * 58), txt[i], fill='white', font=font)

def draw_icon(img_path, wm_num):
    dict_data = {"1": "/pic/icon_1.png",
                 "2": "/pic/icon_2.png",
                 "4": "/pic/icon_4.png"}
    img = Image.open(img_path)
    icon = Image.open(dict_data[wm_num])

    img_w, img_h = img.size
    icon_w, icon_h = icon.size
    x = int((img_w-icon_w)) # The lower right corner
    y = int((img_h-icon_h))  

    img.paste(icon, (x, y), icon)
    img.save(img_path)