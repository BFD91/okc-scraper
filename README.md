# okc-scraper
Bot capabale of scraping online dating site OKCupid (https://www.okcupid.com/) for profile info (including profile text and pictures) and scoring profiles using a list of keywords and match percentage. Also swipes profiles depending on the score. Helped me find my wife; hope it may serve others. :) 

## OBS: 
The bot was written and last tested in July 2020, and due to regular changes of the OKC site, it is likely modification will be required for the code to run; the current code should be regarded as a template. I expect one will get far by prolifically applying the find_element_by_xpath method to components of the website that one needs to access. You can find the xpath by right clicking on the website component you want to access, inspect, right click on the highlighted line, copy, copy full xpath.

Requires the selenium package and chromium webdriver.
