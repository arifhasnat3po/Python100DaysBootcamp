from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
soup.title
print(soup.title)


first_title_link = soup.find('span', class_='titleline')
title_text = first_title_link.get_text(strip=True)
print(title_text)
# print(first_title_link)
article_link = first_title_link.a['href']
article_upvote = soup.find('span', class_='score')
print(article_link)
print(article_upvote.get_text(strip=True))

title_spans = soup.find_all('span', class_='titleline')
for first_title_link in title_spans:
    # Extract and print the title
    title_text = first_title_link.a.get_text(strip=True)
    print("Title:", title_text)

    # Extract and print the link
    article_link = first_title_link.a['href']
    print("Link:", article_link)

    # article_upvote = first_title_link.find_next('span', class_='score')
    # upvotes = article_upvote.get_text(strip=True)
    # print(int(upvotes.split()[0]))
    # print(upvotes)

    # print("\n")  
article_upvote = [int(score.get_text(strip= True).split()[0]) for score in soup.find_all('span', class_='score')]
print(article_upvote)
article_upvote_max = max (article_upvote)
print(article_upvote_max)

if article_upvote_max in article_upvote:
    print(title_text)
    print(article_link)

# print(article_link[article_upvote_max])

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')

#     title_spans = soup.find_all('span', class_='titleline')

#     for title_span in title_spans:
#         title_text = title_span.a.get_text(strip=True)
#         url = title_span.a['href']
#         print(f"Title: {title_text}\nURL: {url}\n")
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

                

































# with open("website.html", "r", encoding="utf-8") as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.find_all( name="a"))
# all_anchor_tag = soup.find_all( name="a")

# for tag in all_anchor_tag:
#     print(tag)
#     print(tag["href"])
#     print(tag.getText())
#     print(tag.get("href"))
    
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)


# heading = soup.select(".heading")
# print(heading)