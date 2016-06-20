# shirt_factory
PDX CodeGuild final project
Github link: https://github.com/justinglobal/shirt_factory/blob/master/proposal.md

### Intro

Shirt Factory ascii art generator is a web app to create an ascii art .png image file from an uploaded image.

It takes in an image file, transforms the image to a string of characters in python, saves the string in the database using django, and renders an output .png image with transparent background of the original image.

It has 3 pages made via django templates:

1. Create and save an ascii art image
2. Permanent page to store the design
3. Gallery for viewing all designs

### Setup

Python 3.5.1

Package requirements:
Django 1.9.6
Pillow 3.2.0

### Usage

1. Create ascii art image - Post page has form input for image file and metadata (design name, comment)
  - input image
  - click 'preview' button for a preview of the design
  - click 'save' to save the image to the database

2. Design page for each design - view + link to design page or image
  - design page and image have permanent link

3. View all designs page - view all designs and a thumbnail size version
