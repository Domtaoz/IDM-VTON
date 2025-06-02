import requests
import base64

with open("C:\IDM-VTON\IDM-VTON\gradio_demo\image.jpg", "rb") as f:
    b64 = base64.b64encode(f.read()).decode()
data = {
    "data": [f"data:image/png;base64,{b64}"]
}

url = "https://8d8a3e7269afc79d53.gradio.live/api/test" # ใส่ URL จริง
r = requests.post(url, json=data, headers={"Content-Type": "application/json"})
print(r.status_code)
print(r.json())
