import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://dsmonline.in/"
visited = set()  # To keep track of visited URLs
data = []  # To store scraped content


def scrape_page(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve {url}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        print(f"Scraping: {url}")

        # Extract and store desired content (e.g., text from paragraphs)
        page_content = soup.get_text(separator="\n")
        data.append({"url": url, "content": page_content})

        # Find all internal links
        for a_tag in soup.find_all("a", href=True):
            link = urljoin(base_url, a_tag['href'])
            if link.startswith(base_url) and link not in visited:
                visited.add(link)
                scrape_page(link)  # Recursive call to scrape the linked page

    except Exception as e:
        print(f"Error scraping {url}: {e}")


# Start scraping from the homepage
scrape_page(base_url)

# Save the scraped data to a file
with open("oriental_website_data.txt", "w", encoding="utf-8") as file:
    for entry in data:
        file.write(f"URL: {entry['url']}\n")
        file.write(f"Content:\n{entry['content']}\n")
        file.write("-" * 80 + "\n")

print("Scraping complete. Data saved to 'oriental_website_data.txt'")