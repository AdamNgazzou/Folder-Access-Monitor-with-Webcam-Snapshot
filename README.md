# Folder Access Monitor with Webcam Snapshot

This repository contains a Python script that monitors a specified folder for access. When the folder is accessed, the script automatically takes a snapshot using the connected webcam and saves the image to a predefined folder.

## Features

- Monitors a folder for any access (file modifications or opening).
- Takes a snapshot using the webcam when the folder is accessed.
- Saves the photo with a timestamp in a specific directory.
- The script can be set to run automatically when the system starts.

## Prerequisites

- Python 3.x installed.
- OpenCV library installed. If it's not installed, you can install it using pip:

```bash
pip install opencv-python
