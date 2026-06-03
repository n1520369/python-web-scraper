import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    print("\nWebsite Title:")
    print(soup.title.string if soup.title else "No title found")

    print("\nFirst 10 Links:")
    links = soup.find_all("a")

    for i, link in enumerate(links[:10], start=1):
        href = link.get("href")
        print(f"{i}. {href}")

else:
    print("Failed to access website.")
