# Using Python & ChatGPT to webscrape

______

## First Attempt(s)

1. Tried to use more traditional web-scraping methods (e.g. Selenium etc.) --> realised this was an issue as the website required you to scroll to load more data on attendees (infinite scroll)
2. Thought about using OpenCV to take screenshots and parse; did this is a previous project; however the scrolling issue stoppped me dead in my tracks

After enough googling/inspecting elements etc. figured out that the website was calling an API each time I scrolled down, and that's how more poeple were being loaded in.. About 20 per page. 

As it turns out there were roughly 175 page. Doing a bit of basic maths we get:
```
175 * 20 = 3500
```

So all in all, there is about ~3,500 on this list alone. It would take tens, if not hundreds of hours to scroll through each page. and collect this info. What a waste of time that would be...

> Never spend 6 minutes doing something by hand when you can spend 6 hours failing to automate it


### Steps:
- Go into inspect (on chrome)
- Network tab
- Scroll down/click load more
- Click the second request:
```
https://api-prod.grip.events/1/container/5062/search?search=&sort=name&order=asc&type_id=5716,5718,5714,5717&page=2
```
- Look at the general headers:
```
Request URL: https://api-prod.grip.events/1/container/5062/search?search=&sort=name&order=asc&type_id=5716,5718,5714,5717&page=2
Request Method: GET
Status Code: 200 
Remote Address: 54.73.94.200:443
Referrer Policy: no-referrer-when-downgrade
```
-  Go into preview section:
```js
{success: true, } data: [
    {id: 7311283, application_id: 743, name: "Abbi Failla", first_name: "Abbi", last_name: "Failla",},
    {id: 7351156, application_id: 743, name: "Abby DuLac ", first_name: "Abby ",},
    {id: 7381669, application_id: 743, name: "Abby Rogers", first_name: "Abby", last_name: "Rogers",},
    {id: 7311328, application_id: 743, name: "Abdo Bridi", first_name: "Abdo", last_name: "Bridi",},
    {id: 7380088, application_id: 743, name: "Abdul Bari Ahmadzai", first_name: "Abdul Bari",},
    {id: 6027759, application_id: 743, name: "Abhijit Ganguly", first_name: "Abhijit ",},
    {id: 7322530, application_id: 743, name: "Abhijit Joshi", first_name: "Abhijit", last_name: "Joshi",},
    {id: 7343896, application_id: 743, name: "Abhinav Warrier", first_name: "Abhinav",},
    {id: 6027962, application_id: 743, name: "Abhishek Katyal", first_name: "Abhishek ",},
    {id: 7260973, application_id: 743, name: "Abhishek Kapur", first_name: "Abhishek", last_name: "Kapur",},
    {id: 7262137, application_id: 743, name: "Abraham Lin ", first_name: "Abraham ",},
    {id: 7481091, application_id: 743, name: "Abraham Adamour", first_name: "Abraham",},
    {id: 7337961, application_id: 743, name: "Aby Lijtszain", first_name: "Aby", last_name: "Lijtszain",},
    {id: 6027741, application_id: 743, name: "Adam Jeevunjee ", first_name: "Adam ",},
    {id: 7347401, application_id: 743, name: "Adam Jensen", first_name: "Adam ", last_name: "Jensen",},
    {id: 7423058, application_id: 743, name: "Adam Gough ", first_name: "Adam ", last_name: "Gough ",},
    {id: 7414089, application_id: 743, name: "Adam Harrington ", first_name: "Adam ",},
    {id: 7417349, application_id: 743, name: "Adam Angell ", first_name: "Adam", last_name: "Angell ",},
    {id: 7428706, application_id: 743, name: "Adam Annen", first_name: "Adam", last_name: "Annen",},
    {id: 7415869, application_id: 743, name: "Adam Bryant", first_name: "Adam", last_name: "Bryant",}]
```

Perfect, we found what we were looking for! This is one request of many. 

I (naively) tried entering in this API url into my webrowser, only to be greeted with the message:
```js
{"error":"missing authorization header"}
```

Hmmm. Still no luck.

I thought to myself, this would be a perfect time to try ChatGPT... Surely it might be of use?

___

___

## ChatGPT

I've never used ChatGPT prior to this, so I was keen to see its capabilities first-hand. I decided to jump straight into it, and ask it to assist me with this task...


