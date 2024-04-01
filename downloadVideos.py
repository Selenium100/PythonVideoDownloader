import os
from pytube import Playlist
import logging

logging.basicConfig(level=logging.INFO)


def download_playlist(playlist_url, download_path, start_index=0):
    playlist = Playlist(playlist_url)
    logging.info(f"Downloading playlist: {playlist.title}")

    for index, video in enumerate(playlist.videos, start=1):
        if index < start_index:
            logging.info(f"{video.title} skipped")
            continue

        logging.info(f"Downloading: {video.title}")

        # Check if video already exists in download path
        video_filename = f"{video.title}.mp4"
        if os.path.exists(os.path.join(download_path, video_filename)):
            logging.info(f"{video.title} already exists, skipping download")
            continue

        try:
            stream = video.streams.get_highest_resolution()
            stream.download(download_path)
            logging.info(f"{video.title} downloaded successfully!!")
        except Exception as e:
            logging.error(f"Failed to download {video.title}: {str(e)}")


if __name__ == "__main__":
    playlist_url = r"https://www.youtube.com/playlist?list=PLu71SKxNbfoBuX3f4EOACle2y-tRC5Q37"
    download_path = r"D:\Javascript-ChaiCode-Videos"
    download_playlist(playlist_url, download_path)
