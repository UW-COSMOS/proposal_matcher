from PIL import ImageDraw, Image
from xml_utils import parse_xml
gt_color = "#00f"
pred_color = "#0f0"
corrected_color = "#f00"

def get_rectangles(xml_path):
    classes, x1, y1, x2, y2 = parse_xml(xml_path)
    return zip(classes, x1, y1, x2,y2)

def get_center(x1, y1, x2, y2):
    x = (x1 +x2)/2
    y = (y1+y2)/2
    return x, y

def draw_xml(img, xml_path, color):
    draw = ImageDraw.Draw(img)
    data = get_rectangles(xml_path)
    for obj in data:
        cls, x1, y1, x2, y2 = obj
        draw.rectangle((x1, y1, x2, y2), fill=None, outline=color)
        cx, cy = get_center(x1, y1, x2, y2)
        draw.text((cx, cy), cls, fill=color)


def draw(img_path, pred_path, gt_path, corrected_path, out_path):
    im = Image.open(img_path)
    #draw_xml(im, pred_path, pred_color)
    # draw_xml(im, gt_path, gt_color)
    draw_xml(im, corrected_path, corrected_color)
    im.save(out_path, "PNG")
