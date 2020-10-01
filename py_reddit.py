import requests
import json
import csv
import time
import datetime

"""
Full api avalible at
https://pushshift.io/api-parameters/
"""
def hello():
    print("Hello world!")

def scrape( type,
            sort_type = "",
            size = 10**11,
            sub = ""):
    
    queries = 0
    data = [] #scrapped data is added to this list
    query_on = "" #element used to continuisly search

    url = url_make(type, sub=sub, after = 12) #
    
 
    if sort_type=="":
        url = url_make(type, sub=sub, after = 12) #
    else:

         url #allows preperation of URL

    if sort == "":
        sort = "asc"
    if sort_type =="": 
        sort_type = "created_utc"
    holder_url = url #allows preperation of URL
#start while
    while len(data)<=size:
        r = requests.get(holder_url) #pings pushift using URL
        holder = json.loads(r.text)["data"] #Processes pushift data and inserts it into a holder array

        if queries!= 0 and holder[-1][sort_type] == query_on: #checks if repeated element
            connect_point = data[-1] #grabs last unrepeated element
            position_join = holder.index(connect_point)
            if sort=="asc":
                print("ascending")
                data = data + holder[position_join:] #Need to find out if colon goes before or after
            if sort=="desc":
                print("descending")
                #data = data + holder[position_join] #Need to find out if colon goes before or after
            break
        data = data + holder
        query_on = holder[-1][sort_type]
        holder_url = url.replace("")
        queries +=1 #adds one to number of queries made
#end while

    if len(data)> size:
        data = data[:size]
    
    return data, queries

def query( type, #comment, submission, subreddit
            size = "", #integer less than 1000
            sub = "", #subreddit
            after = "", #from after in epoch time
            before = "", #from before in epoch time
            after_id = "",
            before_id = ""
            ):
    url = url_make(
        type, #comment, submission, subreddit
                size = size, #integer less than 1000
                sub = sub, #subreddit
                after = after, #from after in epoch time
                before = before, #from before in epoch time
                after_id = after_id,
                before_id = before_id
    )
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']

def url_make(type, #comment, submission, subreddit
            sort = "",
            sort_type = "",
            size = "", #integer less than 1000
            sub = "", #subreddit
            after = "", #from after in epoch time
            before = "", #from before in epoch time
            after_id = "", #int
            before_id = "", #int
            created_utc = "", #int
            score = "", #int
            gilded = "", #int
            edited = "", #Boolean
            author = "",
            distinguished = ""): 
    url = "https://api.pushshift.io/reddit/search/"+type+"/?"
    if size != "":
        url = url + "/?&size=" + str(int(size)) 
        
    if sub != "": #adds subreddit
        url = url + "&subreddit="+str(sub)
    
    if after != "": #adds from before in epoch time
        url = url +"&after="+ str(after)

    if before!="":
        url = url+"&before="+ str(before)

    if after_id!="":
        url = url+"&after_id="+ str(after_id)

    return url
