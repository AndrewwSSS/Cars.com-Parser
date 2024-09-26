# Cars.com-Parser

Python script that parse cars and seller's contact from site cars.com

# How to run:

In settings by you have to provide valid proxies.
Also, in settings.py You can find settings to configure parser work. 

```shell
python -m venv venv
```

for unix systems:
```shell
source venv/bin/activate
```

for windows systems:
```shell
venv/Scripts/activate
```

```shell
pip install -r requirements.txt
python main.py
```

# Problems I faced:
   1. The site is blocked in Ukraine, so I use proxies to bypass this restriction.
   2. The site loads a lot of information dynamically and doesn't display all the data immediately after the page load. I found that the site stores JSON data in HTML tags and attributes. I use this feature to extract information without relying on traditional scraping.