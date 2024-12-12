import json
from src.scraper import scrape_youtube_videos
from src.sheet_manager import save_to_csv
from src.utils import setup_logging

def main():
    setup_logging()

    with open("config/config.json") as config_file:
        config = json.load(config_file)
    
    videos = scrape_youtube_videos(config["channel_url"])
    if videos:
        for video in videos:
            save_to_csv(video, config["output_file"])
        print(f"Saved {len(videos)} videos to {config['output_file']}.")

if __name__ == "__main__":
    main()