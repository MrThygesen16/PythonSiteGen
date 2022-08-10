# LinkedIn Company Scraper

_____

TLDR; This project scrapes data about companies from LinkedIn. 

## Build, run, & requirements
This section will detail how to download, run, and use the program.

### Requirements
This section is still a place holder, but this is built purely using python and a few different libraries. The exact dependencies can be found in the file `requirements.txt`. Although it is a little bloated. A review of the exact requirements might be needed.

### Build and run
To run this project, it is recommended to clone this repo to your machine. So far this script has only been run and tested on a MacBook Pro - so there are no guarentees to whether or not it would work on Windows/Linux.

In any case, once the repo has been cloned, it is recommended that you create a python virtual environment. 

When you're inside the project folder type:
```
 python -m venv venv 
```

Into the console.

To activate this virtual environment type:
```
. venv/bin/activate
```
*note: this will be different on windows*

There will be visible indication in your command line once the virtual environment is activated:
```
(venv) name-of-pc-here linkedin-scraper 
```


Now finally (with the venv acivated) type:
```
pip install -r requirements.txt
```

With that, the dependencies should be installed, and the script usable. Using virtual environments for python is considered a best practice as it helps segment dependencies and help reduce clutter in your computers main python directory.

*Note:  it is recommended that two screens are used. Furthermore, LinkedIn should be set to 50% zoom in google chrome. Running this program over night with a secure internet connection would be best...*

## Background and intention 
This started as way to try and assist a fellow intern. They were given an excel document with well over 1000+ rows of different companies to extract information on. This process involved going into LinkedIn, going to their about page, copying the company size, pasting it back into the excel spread-sheet, going back to the webpage, finding the company headquarters, and doing the same, etc. This is a process that would have taken him many hours and many days. Manual data entry - not a great task to waste time on. This project was an attempt to try and cut down their work as much as possible.

The sort of data we want to collect around a company involves:
* Company size --> this can be a range (e.g. 2-10), etc.
* Company headquarters --> a location (e.g. Australia)
* Company Industry --> the good/service they provide (e.g. Software Services)

 *Note: using two screens & having a LinkedIn window open already at 50% zoom produces the best results...*