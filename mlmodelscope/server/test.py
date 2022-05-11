import requests


ray_logo_bytes = requests.get(
    "https://github.com/ray-project/ray/raw/"
    "master/doc/source/images/ray_header_logo.png"
).content

resp = requests.post(
    "http://localhost:8000/image_predict",
    data=ray_logo_bytes
)
print(resp.json())
