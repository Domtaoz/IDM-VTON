import base64, os

# ใส่ path ของไฟล์รูป
image_path = "C:\\IDM-VTON\\IDM-VTON\\gradio_demo\\image.jpg"

if not os.path.exists(image_path):
    print("หาไฟล์ไม่เจอ:", image_path)
else:
    print("เจอไฟล์แล้ว:", image_path)

with open(image_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Prefix สำหรับ JPG
base64_str = "data:image/jpeg;base64," + encoded_string

# print(base64_str)

with open("output.txt", "w") as out:
    out.write(base64_str)

print("Base64 string saved to output_base64.txt")