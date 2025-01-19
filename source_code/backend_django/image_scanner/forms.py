from django import forms

class ImageScanForm(forms.Form):
    image = forms.ImageField(label='Upload an Image')
    
    # Slider to specify the match percentage
    match_threshold = forms.IntegerField(
        label='Match Threshold (%)',
        initial=50,
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'type': 'range', 'oninput': "this.nextElementSibling.value = this.value"})
    )
