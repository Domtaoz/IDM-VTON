import base64

# ใส่ path ของไฟล์รูป
image_path = "04743_00.jpg"

with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Prefix สำหรับ JPG
base64_str = "data:image/jpeg;base64," + encoded_string

print(base64_str)
