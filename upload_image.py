from load_env import configure_genai # import configure_genai from load_env.py


genai = configure_genai()

image_path = "images/pink_vader.jpg"

image_upload = genai.upload_file(path=image_path, display_name="Pink Vader")    # file upload

print(f"Uploaded file '{image_upload.display_name}' as: {image_upload.uri}")

file = genai.get_file(name=image_upload.name)   # file retrieval
print(f"Retrieved file '{file.display_name}' from: {file.uri}")