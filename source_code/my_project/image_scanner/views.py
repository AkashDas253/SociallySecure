import base64
from io import BytesIO
from PIL import Image
from django.shortcuts import render
from .forms import ImageScanForm
from .utils import process_image  # Assuming the process_image function exists

def scan_image_view(request):
    if request.method == 'POST':
        form = ImageScanForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = form.cleaned_data['image']
            
            try:
                # Open the uploaded image using Pillow
                image = Image.open(image_file)

                # Check if the user is authenticated and retrieve their credentials
                if request.user.is_authenticated:
                    # Fetch credentials for matching
                    credentials = request.user.credentials.values_list('credential_value', flat=True)
                    matching_threshold = form.cleaned_data['match_threshold']
                else:
                    credentials = []  # Empty list if the user is not logged in
                    matching_threshold = 0  # Set threshold to 0 for guests

                # Process the image with or without credentials
                processed_image, extracted_text, matching_results = process_image(image, credentials, matching_threshold)

                # Initialize matched and unmatched words lists
                matched_words = []
                unmatched_words = []

                if request.user.is_authenticated:
                    # Separate matching and unmatched words based on the threshold
                    for word, result in matching_results.items():
                        if result["match_percentage"] > matching_threshold:
                            matched_words.append({
                                'found_word': word,
                                'credential': result["credential"],  # The credential that matched
                                'match_percentage': result["match_percentage"]
                            })
                        else:
                            unmatched_words.append(word)
                else:
                    # For guests, add all extracted text as unmatched
                    unmatched_words = extracted_text  # All extracted text for guests

                # Convert the processed image to base64 string
                buffer = BytesIO()
                processed_image.save(buffer, format="PNG")  # Save the processed image in PNG format
                img_str = base64.b64encode(buffer.getvalue()).decode()

                return render(request, 'image_scanner/result.html', {
                    'processed_image': img_str,  # Base64 string to display image in the template
                    'matched_words': matched_words,  # Words matching the credentials
                    'unmatched_words': unmatched_words,  # Words that did not match
                })

            except Exception as e:
                # Handle any exception during image processing
                return render(request, 'image_scanner/upload.html', {
                    'form': form,
                    'error': f'There was an error processing the image: {e}'
                })
    else:
        form = ImageScanForm()

    return render(request, 'image_scanner/upload.html', {'form': form})
