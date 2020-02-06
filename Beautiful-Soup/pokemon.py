from bs4 import BeautifulSoup  #used for scraping
import requests #used to send get requests to fetch the data 
from pprint import pprint #pretty print dicts

# website to be scraped ; the pokemon database
url = "https://pokemondb.net/pokedex/game/gold-silver-crystal"

# We are hoping to scrape the website and collect the following items
#	-Name
#	-pokedex number
#	-link to its page

# Getting the contents of the website
PokeContent = requests.get(url)

# Making the soup using the html.We extract the content using the .text method variable and we're using the python inbuilt html parser
PokeSoup = BeautifulSoup(PokeContent.text,"html.parser") 

# Empty list to store the pokemon
Pokemon = []

# Pokemon are in <main> --> <div class="infocard-list infocard-list-pkmn-lg"> ---> <div class=infocard>
# and since theres only one main we use the " . " to get inside it
# We also can search for partial strings to be matched , so no need to type entire class name 
PokeCollection = PokeSoup.main.find("div",class_="infocard-list")

# Finds all the <div> containg the string "infocard" in their class name as they contain each individual pokemon
PokeList = PokeCollection.findAll("div",class_="infocard")

print("NUMBER OF POKEMON === ",len(PokeList),sep="",end="\n\n")


for item in PokeList:
	# Temporary dictionary to hold the details
	temp = {}

	# All the details are found in the <span> with class name text-muted
	
	temp["name"] = item.find("span",class_="text-muted").a.text

	temp["number"] = item.find("span",class_="text-muted").small.text

	# Appending the base url "https://pokemondb.net/" to the link of the pokemon so that we get the full url
	temp["link"] = "https://pokemondb.net" + item.find("span",class_="text-muted").a.attrs["href"]
	
	Pokemon.append(temp)


for pokemon in Pokemon:
	pprint(pokemon)
	print("--------------------------------------------------")

