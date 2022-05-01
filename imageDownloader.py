import requests
import os.path #merging, normalizing and retrieving path names in python
# **********************************************************************
# By Mikhailgov Lmao 2022-04-28
# bad image downloader that relies on external libaries
# **********************************************************************

# TODO add better error handling/messages instead of sys exits and defult images

class GetSource:
    """downloads image file to a predetermined save path by passing in an image url"""
    
    def __init__(self,url:str,save_path:str):
        self.url = url
        self.path = save_path
        
    def save_img(self):
        """saves the image using request module"""
        
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36'}
        try:
            src = requests.get(self.url, headers=header) #sends request for img with custom user agent 
            session_header = src.headers
            
            if session_header['Content-Type'] not in('image/jpeg', 'image/png'): #if an image is not passed in redirect to a 404.png
                src = requests.get('https://i.stack.imgur.com/6M513.png', headers=header)
            
            src_name = src.url #gets url plaintext
            src_name = src_name.split('/')[-1]
            src_wpath = os.path.join(self.path, src_name) 
        
            with open (src_wpath, 'wb') as img_file:
                img_file.write(src.content) #wrties content(binary) of the image file from requests
                
        except requests.exceptions.RequestException as e:  # raise an error for connection issues
            raise SystemExit(e) #abort program while prinitng an error to terminal
