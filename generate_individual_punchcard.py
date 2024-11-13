import os
import sys
from PIL import Image

# Size of each Punch Card in pixels
PUNCHCARD_WIDTH, PUNCHCARD_HEIGHT = 1088, 638

def generate_individual_punchcards(num_punchcards):
    # Directory to save the individual Punch Cards images
    individual_output_dir = "individual_output"
    os.makedirs(individual_output_dir, exist_ok=True)

    # Load base image
    image_folder = "images"
    base_image_path = os.path.join(image_folder, "punchcard.png")
    base_image = Image.open(base_image_path).resize((PUNCHCARD_WIDTH, PUNCHCARD_HEIGHT), Image.Resampling.LANCZOS)

    # Generate Punch Cards without serial numbers and save as individual images
    for serial_number in range(1, num_punchcards + 1):
        output_path = os.path.join(individual_output_dir, f"PunchCard_{serial_number:04d}.png")
        base_image.save(output_path)
        print(f"Saved: {output_path}")

    print("Individual Punch Cards generation complete!")

if __name__ == "__main__":
    num_punchcards = int(sys.argv[1])
    generate_individual_punchcards(num_punchcards)