#### Prompt
```
Write a powershell script to query and retrieve the data from this api: https://api-prod.grip.events/1/container/5062/search?search=&sort=name&order=asc&type_id=5716,5718,5714,5717&page=4
```

#### Response
```perl
$url = "https://api-prod.grip.events/1/container/5062/search?search=&sort=name&order=asc&type_id=5716,5718,5714,5717&page=4"
$response = Invoke-RestMethod -Uri $url
$data = $response.data

foreach ($item in $data) {
    Write-Host "Name: $($item.name)"
}
```

It gave me a script in what appears to be pearl (that's what the ChatGPT syntax highlighting said). I should have been a bit more specific.

_____

#### Prompt
```
When trying to access a website I get the error message: {"error":"missing authorization header"} what does this mean and how can I get around this?
```

#### Response
```
The error message "missing authorization header" indicates that the server is expecting the client (you) to include an authorization header in the request to access the website.

To get around this, you'll need to include the necessary authorization information in the header of the request you're sending to the server. The exact format of the header and the information it should contain depends on the authorization mechanism used by the server.

If the server is using Basic authentication, the header should contain the word "Basic" followed by a base64-encoded string of the username and password separated by a colon.

If the server is using token-based authentication, the header should contain the word "Bearer" followed by the token.

Here's an example of how you could include an authorization header in a curl request:
```
```bash
curl -H "Authorization: Bearer <token>" https://example.com
```
```
You'll need to replace `<token>` with the actual token you have received from the server.

If you're using a different programming language or tool, the specific method for including the authorization header in your request will vary, but the basic concept will be the same.
```

Unfortunately this did not work either. Again, in retrospect, more specificity (i.e. what tools & languages) would have been a good start.

____

#### Prompt
```
How can I see the authorization token on a website I am visiting
```

#### Response
```
You can view the authorization token for a website you're visiting in the developer tools of your web browser. Here's how you can do this in Google Chrome:

1.  Right-click on the page and select "Inspect"
2.  In the developer tools window that opens, switch to the "Network" tab
3.  Refresh the page you're visiting
4.  Look for the API request you're interested in, and click on it to view its details
5.  Switch to the "Headers" tab, and look for the "Authorization" header

Note that some websites may encode the token, and it may not be immediately readable in its raw form. Additionally, not all websites will include the authorization token in the request header, as it may be stored elsewhere or passed as part of the URL or as a cookie.

Keep in mind that viewing the authorization token of someone else's website is not ethical, and may also be illegal, so use this information responsibly.
```

To my surpise, this worked exactly how I wanted it to. I was able to see the field `x-authorization` with no issues.

This was my first little 'win' with ChatGPT.


Below is what the `x-authorization` looks like:

```
Headers:
x-authorization: d42cdd6-6592-448d-a2ca-c315808c2960
```

This appears to be submitted to the API - as some sort of form of authentication. My guess is that the browser stores this info, and then attaches it to the HTTPS request (in the header), and that allows the browser to load the queried data from this API.

I needed an easy way to query this. I was still having issue with curl unfortunately.

One of my coworkers recommended that I use PostMan for testing this. It actually worked really well - I just plugged in the following values:
```
https://api-prod.grip.events/1/container/5062/search?search=&sort=name&order=asc&type_id=5716,5718,5714,5717&page=10

Headers:
x-authorization: ad42cdd6-6592-448d-a2ca-c315808c2960
```

And to my surprise -- it worked.

The response received is below:
```js
{
    "success": true,
    "data": [
        {
            "id": 7420542,
            "application_id": 743,
            "name": "Amber Franklin",
            "first_name": "Amber",
            "last_name": "Franklin",
            "headline": "Social Media at Media AF",
            "summary": " ",
            "job_title": "Social Media",
            "company_name": "Media AF",
            "job_industry": null,
            "location": "Chicago",
            "location_code": "en-gb",
            "picture_url": "https://events-cdn.grip.events/things-images/7e5623fb324698f4f438635571cf652a_1675293967.jpg",
            "type_id": 5714,
            "type_category_id": 1,
            "type_key_translation": "Attendee",
            "active": 1,
            "needs_activation": 0,
            "date_created": 1674503422,
            "can_meet": 0,
            "can_swipe": 1,
            "date_updated": 1675294525,
            "uri": "/1/container/5062/thing/7420542",
            "words": null,
            "last_joined_group_ids": "",
            "container_id": [
                5062
            ],
            "sessions_speaking": [],
            "sessions_attending": [
                121659
            ],
            "types": [
                {
                    "container_id": 5062,
                    "type_id": 5714,
                    "can_meet": "true",
                    "can_swipe": "true",
                    "type_key_translation_en": "Attendee",
                    "type_key_translation": "Attendee",
                    "type_key_translation_en-gb": "Attendee"
                }
            ],
            "promotion_locations": [],
            "group_ids": [],
            "groups": [],
            "type_key_translation_en-gb": "Attendee",
            "type_key_translation_en": "Attendee",
            "promoted": 0,
            "promotion_level": "normal",
            "default_meeting_location": null,
            "registration_id": null,
            "gps_lat": null,
            "gps_lng": null,
            "location_lat": null,
            "location_lng": null,
            "metadata": null,
            "categories": null,
            "did_answer_yes": 0,
            "swipe_message": null,
            "swipe_message_date_sent": null,
            "default_access": "in_person"
        },
        ...
    ]
}
```

Great. So now we can request data from this API whilst not even being on the site. This was a major turning point in this little exercise. Querying this API via postman to get page after page of JSON would be faster than scrolling through the site, yet still quite slow...

Lets see if ChatGPT can generate a script/command to automate this process...


#### Prompt
```
How to curl an api url with a parameter for `x-authorization`
```
#### Response
```
The curl command to access an API endpoint with a header parameter `x-authorization` would be:
```
```less
curl -H "x-authorization: [value]" [API endpoint URL]
```
```
Replace `[value]` with the actual value for the `x-authorization` header and `[API endpoint URL]` with the actual URL of the API endpoint you want to access.
```

This seemed certain to worked. Unfortunately... this was not the case.

______

#### Prompt
```
When running the code above I get the error: `Invoke-WebRequest : Cannot bind parameter 'Headers'. Cannot convert the "x-authorization:ad42cdd6-6592-448d-a2ca-c315808c2960" value of type "System.String" to type "System.Collections.IDictionary".` How can I fix this
```

#### Response
```
The error message is indicating that the `-Headers` parameter of the `Invoke-WebRequest` cmdlet in PowerShell requires a hashtable (dictionary) as its value, not a simple string. To correct the error, you can create a hashtable that contains your header key-value pair and pass that as the value of the `-Headers` parameter:
```
```bash
$headers = @{ "x-authorization" = "ad42cdd6-6592-448d-a2ca-c315808c2960" }
Invoke-WebRequest -Uri [API endpoint URL] -Method GET -Headers $headers
```
```
Replace `[API endpoint URL]` with the actual URL of the API endpoint you want to access.
```

This command ended up working perfectly. I could not describe how happy and impressed I was that I had even got this far. I definitely could have Googled this, but honestly, this is far more convenient.

______

#### Prompt
```
How can I rewrite this script in python
```

#### Response
```
In Python, you can make a GET request to an API endpoint with a header using the `requests` library. Here's an example script to do that:
```
```python
import requests

url = '[API endpoint URL]'
headers = {'x-authorization': 'ad42cdd6-6592-448d-a2ca-c315808c2960'}

response = requests.get(url, headers=headers)

print(response.content)
```
```
Replace `[API endpoint URL]` with the actual URL of the API endpoint you want to access. The `requests.get` method sends a GET request to the specified URL, and the `headers` argument is used to pass the headers as a dictionary. The `response` object returned by the `requests.get` method contains the response content, which can be accessed using the `content` attribute. In the example above, the content is printed to the console.
```

This python code is essentially the basis for the rest of the project. 

________

#### Prompt
Write a python script to parse this json data: 

#### Response
```js 
{"success":true,"data":[{"id":7384201,"application_id":743,"name":"Eran Pereg","first_name":"Eran","last_name":"Pereg","headline":"CEO at Conbo.ai","summary":"Eran is the CEO and co-founder of conbo.ai. \n\nConbo.ai leverages existing cameras to track, analyze and forecast vehicles and cargo locations within any terminal or logistic hub to streamline operations, increase predictability and deliver better customer service, all while providing sharper tools to meet SDG goals.\n\nEasy to adopt SaaS-based solution\nNo need for additional systems, such as \u000bLPR systems, GPS, OCR, or RFID","job_title":"CEO","company_name":"Conbo.ai","job_industry":null,"location":"Israel","location_code":"en-gb","picture_url":"https://events-cdn.grip.events/things-images/fe8e8390fbd94ebad7d78cbc2adbfb13_1674207650.png","type_id":5714,"type_category_id":1,"type_key_translation":"Attendee","active":1,"needs_activation":0,"date_created":1674039624,"can_meet":1,"can_swipe":1,"date_updated":1674209445,"uri":"/1/container/5062/thing/7384201","words":null,"last_joined_group_ids":"","container_id":[5062],"sessions_speaking":[],"sessions_attending":[121613,121610,121601,121612],"types":[{"container_id":5062,"type_id":5714,"can_meet":"true","can_swipe":"true","type_key_translation_en":"Attendee","type_key_translation":"Attendee","type_key_translation_en-gb":"Attendee"}],"promotion_locations":[],"group_ids":[],"groups":[],"last_joined_group_ids_en-gb":"","type_key_translation_en-gb":"Attendee","type_key_translation_en":"Attendee","promoted":0,"promotion_level":"normal","default_meeting_location":null,"registration_id":null,"gps_lat":null,"gps_lng":null,"location_lat":null,"location_lng":null,"metadata":null,"categories":null,"did_answer_yes":0,"swipe_message":null,"swipe_message_date_sent":null,"default_access":"in_person"}]}
```

```
Here is a Python script that parses the JSON data using the `json` library:
```
```python
import json

json_data = {"success":true,"data":[{"id":7384201,"application_id":743,"name":"Eran Pereg","first_name":"Eran","last_name":"Pereg",
"headline":"CEO at Conbo.ai","summary":"Eran is the CEO and co-founder of conbo.ai. \n\nConbo.ai leverages existing cameras to track, analyze and forecast vehicles and cargo locations within any terminal or logistic hub to streamline operations, increase predictability and deliver better customer service, all while providing sharper tools to meet SDG goals.\n\nEasy to adopt SaaS-based solution\nNo need for additional systems, such as \u000bLPR systems, GPS, OCR, or RFID","job_title":"CEO","company_name":"Conbo.ai","job_industry":null,"location":"Israel","location_code":"en-gb"," picture_url":"https://events-cdn.grip.events/things-images/fe8e8390fbd94ebad7d78cbc2adbfb13_1674207650.png","type_id":5714,"type_category_id":1,"type_key_translation":"Attendee","active":1,"needs_activation":0,"date_created":1674039624,"can_meet":1,"can_swipe":1,"date_updated":1674209445,"uri":"/1/container/5062/thing/7384201","words":null,"last_joined_group_ids":"","container_id":[5062],"sessions_speaking":[],"sessions_attending":[121613,121610,121601,121612],"types":[{"container_id":5062,"type_id":5714,"can_meet":"true","can_swipe":"true","type_key_translation_en":"Attendee","type_key_translation":"Attendee","type_key_translation_en-gb":"Attendee"}],"promotion_locations":[],"group_ids":[],"groups":[],"last_joined_group_ids_en-gb":"","type_key_translation_en-gb":"Attendee","type_key_translation_en":"Attendee","promoted":0,"promotion_level":"normal","default_meeting_location":null,"registration_id":null,"gps_lat":null,"gps_lng":null,"location_lat":null,"location_lng":null,"metadata":null,"categories":null,"did_answer_yes":0,"swipe_message":null,"swipe_message_date_sent":null,"default_access":"in_person"}]}

parsed_data = json.loads(json_data)

if parsed_data['success']:
    data = parsed_data['data']
    for item in data:
        print('ID:', item['id'])
        print('Name:', item['name'])
        print('Headline:', item['headline'])
        print('Summary:', item['summary'])
        print('Job Title:', item['job_title'])
        print('Company Name:', item['company_name'])
        print('Location:',
```

Good thing to note is that whilst this was super convenient - make sure to NEVER input personal data into ChatGPT...
_____

#### Prompt
``` 
rewrite the following code to write the data to a csv file, rather than print to console: parsed_data = json.loads(response) if parsed_data['success']: data = parsed_data['data'] for item in data: print("-----------------") print('ID:', item['id']) print('Name:', item['name']) print('Headline:', item['headline']) print('Summary:', item['summary']) print('Job Title:', item['job_title']) print('Company Name:', item['company_name']) print('Job Industry:', item['job_industry']) print('Location:', item['location'])
```

#### Response
```python
import csv
import json

parsed_data = json.loads(response)

if parsed_data['success']:
    data = parsed_data['data']
    with open('data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'ID', 
            'Name', 
            'Headline', 
            'Summary', 
            'Job Title', 
            'Company Name', 
            'Job Industry', 
            'Location'
        ])
        for item in data:
            writer.writerow([
                item['id'], 
                item['name'], 
                item['headline'], 
                item['summary'], 
                item['job_title'], 
                item['company_name'], 
                item['job_industry'], 
                item['location']
            ])
```

The above code ends up running really slow. After a bit of refactoring, tweaking, troubleshooting, and further consulting with ChatGPT it became quite a bit faster.

____
____

## Final Python Script

Requirements
```
pip install requests
```

Below is the final Python script.

```python
# scrape.py

import requests
import json
import csv

  
def start() -> None:
    # use to construct address for API
    base_url = 'https://api-prod.grip.events/1/container/5062/search?search=&sort=name&order=asc&type_id=5716,5718,5714,5717&page='

    # there is about 175 pages total
    for i in range(1, 5):
        # API Destination to query
        url = base_url+str(i)

        # authentication token for above API
        headers = {'x-authorization': 'ad42cdd6-6592-448d-a2ca-c315808c2960'}
        print(url)

        # get request, process, and parse into json
        response = requests.get(url, headers=headers)
        response = response.text
        parsed_data = json.loads(response)

        # writing to csv file
        if parsed_data['success']:
            data = parsed_data['data']
            with open('output.csv', mode='a', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                for item in data:
                    # Display data as it's being written
                    print("-----------------")
                    print('Name:', item['name'])
                    print('Company Name:', item['company_name'])
                    print('Job Title:', item['job_title'])
                    print('Location:', item['location'])

                    # Sanitize and write data to csv file using the JSON keys
                    row = [
                        sanitize(item['name']),
                        sanitize(item['company_name']),
                        sanitize(item['job_title']),
                        sanitize(item['location'])
                    ]
                    writer.writerow(row)

# function that handles corrupted strings/characters during fetch process
def sanitize(s) -> str:
    try:
        s = s.encode('utf-8', 'ignore').decode('utf-8-sig')
    except:
        return ' '
    return ''.join(c for c in s if ord(c) >= 32)

  

if __name__ == "__main__":
    start()
```


### Result:

Below is a small sample of the 3000+ row Excel/CSV file (took a few minutes to run the script in full).
```
Aabhas Zaveri,Datamatics Robotics Software Inc.,"SVP, Intelligent Automation",Dallas Tx

Aaron Clark,Updike Distribution Logistics,"Sr. Director, Logistics",

Aaron Flack,Susquehanna Growth Equity,Partner,

Aaron Lewis,Marlin Equity Partners,Vice President,

Aaron Marx,Intralox,Global Industry Team Leader ,

Aaron Matto,True Wind Capital,Partner,

Aaron McCall,Flow Trans Inc,President,

Aaron Meyerrenke,Procter & Gamble,Private Fleet Purchases Manager,

Aaron Neil,Battery Ventures,Investor,

Aaron Nguyen,bp pulse fleet,Product Marketing Associate,

Aaron Pierce,PerotJain,Partner,

Aaron Taylor,Cubiscan,Marketing Manager,

Aaron Weston,Lifeline Logistics,Co-Founder,

Abbas  Azher,"Maritime Logistics, Inc.",CEO ,

Abbi Failla,EASE Logistics,"VP, Business Operations",

Abby  DuLac  ,PepsiCo,Warehouse Asset Mgr,

Abby Rogers,Vector,Deployment Strategist,"Detroit, MI"

Abdo Bridi,Anheuser-Busch InBev,Logistics Innovation Manager – Middle America Zone,

Abdul Bari Ahmadzai,Continental Expedited Services,Director of Technology,

Abhijit  Ganguly,Goodyear Ventures,Managing Director,
```