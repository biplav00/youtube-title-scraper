from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import logging

def scrape_youtube_videos(channel_url):
    options = Options()
    options.add_argument("--headless") 
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(), options=options)

    try:
        logging.info(f"Opening URL: {channel_url}")
        driver.get(channel_url)
        time.sleep(5) 

        logging.info("|------Scrolling to the last page-------|")
        
        scroll_pause_time = 2
        last_height = driver.execute_script("return document.documentElement.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(scroll_pause_time)
            new_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        
        logging.info("|------Extracting video elements-------|")
        video_elements = driver.find_elements(By.XPATH, "(//div[@id='content']//ytd-rich-grid-media)")
        videos = []
        title_index = 1
        views_index = 1
        logging.info("|------Extracting video title and views-------|")
        for video in video_elements:
            try:
                title = video.find_element(By.XPATH, f"(//yt-formatted-string[@id='video-title'])[{title_index}]").text
                views = video.find_element(By.XPATH, f"(//span[contains(@class,'inline-metadata-item style-scope')])[{views_index}]").text
                logging.info(f"SN: {title_index} Title: {title}, Views: {views}")
                videos.append({"sn": title_index, "title": title, "views": views})
            except Exception as e:
                logging.warning(f"Error extracting video details: {e}")
            title_index+=1
            views_index+=2
        logging.info(f"Extracted {len(videos)} videos.")
        return videos

    except Exception as e:
        logging.error(f"Error scraping YouTube videos: {e}")
        return []

    finally:
        driver.quit()