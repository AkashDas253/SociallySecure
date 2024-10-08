from PIL import Image, ImageDraw
import pytesseract


# 1. Function to extract text from an image
def extract_text_from_image(image):
    """
    Extract text and their bounding box dimensions from an image.
    Returns a dictionary where keys are the extracted text and values are the bounding box info.
    """
    # Perform OCR on the image
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    
    extracted_text_dict = {}

    for i in range(len(data['text'])):
        text = data['text'][i].strip()
        if text:  # Ignore empty strings
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            # Store the text and the bounding box in a dictionary
            extracted_text_dict[text] = {'bounding_box': (x, y, w, h)}

    return extracted_text_dict



# 2. Function to find matching credentials
def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]

def find_matching_credentials(extracted_text, credentials):
    """Find matching credentials and calculate match percentage."""
    matching_results = {}

    for text in extracted_text:
        match_percentage = 0
        best_credential = None

        for credential in credentials:

            common_substring=longest_common_substring(text, credential)
            if common_substring:
                percentage = (len(common_substring) / len(text)) * 100
                if percentage > match_percentage:
                    match_percentage = percentage
                    best_credential = credential
        

        matching_results[text] = {
            "credential": best_credential,
            "match_percentage": match_percentage 
        }

    return matching_results


# 3. Function to draw bounding boxes on the image
def draw_bounding_boxes(image, extracted_text_dict, matching_results,match_threshold=50):
    """Draw bounding boxes around text in the image."""
    draw = ImageDraw.Draw(image)

    for text, data in extracted_text_dict.items():
        x, y, w, h = data['bounding_box']
        if matching_results[text]["match_percentage"] > match_threshold:
            # Red box for matching credentials
            draw.rectangle([(x, y), (x + w, y + h)], outline="red", width=3)
        else:
            # Green box for non-matching text
            draw.rectangle([(x, y), (x + w, y + h)], outline="green", width=2)

    return image



# 4. Combined function that performs all steps
def process_image(image, credentials,match_threshold_input=50):
    """Sequentially process the image to extract text, find matches, and draw boxes."""
    # Step 1: Extract text and bounding box info
    extracted_text_dict = extract_text_from_image(image)

    # Step 2: Find matching credentials
    extracted_text = list(extracted_text_dict.keys())  # Get the list of extracted text
    matching_results = find_matching_credentials(extracted_text, credentials)

    # Step 3: Draw bounding boxes on the image
    marked_image = draw_bounding_boxes(image, extracted_text_dict, matching_results, match_threshold_input)

    # Return marked image, list of text found, and matching results
    return marked_image, extracted_text, matching_results


