import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.amazon.in/s?i=watches&bbn=2563505031&rh=n%3A1350387031%2Cn%3A%211350388031%2Cn%3A2563505031%2Cp_85%3A10440599031&lo=image&field-pct-off-with-tax=40-&ref=mega_sv_s23_7_3_1_1"
# uReq(my_url)

# open
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
# print(page_html)
page_soup = soup(page_html, "html.parser")
# print(page_soup.h1)
containers = page_soup.findAll("div", {"class": "s-expand-height s-include-content-margin"}).getText()
print(len(containers))
print(containers)
