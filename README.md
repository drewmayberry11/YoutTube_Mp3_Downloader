
# YouTube MP3 Downloader

## Download music for free from youtube links.

### Description
This script downloads the music/audio from a YouTube video and saves it as an MP3 file. It is useful for extracting music from YouTube videos for offline listening.

### Requirements
- Python 3.6 or higher
- pytube library

### Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/drewmayberry11/YoutTube_Mp3_Downloader.git
   cd youtube_mp3_downloader
   ```

2. **Install Required Packages**
   ```sh
   pip install pytube
   ```

### Usage
1. **Run the Script**
   ```sh
   python3 youtube_mp3_downloader.py
   ```

2. **Enter the YouTube Video URL**
   When prompted, enter the URL of the YouTube video you want to download the audio from.

### Example
```sh
$ python3 youtube_mp3_downloader.py
Please enter the YouTube video URL:
https://www.youtube.com/watch?v=example
Downloaded and saved audio to ./example.mp3
```

### Script Details
- **download_audio_from_youtube(url, output_path='.')**
  - Downloads the audio from a YouTube video and saves it as an MP3 file.
  - **Args:**
    - `url` (str): The URL of the YouTube video.
    - `output_path` (str): The directory where the MP3 file will be saved. Defaults to the current directory.
    
- **main()**
  - Main function to handle user input and initiate the download process.

### Error Handling
The script includes basic error handling to catch and print errors that may occur during the download process.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request.


---

Enjoy using the YouTube MP3 Downloader!
