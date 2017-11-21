import bs4 as bs
import urllib.request

def take_input():
	title = input("Enter a movie or a TV show name  : ")
	title = " http://www.imdb.com/find?q=" + title.replace(' ','+')
	return title

def searching(title):
	sourc = urllib.request.urlopen(title).read()	
	source = bs.BeautifulSoup(sourc,'html.parser')
	if str(source.findAll(True, {"class":["findResult odd"]})) == "[]":
		print("\n No items found please try again...\n\n")
		title = take_input()
		return(searching(title))
	else:
		table = source.find('table')
		table_rows = table.find_all('tr')
		result=[]
		j = 1
		for tr in table_rows:
			cols = tr.find_all('td')
			for col_num in range(len(cols)):
				col_num+=1
				result.append(cols[col_num].a['href'])
				print(str(j) +"."+ cols[col_num].text)
				j+=1
				break
		return(result)



def details(result):
	select = int(input("Please select which one you are searching for, mention the number :"))
	newsourc = urllib.request.urlopen("http://www.imdb.com" + result[select-1]).read()
	newsource = bs.BeautifulSoup(newsourc,'html.parser')
	if((newsource.find("meta", {"property":"og:type"})['content'])=="video.movie"):
		print("\n\n\n\t\t\t\t\t\t\tIt's a movie\n")
	elif((newsource.find("meta", {"property":"og:type"})['content'])=="video.tv_show"):
		print("\n\n\n\t\t\t\t\t\t\tIt's a TV Show\n")
	else:
		print("\n\n\n\t\t\tT\t\t\type Un identified\n")
	print("\t\t\t\t\t\t\t" + newsource.find("meta", {"name":"title"})['content'])
	print("\n\n\n\t\t\t\t\t\t--------:  Description  :------\n\n" + newsource.find("meta", {"name":"description"})['content'] + "\n\n\n")
	print("\t\t\t\t\t\t\tRating  ::  " + newsource.select_one("span[itemprop=ratingValue]").text)


	

title = take_input()
result = searching(title)
details(result)
#print(result)
