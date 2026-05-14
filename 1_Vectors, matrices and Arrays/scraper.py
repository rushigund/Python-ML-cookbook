from bs4 import BeautifulSoup
import os
import requests







#soup = BeautifulSoup(open(os.path.join(main_folder, file_name)), 'html.parser')

def scraper():
    URL = "https://www.pexels.com/search/4k%20wallpaper/"
    #main_folder = os.path.dirname(os.path.abspath(__file__))
    main_folder = os.mkdir("images_folder")
    print(f"{main_folder} has been created")   
  #  parent_folder = os.path.dirname(main_folder)
   # file_names = 

    while True:
        try:
            response = requests.get(URL)
            if response.status_code == 200: 
                soup = BeautifulSoup(response.text, 'html.parser')
                #images = soup.find_all('img')[]
                for img in images:
                    img_url = img['src']
                    img_data = requests.get(img_url).content
                    img_name = os.path.join(main_folder, 'images', os.path.basename(img_url))
                    with open(img_name, 'wb') as handler:
                        handler.write(img_data)
        except Exception as e:
            print(f"Error occurred: {e}. Retrying...")

if __name__ =='__main__':
    scraper()