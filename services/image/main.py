
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

project_id = "sascha-playground-doit"
prompt = "generate a hotdog"
output_file = "temp_recipe.png"

vertexai.init(project=project_id, location="us-central1")

model = ImageGenerationModel.from_pretrained("imagegeneration@006")

images = model.generate_images(
    prompt=prompt,
    # Optional parameters
    number_of_images=4,
    language="en",
    # You can't use a seed value and watermark at the same time.
    # add_watermark=False,
    # seed=100,
    aspect_ratio="16:9",
    safety_filter_level="block_some",
    #person_generation="allow_adult",
)

print(images)

images[0].save(location=output_file, include_generation_parameters=False)

# Optional. View the generated image in a notebook.
# images[0].show()

print(f"Created output image using {len(images[0]._image_bytes)} bytes")