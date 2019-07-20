from bs4 import BeautifulSoup
import re
import requests
import time

def snapdealparser(url):
    time.sleep(2)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    response = requests.get(url, headers=headers)
    output = []

    htmltext = response.text
    soup = BeautifulSoup(htmltext,'html.parser')
    name = soup.findAll('img',{'class':"cloudzoom"})[0].get('title')
    price = soup.find('span',{'class':"payBlkBig"})
    rating = soup.find('span',{'class':"avrg-rating"})
    photo = soup.findAll('img',{'class':"cloudzoom"})[0].get('src')
    link = url
    if name:
        output.append(name)
    else :
        output.append('N/A')
            
    if price:
        output.append(price.text)
    else :
        output.append('N/A')
        
    if rating:
        output.append(rating.text)
    else :
        output.append('N/A')
    if photo:
        output.append(photo)
    else:
        output.append("N/A")
    output.append(link)
    return output


def getproductid():

    print("Enter item to be searched\n")
    query = input()
    url = "https://www.snapdeal.com/search?keyword=" + query.lower()
    print("Searching your product at...",url,sep=" ")
    htmltext = requests.get(url).text
    time.sleep(2)
    pattern = re.compile(r"/product/.*/\d{12,12}")  #Snapdeal product id
    List = re.findall(pattern,htmltext)
    
    List = list(set(List))
    
    return List
    
def ReadAsin():
    
    Id = getproductid()
    extracted_data = []
    ctr=0
    for i in Id:
        ctr +=1
        
        url = "https://www.snapdeal.com"+i
        print ("Processing: "+url)
        extracted_data.append(snapdealparser(url))
        if(ctr==5):
            break
        time.sleep(1)
    for i in extracted_data:
        print(i)
        print()
        
        
 
if __name__ == "__main__":
    ReadAsin()

	
