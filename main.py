import requests       # requests module to use get or post the api. used to get the data from api
import json          # helps is understanding the json returned from the data

api_name = input("Enter the api- key: ")       # get the api key from https://api.watchmode.com Its free.
film_name = input("Enter the movie name: ") 

''' 
---------------------------------------------------------------
so actually to get streaming services from watchmode API. 
first you have to get the streaming services the api supports, and its 'id', using /sources endpoint
then you get the watchmode ID of the respective movie you want information about(in our case streaming service) using /search endpoint
then you use the watch mode api to get the streaming service id  and region it is hosted in using /title/watchmode Id/sources
after that you compare the streaming service souce id using the data you got from the first step
---------------------------------------------------------------
'''

file1 = open("u.txt", "r") #I have stored the streaming source Id and their name in another file as it does not get updated often an it is mostly static
data1 = json.load(file1) # loads the file 

'''
-------------------------------------------------------------
Here u.txt is the file where we stored the streaming source ID the first step
you can do that using the following code
file1 = open("u.txt", "w")
response = requests.get('https://api.watchmode.com/v1/sources/?apiKey={apiKey}')   [remove the curly braces{} while typing the api key
data1 = response.json()
json.dump(data1,file1)
------------------------------------------------------------
'''

def func(string):
    if(string=="US"):
        return "United_States"
    elif(string=="CA"):
        return "canada"
    elif(string=="GB"):
        return "England"
    elif(string=="AU"):
        return "Australia"
    else:
        return "country not specified"

search = "https://api.watchmode.com/v1/search/?apiKey="+str(api_name)+"&search_field=name&search_value=" + film_name  #using string concatenation to get the required url

file2 = requests.get(search) # searches the api call on internet

data=file2.json()  # the data you get is converted into json format and stored into data

for a in data['title_results']: #using to get the id of the movie
    movie_id=a['id']

regions = "https://api.watchmode.com/v1/title/" +str(movie_id) +"/sources/?apiKey="+ str(api_name) #to get the the movie streaming ID
get_regions = requests.get(regions)
data2 = get_regions.json()

def func(string):  # as the specific region where the movie is streamed is  returned using the codes so to convert it into text for better reading
    if(string=="US"):
        return "United_States"
    elif(string=="CA"):
        return "Canada"
    elif(string=="GB"):
        return "England"
    elif(string=="AU"):
        return "Australia"
    else:
        return "country not specified"



for b in data2: # loops the streaming service returned
    for a in data1: # loops with data stored in the text file earlier stored 
        if(b['source_id']==a['id']): # checks the source id of movie where it is streamed with streaming id of the streaming services earlier stored in localstorage 
            print(a['name']+ "("+ b['web_url']    +")"+"------->"+ func(b['region'])) # prints the name, url(to watch it directly) with the region

    



