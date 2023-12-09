# from io import BytesIO

# from PIL import Image
# import numpy as np
# import requests
# import cv2


# def convertToGrayAPI(img):
#     API_ENDPOINT = "https://0f1qy8uvzl.execute-api.eu-north-1.amazonaws.com/dev"  # paste your endpoint here

#     is_success, im_buf_arr = cv2.imencode(".png", img)
#     byte_im = im_buf_arr.tobytes()

#     r = requests.post(url=API_ENDPOINT, data=byte_im)

#     img_ = Image.open(BytesIO(r.content))

#     return np.asarray(img_)


# def convertToGray(img):

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     return gray


# if __name__ == "__main__":

#     img_path = './cca.png'

#     img = cv2.imread(img_path)

#     img_gray = convertToGrayAPI(img)

#     cv2.imwrite('./abc.png', img_gray)

import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import requests
import numpy as np
import cv2
from io import BytesIO

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Converter")
        self.master.geometry("600x500")

        self.image_label = ttk.Label(self.master, text="Original Image")
        self.image_label.pack(pady=10)

        self.img_path = None
        self.img = None

        self.load_button = ttk.Button(self.master, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

        self.convert_button = ttk.Button(self.master, text="Convert to Grayscale", command=self.convert_to_gray)
        self.convert_button.pack(pady=10)

        self.save_button = ttk.Button(self.master, text="Save Grayscale Image", command=self.save_grayscale_image)
        self.save_button.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.img_path = file_path
            self.img = cv2.imread(self.img_path)
            self.display_image()

    def display_image(self):
        image_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(Image.fromarray(image_rgb))
        self.image_label.config(image=photo)
        self.image_label.image = photo

    def convert_to_gray(self):
        if self.img_path:
            img_array = self.convertToGrayAPI(self.img)
            self.img = img_array
            self.display_image()

    def save_grayscale_image(self):
        if self.img is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if save_path:
                cv2.imwrite(save_path, self.img)
                print("Grayscale image saved successfully.")

    def convertToGrayAPI(self, img):
        API_ENDPOINT = "https://0f1qy8uvzl.execute-api.eu-north-1.amazonaws.com/dev"  # replace with your API endpoint

        is_success, im_buf_arr = cv2.imencode(".png", img)
        byte_im = im_buf_arr.tobytes()

        r = requests.post(url=API_ENDPOINT, data=byte_im)

        img_ = Image.open(BytesIO(r.content))

        return np.asarray(img_)


if __name__ == "__main__":
    root = tk.Tk()
    # Use a themed style for a more modern look
    style = ttk.Style(root)
    style.theme_use("clam")
    
    app = ImageConverterApp(root)
    root.mainloop()
