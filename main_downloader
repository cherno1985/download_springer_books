import pandas as pd
import os
import requests
from bs4 import BeautifulSoup

BASE_PDF = r'https://link.springer.com/content/pdf/10.1007'


def file_reader(file_loc_and_name):
  #Not that the file should have 4 columns - Book Title|	Author|	English Package Name|	OpenURL
  df = pd.read_excel(file_loc_and_name)
  
  return df


def save_pdfs(cols):
    
    if f"{field} - {author} - {title}.pdf" in os.getcwd():
        print('Got it!')
    else:
        title = cols[0]
        author = cols[1]
        field = cols[2]
        first_url = cols[3]
        try:
            r=requests.get(first_url)
            soup = BeautifulSoup(r.text, 'lxml')
            suff_ = '%' +soup.find_all('a', {'title':'Download this book in PDF format'})[0].get('href').split("%")[1]

            new_url = BASE_PDF+suff_
            f = requests.get(new_url)

            print(f"Saving {field} - {author} - {title}")
            with open(f"{field} - {author} - {title}.pdf", 'wb') as pdf:
                pdf.write(f.content)

            print(f"Done with {field} - {author} - {title}")

            return 'Done'

        except Exception as e:
            print(e)
            return f'Error - {e}'


if __name__ == '__main__':


  file_loc_and_name = input('Enter the file+file location:\n')
  file_read = file_reader(file_loc_and_name)
  file_read['status'] = df.apply(save_pdfs, axis=1)
  
  file_read.to_excel(f'{file_loc_and_name} - status.xlsx', index=False)

