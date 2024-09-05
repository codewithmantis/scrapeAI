import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching web browser")
    
    chrome_driver_path = "./chromedriver.exe"
    
    # Setup Chrome options for headless mode
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--window-size=1920x1080")  # Set the window size

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    
    try:
        driver.get(website)
        print("Page loaded..")
        
        html = driver.page_source
        time.sleep(5)  # Adjust the sleep time as needed
        soup = BeautifulSoup(html, 'html.parser')

        tags_to_extract = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']
        extracted_texts = []
        
        for tag in tags_to_extract:
            elements = soup.find_all(tag)
            for element in elements:
                extracted_texts.append(element.get_text())
        
        # Combine extracted texts
        final = ' '.join(text.strip() for text in extracted_texts if text.strip())
        return final.replace('.', '. ')
    finally:
        driver.quit()
