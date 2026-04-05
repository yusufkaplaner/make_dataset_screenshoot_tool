# Screen Dataset Collector

A simple Python tool to quickly collect image datasets by taking screenshots of a selected region.

##  Features

* Select any area on screen
* Capture images with a hotkey (F8)
* Reset selection anytime (F9)
* Automatically saves images in sequence
* Perfect for creating ML datasets

##  Installation

```bash
git clone https://github.com/yourusername/screen-dataset-collector.git
cd screen-dataset-collector
pip install -r requirements.txt
```

##  Usage

```bash
python main.py
```

### Controls:

* **F8** → Take screenshot
* **F9** → Reset selection
* **ESC** → Exit

##  Output

Images are saved in:

```
/togg_dataset/    
```

Example:

```
togg_t10x_0001.jpg
togg_t10x_0002.jpg
```

##  Use Cases

* Object detection datasets
* AI training data collection
* Web scraping via screenshots
* Game data collection

##  Notes

* Make sure the target object is visible on screen
* Works best with consistent positioning

##  Future Improvements

* Auto-labeling support
* YOLO format export
* Bounding box saving
* Multi-class support

##  Author

Developed by [YusufKaplaner]

---

⭐ Star the repo if you find it useful!
