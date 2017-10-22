import urllib.request
req = urllib.request.urlopen('http://www.google.com')
data = req.read()

urllib.request.urlretrieve('https://static.pexels.com/photos/302892/pexels-photo-302892.jpeg',
        '/home/hnr/web/python-scraper/dl/pic.jpg')
