# Background Remover Streamlit App

A simple yet powerful Streamlit web application that allows users to upload an image, automatically remove its background, and replace it with a custom background. Users can preview the result, customize output options, and download the processed image.

## Features

* Upload images in PNG, JPG, or JPEG format
* Automatic background removal using the `rembg` library (powered by AI)
* Custom background color selection (default: white)
* Optional padding around the image
* Resize the output image to custom dimensions
* Choose download format: PNG or JPG
* Preview transparent (checkerboard) or final image
* Download the processed image
* Simple, user-friendly interface with advanced controls

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/lumedrano/ImageBackgroundRemover.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit rembg pillow
```

## Running the App

```bash
cd runScripts
streamlit run app.py
```

Then open the provided local URL in your browser.

## Project Structure

```
background-remover-app/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Example Workflow

1. Upload your image (PNG, JPG, or JPEG)
2. Select background color (default is white)
3. (Optional) Adjust padding or resize image
4. Preview both original and processed images
5. Download your customized output

## Requirements

* Python 3.7+
* rembg
* pillow
* streamlit

## License

This project is licensed under the MIT License.

## Credits

* [rembg](https://github.com/danielgatis/rembg) for the background removal engine
* Built with ❤️ using Streamlit

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss your proposed changes.

