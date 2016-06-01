## Shirt Factory 'changelog'

***_journal of development of Shirt Factory website and web app_***

https://github.com/justinglobal/shirt_factory

3/17/2016 - 5/16/2016

This project begins as part of a Python 'full stack' development class at PDX CodeGuild.

PDXCodeGuild's class has a capstone project that requires using all the basic things I would need to get Shirt Factory up and running. I have made a plan for my capstone that accomplishes the basic functionality of my site. After I complete the capstone I will revise/improve the design until I get a fully functioning site.

For the last 2 months I have been learning the basics of software development and Python.
  - Python basics: syntax, data types, functions, if/while statements, etc.
  - Python intermediate: Classes, Modules and processing data
  - Development basics: git/hub, debugging and testing
  - HTML, CSS, JS, JQuery, lodash
  - Django web framework
  - Ajax/JSON/APIs (We haven't covered JSON and API's yet)

Outside of class I made a Heroku account and did a basic install and checked my local server.
  - it all works but it tenuous and could topple like a jenga tower
  - Heroku is a hosting service
  - I'm using Heroku for this project eventually, but I have experience using AWS's 'beanstalk' so we will see. For my final class project I will host locally.

Today, 5/16 I have begun installing my project locally on my laptop to begin actual development.

I have set up my shirt_factory directory and installed the venv and django. My local server is configured and running.

My site will have 3 pages: Index, shirt page, and gallery.

A django site with dynamic pages is fairly complicated, so I will probably start with using the structure of a previous django project for class.

I have done a half-assed job of 'filling in' parts of my project from previous django installations. I am going to finish this, but alot needs to be changed in several files.

For now, I am going to focus on getting my ascii art generator to work.

link: https://github.com/electronut/pp/tree/master/ascii

5/17

ascii art generator works, it has a few quirks

biggest problem: it outputs to a .txt file....will have to figure out how to display image for user in the browser.

set --scale .5 makes circles actually appear circular

will come back to this later

today i'm going to get the basic web pages up

5/23

Well.

Here we are. I've learned *alot* more about actually implementing a full django install.

We learned about the ORM schema and setting up the relational model using a models.py file...it's awesome, does all the SQL stuff automatically but it's hard to set up right.

I started the shirt_factory install using an old, pre-ORM build of a project...I am getting errors when loggin in to my admin django page ('unapplied migrations') so I am setting up a new model and will apply migrations there.

Starting with my ORM, setting up everything, and hopefully making pages by the end of today.

Database tested and active...migrations clean

Test Database:
  - design name (inputtext)
  - timestamp - system generated
  - design text (inputtext)

I use basic text art like this for testing now: ( ͡° ͜ʖ ͡°)

Notes:

- need to use block display font or images are skewed
- test text display needs to be 'block' not stretching to fit window

5/24

Busy day, had to work at ITT tech

David's code really pushed me to get working.

code from David:

<form action="{% url 'upload_ack' %}" method="post">
  <input type="file" name="image">
  <input type="submit">
</form>


def render_upload_ack(request):
  try:
    img = Image.open(request.FILES['image'])  # File like object
  catch IOError:
    img = None

  if img is not None:
    return render('yay')
  else:
    return render('booG')

- Installed Pillow in venv

- Form note: when taking in image files via html form (from: https://docs.djangoproject.com/en/1.9/ref/request-response/#django.http.HttpRequest.FILES):
Note that FILES will only contain data if the request method was POST and the <form> that posted to the request had enctype="multipart/form-data". Otherwise, FILES will be a blank dictionary-like object.

**important note**
- Changed ascii art generator in logic model to not need to use numpy. David wrote it. It is a one-liner:

this code:
def getAverageL(image):
    """
   Given PIL Image, return average value of grayscale value
   """
   # get image as numpy array
   im = np.array(image)
   # get shape
   w,h = im.shape
   # get average
   return np.average(im.reshape(w*h))

is replaced with this funtion:
def getAverageNew(image):
    return statistics.mean(image.getdata())

- tested and it works! used a Pillow function: http://pillow.readthedocs.io/en/3.0.x/reference/Image.html#the-image-class Image.getdata()

after class while at work at ITT I connected the database.

#SUCCESS!!!

it works but everything is wrong with it

- font of text needs to be fixed-width
- extra chars in display (this probably can be fixed using ascii.py's other functions)
- rebuild database
- each design gets its own URL, do this in urls.py

5/26

alot happened today, but it can be summarized by me getting the image to display properly

my main problem was that my database was casting my ascii list of strings to a string when saving it, causing my formatting steps to break. I didn't catch it b/c my testing list was taken from before it gets saved in the database.

I renamed everything.

Need to consider adding database class for serving my images

5/27

potential image storage class

class ImageServe(models.Model):

    background_shirt = models.DataField()

javascript suggestion from david:  avoid using IDs, especially programmatically generated ones. There's almost always a way to more cleanly and concisely get what you want done. In this case it's using the fact that an event handler function has access to the element clicked on; then you can use jQuery selections to find the element you want to modify.
