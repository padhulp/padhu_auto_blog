import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from html import escape
import os

load_dotenv()
# Replace with your site URL, username, and application password
site_url = os.getenv('SITE_URL')
username = os.getenv('USER_NAME')
application_password = os.getenv('APPLICATION_PASSWORD')
category_id = 41  # Replace with your category ID

# Read content from the file
file_path = "./logs/blog_post.html"
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Use BeautifulSoup to parse the HTML and convert it to plain text
soup = BeautifulSoup(html_content, 'html.parser')
plain_text_content = soup.get_text()

# Alternatively, if you want to keep some basic HTML formatting:
basic_html_content = ''.join(str(tag) for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'ul', 'ol', 'li', 'strong', 'em', 'a']))

escaped_content = escape(html_content)

#allowed_tags = ['p', 'h1', 'h2', 'h3', 'ul', 'ol', 'li', 'strong', 'em', 'a']
#cleaned_content = ''.join(str(tag) for tag in soup.find_all(allowed_tags))

for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
        text = soup.get_text()
    # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
        style_removed_content = '\n'.join(chunk for chunk in chunks if chunk)



# Convert the cleaned soup object back to a string
cleaned_html_content = str(soup)

h1_tag = soup.find('h1')
title = h1_tag.get_text() if h1_tag else 'My Blog Post'

class_name = 'personal-message'
elements= soup.find_all(class_=class_name)

for element in elements:
     blog_post_title = element.get_text(strip=True)

allowed_tags = ['p', 'h1', 'h2', 'h3', 'strong', 'em', 'a']
cleaned_content = ''.join(str(tag) for tag in soup.find_all(allowed_tags))

paragraphs = soup.find_all('p')
for p in paragraphs:
    para_content = p.get_text()


# Post data
post_data = {
    'title': blog_post_title,
    'content': cleaned_content,
    'status': 'publish',
    'categories': [category_id]
}

headers = {
    'Authorization': f'Basic {username}:{application_password}',
    'Content-Type': 'application/json'
}
# Create the post
response = requests.post(
    f"{site_url}/wp-json/wp/v2/posts",
    auth=HTTPBasicAuth(username, application_password),
    headers={'Content-Type': 'application/json'},
    json=post_data
)
response.raise_for_status()  # Check for errors
post = response.json()

print(f"Post created: {post['link']}")
