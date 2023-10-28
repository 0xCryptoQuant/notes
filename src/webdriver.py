from src.utils import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

# Create ChromeOptions object
chrome_options = Options()
# Set the headless option
chrome_options.add_argument("--headless")
user = 'solidquant'
url = f"https://medium.com/@{user}"

# Initialize the web driver (e.g., for Chrome)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Automatically scroll the page
scroll_pause_time = 2  # Pause between each scroll
screen_height = driver.execute_script("return window.screen.height;")  # Browser window height
print(f'screen_height is {screen_height}')
i = 1
while True:
    # Scroll down
    driver.execute_script(f"window.scrollTo(0, {screen_height * i});")
    i += 1
    time.sleep(scroll_pause_time)

    # Check if reaching the end of the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")
    if screen_height * i > scroll_height:
        break

# Get the page source after scrolling
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, "html.parser")

# Find and extract the links
article_links = []

for link in soup.find_all('a', class_='af ag ah ai aj ak al am an ao ap aq ar as at'):
    if link['href'] not in article_links \
    and ('?source=user_profile-' in link['href']):
        article_links.append(url+link['href'])

article_links = list(set(article_links))
keys = [ f'article_{i}'for i in range(len(article_links))]
values = sort_by(article_links, pattern=r'---(\d+)---')
data = dict(zip(keys, values))

file_path = f"article_user.json"
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)