import requests
import base64

# ใส่ path รูปของคุณ (เช่นที่เพิ่ง upload)
IMAGE_PATH = r"C:\IDM-VTON\IDM-VTON\gradio_demo\image.jpg"

# แปลงไฟล์เป็น base64 string
with open(IMAGE_PATH, "rb") as f:
    b64_image = base64.b64encode(f.read()).decode()

# สร้าง payload ตาม format Gradio ต้องการ
data = {
    "data": [            
        f"data:image/jpeg;base64,{b64_image}"  # <== base64 image
    ]
}

# ใส่ Gradio API URL ที่ได้จากการรัน demo
GRADIO_API_URL = "https://4b4cf2f9f258aab4d2.gradio.live/api/test"  # ตัวอย่าง

headers = {"Content-Type": "application/json"}

# ส่ง POST request
response = requests.post(GRADIO_API_URL, json=data, headers=headers)

# แสดงผลลัพธ์
print("Status code:", response.status_code)
try:
    print("Response:", response.json())
except Exception:
    print("Response (raw):", response.text)

# ถ้า output เป็นรูป base64 ก็สามารถบันทึกกลับเป็นไฟล์ได้แบบนี้
if response.status_code == 200:
    result = response.json()
    if result["data"] and result["data"][0].startswith("data:image"):
        out_b64 = result["data"][0].split(",")[1]
        with open("output_image.png", "wb") as f:
            f.write(base64.b64decode(out_b64))
        print("บันทึก output_image.png สำเร็จ")
