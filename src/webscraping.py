import requests
from bs4 import BeautifulSoup

url = "https://xthemadgenius.medium.com"

response = requests.get(url)
article_links = []
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Modify the selectors based on the HTML structure of the page
    for link in soup.find_all('a', class_='af ag ah ai aj ak al am an ao ap aq ar as at'):
        if link['href'] not in article_links \
        and ('medium.com' not in link['href']) \
        and ('?source=user_profile-' in link['href']):
            article_links.append(link['href'])

else:
    print(f"Failed to retrieve the author's page. Status code: {response.status_code}")

print(f'article links are {article_links}')