# Cars.com-Parser

Cars.com Parser
This repository contains a web scraping tool for extracting car listing data from Cars.com. The parser scrapes important details about vehicles, including make, model, year, price, manager contact, and outputs the data in a structured format suitable for further analysis.

# How to run:

In settings.py you have to provide valid proxies.
Also, in settings You can find variables to configure parser work. 

# Requirements:
1. Docker

# How to run:
```shell
docker-compose up --build
```

# Problems I faced:
   1. The site is blocked in Ukraine, so I use proxies to bypass this restriction.
   2. The site loads a lot of information dynamically and doesn't display all the data immediately after the page load. I found that the site stores JSON data in HTML tags and attributes. I use this feature to extract information without relying on traditional scraping.