from PIL import Image
from pytesseract import pytesseract

def auto(image_file: str, x_crop: int = 5, y_crop: int = 5) -> str:
    img = Image.open(image_file)    
    img_wid, img_len = img.size

    # minimizes unncessary borders from inputted picture
    crop_img = img.crop((5, 5, img_wid - x_crop, img_len - y_crop)) 
    crop_img.save("optimized.png")

    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = "optimized.png"

    # read image
    main_img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(main_img)

    # last character is glitched
    return text[:-1]

print(auto("unknown.png", 5, 5))
