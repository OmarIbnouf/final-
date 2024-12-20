import openai
import config  # This file contains the API key
import base64

# Set up your API key
openai.api_key = config.OPENAI_API_KEY

# Generate an image using the updated OpenAI API
response = openai.Image.create(
    prompt="A white Siamese cat, high-definition, photorealistic",
    n=1,  # Number of images to generate
    size="1792x1024",  # Image resolution
    response_format="b64_json"  # Base64-encoded JSON
)

# Extract the base64-encoded image
image_data = response["data"][0]["b64_json"]

# Decode the image and save it locally
output_file = "white_siamese_cat.png"
with open(output_file, "wb") as f:
    f.write(base64.b64decode(image_data))

print(f"Image saved successfully as {output_file}.")

