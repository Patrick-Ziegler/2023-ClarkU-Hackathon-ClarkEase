# 2023-ClarkU-Hackathon-ClarkEase
ClarkEase is an interactive map web page that provides a detailed map of the accessibility of every building on Clarks campus
Created by Patrick Ziegler


## HOW TO USE

After opening the Repo, open a terminal and Cd into the parent folder.
Enter The following commands:
(WINDOWS)
..\venv\Scripts\activate
(MAC/LINUX)
venv/bin/activate

And then activate the Wesbite using
python manage.py runserver

From here open your browser and enter the following into the search bar:
http://127.0.0.1:8000/

Now you are on CLARKEASE! Select a map marker on the Clark Campus to see the accessibility of the respective building.

- **PROJECT AIM**: WHAT PROBLEM ARE YOU SOLVING? WHY DID YOU CHOOSE THIS PROBLEM?

With CLARKEASE, I was aiming to create a location for anyone to reference the accessibility of any of the buildings on campus. As someone who works at ITS on campus,
we will occasionally have to go on appointments to staff/faculty offices and pick up or drop off large desktops using a big metal cart. Working at that job has made me realize
not only how many buildings on our campus are completely inaccessible for someone in a wheelchair, but also how annoying it is to get around campus when, for example, only one of the
entrances to the building you are trying to enter automatically or doesn't have stairs, and it's on the complete opposite side of the building from where you are coming or where 
you need to be.

- **SOLUTION**: HOW DOES YOUR PROJECT ADDRESS THE ISSUE? WHAT TECHNOLOGY STACK DID YOU USE?

My website provides a single spot where someone can, at a glance, see how accessible the building they are headed to is. It has data for not just the main buildings on campus like the dorms
and dining hall, but also some of the off-campus buildings that people may not be as familiar with such as the corner house or the CPG building. CLARKEASE was built using django, so most of the coding was
done in Python, HTML, and CSS. I used the Folium Library to visualize my map and all of the building data on the map.

- **REAL-WORLD APPLICATION**: WHO IS THE TARGET MARKET? HOW DOES IT BENEFIT THEM? ANY EXISTING SIMILAR SOLUTIONS?

The target audience of my site currently is any student or faculty who have any sort of disability that limits their movement, and my coworkers at the Helpdesk who also need to deal with pushing a big cart around
campus. Currently, besides just memorizing which buildings have elevators and such, there is no real resource online to see what parts of campus are accessible or not, and I am hoping that a project like mine will
be able to provide a resource for people who seriously rely on data like that to get around with a useful tool.


- **FUTURE AIMS AND GOALS**: WHAT ARE THE NEXT STEPS? ANY PLANS FOR SCALING OR ADDING FEATURES?

While working on CLARKEASE, I realized how easily the same framework of code can be applied to any other campus or town. Ignoring the color scheme, by providing an Excel document with the data and locations for
all of the buildings, and changing some settings with the map location, someone could easily convert CLARKEASE to work in just about any other setting. It's so easy, that I plan to create a tool  in the future
for users to easily generate their own version of the site by just entering a dataset (as opposed to having them open up the code). Additionally, I originally had plans to add a button that allows users to report
an out-of-order elevator, which would mark it as out of service until the next morning. After coding this I realized it is basically impossible without actually hosting the site on an HTTP server, so I had to cut
it. If I hosted the site in the future, this feature would greatly improve the functionality of the site.
