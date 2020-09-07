# SPAWebScrapers
A web scraping project I undertook to help with my work as a Student Project Assistant at McGill Libraries in thier Digital Initiatives branch.

##Libraries used
* BeautifulSoup
```bash
pip install beautifulsoup4
```
* xlwings
```bash
pip install xlwings
```
* requests
```bash
pip install requests
```

##Sherpa Scraper
file name: SherpaScraper.py  

Script for a personal UDF for Excel.  

This is a scraper created to scrape embargo, 
ISSN and publication information from the [sherpa/romeo](http://sherpa.ac.uk/romeo/index.php)
website.  
  
  
It successfully extracts and puts the information u need into 
your excel sheet by column
* ISSN
* Publisher
* version\[pathway\]: embargo information

#Running with xlwings
To run the script on excel, you need to make sure your Excel workbook is macros enabled.
You also need to make sure xlwings is enabled in your VBA environment. 
  
Everytime you implement a new script/edit an old script, you need to hit import UDF's before using it as 
a function in excel.  
  
Refer the [documentation](https://docs.xlwings.org/en/stable/installation.html#add-in) for more details.
