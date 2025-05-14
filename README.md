# Google Image Scraper

This is a Python script that uses **Selenium** and **Pillow** to scrape and download images from Google based on a search term. It is particularly useful for collecting sample images for machine learning, research, or personal projects.

---

## 📦 Features

- Automatically opens Google and searches for images.
- Extracts up to 11 images related to the search term.
- Handles both base64-encoded images and standard image URLs.
- Saves the images as `.jpeg` files in the specified folder.

---

## 🛠 Requirements

- Python 3.6+
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (make sure it's in your system PATH)

### Python packages:
Install them via pip:
```bash
pip install selenium requests pillow
