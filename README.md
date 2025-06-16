# Background Remover Streamlit App

This is a simple Streamlit web application that allows users to upload an image, automatically removes its background, and replaces it with a solid **white** background. The app displays both the original and processed images side by side and provides a download option for the result.

## Features

* Upload images in PNG, JPG, or JPEG format
* Automatic background removal using the `rembg` library
* Replaces transparent background with **white**
* Displays before and after images
* Download the processed image in PNG format

## Installation

### 1. Clone the Repository

```bash
git clone git@github.com:lumedrano/ImageBackgroundRemover.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install individually:

```bash
pip install streamlit rembg pillow
```

## Running the App

```bash
cd runScripts
streamlit run app.py
```

## Project Structure

```
background-remover-app/
├── app.py                # Main Streamlit app
└── requirements.txt      # Python dependencies
```

## Example

1. Upload your image (PNG/JPG/JPEG)
2. View the original and processed versions side by side
3. Click **Download Image** to save the result

## Requirements

* Python 3.7+
* rembg
* Pillow
* streamlit

## License

This project is licensed under the MIT License.

## Credits

* [rembg](https://github.com/danielgatis/rembg) for background removal
* Developed with ❤️ using Streamlit

## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
