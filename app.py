import streamlit as st
import pytube
from pytube import Playlist
import os

# Define function to download playlist
def download_playlist(playlist_url, save_path):
    # Create playlist object
    playlist = Playlist(playlist_url)

    # Print playlist details
    st.write("Downloading playlist: ", playlist.title)
    st.write("Number of videos in playlist: ", len(playlist.video_urls))

    # Download each video in playlist
    for url in playlist.video_urls:
        # Create video object
        video = pytube.YouTube(url)

        # Get highest resolution stream
        stream = video.streams.get_highest_resolution()

        # Download video
        st.write("Downloading video: ", video.title)
        stream.download(output_path=save_path)
        st.write("Download complete!")

# Define Streamlit app
def app():
    st.set_page_config(page_title="YouTube Playlist Downloader")

    # Set app title and description
    st.title("YouTube Playlist Downloader")
    st.write("Enter the URL of the YouTube playlist you want to download:")
    
    # Get playlist URL from user
    playlist_url = st.text_input("Playlist URL")
    
    # Get save directory from user
    save_dir = st.text_input("Save directory")

    # Download playlist when user clicks button
    if st.button("Download Playlist"):
        download_playlist(playlist_url, save_dir)

if __name__ == "__main__":
    app()
