import os
from PIL import Image

# Define the size of an A4 sheet in pixels at 300 DPI
A4_WIDTH, A4_HEIGHT = 2480, 3508

# Define the spacing between punch cards
COLUMN_SPACING = 10  # Space between columns
ROW_SPACING = 10     # Space between rows

def create_composite_images():
    # Directory to save the composite images
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Directory of individual Punch Cards images
    individual_output_dir = "individual_output"

    # Ensure the individual_output directory exists
    if not os.path.exists(individual_output_dir):
        raise FileNotFoundError(f"The directory '{individual_output_dir}' does not exist. Please run 'generate_individual_punchcard.py' first.")

    # Define the grid layout for Punch Cards on an A4 sheet
    cols = 2
    rows = 5

    # List all individual Punch Cards images in order
    individual_images = sorted(os.listdir(individual_output_dir))

    # Detect dimensions from the first image (assuming all images have the same dimensions)
    first_image_path = os.path.join(individual_output_dir, individual_images[0])
    first_image = Image.open(first_image_path)
    punchcard_width, punchcard_height = first_image.size

    # Calculate margins and spacing based on the detected dimensions
    total_punchcard_width = (cols * punchcard_width) + ((cols - 1) * COLUMN_SPACING)
    total_punchcard_height = (rows * punchcard_height) + ((rows - 1) * ROW_SPACING)

    margin_x = (A4_WIDTH - total_punchcard_width) // 2
    margin_y = (A4_HEIGHT - total_punchcard_height) // 2

    # Create composite images for printing
    page_number = 1
    pages = []
    for i in range(0, len(individual_images), cols * rows):
        for is_back in range(2):  # Duplicate each page for front and back
            sheet = Image.new("RGB", (A4_WIDTH, A4_HEIGHT), (255, 255, 255))  # Create a blank A4 page
            for j in range(cols * rows):
                if i + j >= len(individual_images):
                    break
                punchcard_path = os.path.join(individual_output_dir, individual_images[i + j])
                punchcard = Image.open(punchcard_path)
                
                # Calculate position
                x = margin_x + (j % cols) * (punchcard_width + COLUMN_SPACING)
                y = margin_y + (j // cols) * (punchcard_height + ROW_SPACING)
                
                # Ensure positions are integers
                x = int(x)
                y = int(y)
                
                sheet.paste(punchcard, (x, y))
            output_path = os.path.join(output_dir, f"PunchCards_Page_{page_number}_{'back' if is_back else 'front'}.png")
            sheet.save(output_path)
            pages.append(sheet)
            print(f"Saved: {output_path}")
            page_number += 1

    # Save all pages to a single PDF file
    if pages:
        pdf_path = os.path.join(output_dir, "PunchCards.pdf")
        pages[0].save(pdf_path, save_all=True, append_images=pages[1:])
        print(f"PDF saved: {pdf_path}")
    else:
        print("No pages were generated for the PDF.")

    print("Composite Punch Cards generation complete!")

if __name__ == "__main__":
    create_composite_images()
