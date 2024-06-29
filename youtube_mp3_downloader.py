#!/usr/bin/env python3
# youtube_mp3_downloader.py

"""
Author: Drew Mayberry
Date: July 2024
Description: This script downloads the audio from a YouTube video and saves it as an MP3 file.
Version: 1.0
"""

import os
from pytube import YouTube

def download_audio_from_youtube(url, output_path='.'):
    """
    Downloads the audio from a YouTube video and saves it as an MP3 file.

    Args:
    url (str): The URL of the YouTube video.
    output_path (str): The directory where the MP3 file will be saved. Defaults to the current directory.
    """
    try:
        # Initialize the YouTube object
        yt = YouTube(url)
        
        # Filter the audio streams and select the first one
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Download the audio stream
        output_file = audio_stream.download(output_path=output_path)
        
        # Rename the downloaded file to have a .mp3 extension
        base, ext = os.path.splitext(output_file)
        new_file = base + '.mp3'
        os.rename(output_file, new_file)
        
        print(f"Downloaded and saved audio to {new_file}")

    except Exception as e:
        print("An error occurred:", e)

def main():
    """
    Main function to handle user input and initiate the download process.
    """
    # Prompt the user to enter the YouTube video URL
    print("Please enter the YouTube video URL:")
    video_url = input().strip()
    
    # Call the function to download audio
    download_audio_from_youtube(video_url)

if __name__ == "__main__":
    main()
