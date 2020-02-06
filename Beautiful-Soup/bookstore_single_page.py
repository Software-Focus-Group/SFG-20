from bs4 import BeautifulSoup  #used for scraping
import requests #used to send get requests to fetch the data 
from word2number import w2n #minor QOL improvement module to convert words to number
from pprint import pprint #pretty print dicts


# website to be scraped ; the book store
url="http://books.toscrape.com"

# Gets the data from the url , will be in the form of HTML same as you would see when you inspect the page
content = requests.get(url)

# create soup from the content to parse
# we'll be using pythons native html parser -- html.parser, will work with other parsers too eg lxml
soup = BeautifulSoup(content.text,"html.parser")

# We are hoping to scrape the website and collect the following items
#	-Title
#	-Price
#	-Rating
#	-Stock availability
# If you inspect you see that all the books are in <li> items with the class id as "col-xs-6 col-sm-4 col-md-3 col-lg-3"
# so we find all <li> elements with that class
# class_ used as class is already a keyword in python
items = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

# print number of elements found
print("Number of items in this page = ",len(items))

# list to store all the details
books = [] 

for item in items:
	# temp dictonary to hold the details
	temp = {}

	# title is an attribute of the <a> tag inside <h3> which is inside <article>
	# as there is only 1 <article> we use the " . " to get inside it ,same with h3,a. attrs lists the attributes
	temp["title"] = item.article.h3.a.attrs["title"] 

	# price is inside <div> with class "product_price", but since there is more than one <div> we need to use find
	# inside that <div> we  find a <p> with class "price_color" and use text to get the data and splice off the undesired unicode at the front [1:]
	temp["price"] = item.article.find("div",class_="product_price").find("p",class_="price_color").text[1:]

	# stock is inside the <div class="product_price"> within <p> class "instock availability"
	# as we have more than one <div> we use find("div",class_="product_price")
	# we use the .text method to extract the text as a string and use strip() to remove white spaces
	temp["stock"] = item.article.find("div",class_="product_price").find("p",class_="instock availability").text.strip()	

	# star rating is a word inside the <article> within a <p> with class "star-rating"
	# we use the word2number module to make words [One,Two,Three...] --> [1,2,3..]
	temp["rating"] = w2n.word_to_num(item.article.p.attrs["class"][1])

	# store the dictionary in the list of books
	books.append(temp)


# All above paths to the data was found by inspecting the source


# Print all the dictionaries on the page with the details
for i in books:
	pprint(i)
	print("-------------------------------------------")
