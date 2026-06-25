
from rembg import remove  # type: ignore

""" 
input_path = "module_5/input_image.jpg"
output_path = "module_5/output_image.png"

with open(input_path, "rb") as i:
    with open(output_path, "wb") as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)

print("Background removed successfully")

"""


input_path = "module_5/lion.jpg"
output_path = "module_5/lion.png"

with open(input_path, "rb") as i:
    with open(output_path, "wb") as o:
        input_data = i.read()
        output_data = remove(input_data)
        o.write(output_data)

print("Background removed successfully")


#.\.venv\Scripts\python.exe module_5\input_image.py     ===> to run the script