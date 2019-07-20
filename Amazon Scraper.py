from bs4 import BeautifulSoup
import re
import requests
import time

def amazonparser(url):
    time.sleep(2)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    response = requests.get(url, headers=headers)
    output = []

    htmltext = response.text
    soup = BeautifulSoup(htmltext,'html.parser')
    brand = soup.find('a',{'id':"bylineInfo"})
    name = soup.findAll('img',{'id':"landingImage"})[0].get('alt')
    price = soup.find('span',{'id':"priceblock_ourprice"})
    rating = soup.find('span',{'id':"a-icon-alt"})
    photo = soup.findAll('img',{'id':"landingImage"})[0].get('data-a-dynamic-image').split('"')[1]
    
    link = url
    if brand:
        output.append(brand.text)
    else :
        output.append('N/A')
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
    url = "https://www.amazon.in/s?k=" + query.lower()
    print("Searching your product at...",url,sep=" ")
    htmltext = requests.get(url).text
    time.sleep(1) 
    pattern =  re.compile(r"/dp/[0-9A-Z]{10,10}")  #amazon product id
    List = re.findall(pattern,htmltext)
    time.sleep(1)
    List = list(set(List))
    return List
    
def ReadAsin():
    
    Id = getproductid()
    extracted_data = []
    ctr=0
    for i in Id:
        ctr +=1
        
        url = "http://www.amazon.in"+i
        print ("Processing: "+url)
        extracted_data.append(amazonparser(url))
        if(ctr==5):
            break
        time.sleep(1)
    for i in extracted_data:
        print(i)
        print()
        
        
 
if __name__ == "__main__":
    ReadAsin()

	
