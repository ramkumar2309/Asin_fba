import urllib3
from bs4 import BeautifulSoup
import requests

r  = requests.get('https://browse-query-editor-na.aka.amazon.com/?browseNodeFilter=category-node-merchant-facing&catalogAttributes=title&marketplaceId=1&pageSize=5&retailAsins=N&showImages=Y&useSuggestedBrowseNode=N&userQuery=%5Bpackage_weight.pounds%3A-10%5D&variationParentOnly=N&websiteSearchable=N',verify=False)

data = r.text

soup = BeautifulSoup(data,features='html.parser')
print(soup.title)

for link in soup.find_all('a'):
    print(link.get('href'))