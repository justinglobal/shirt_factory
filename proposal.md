# Capstone Proposal

Jusin Epperly
PDXCodeGuild Day class - March

### Name
What is the short name of your product or project?

shirt_factory

### High-Level Product

####What is your web app going to do?

Users design tshirt using an image they provide or inputing parameters for a template, with options for transforming the image. Output is an shirt design they can order printed and/or upload to image gallery.


####How does a user interact with it on a high level?

Users input parameters and/or image via the web app and the system will return a processed image representing the shirt design for the web page to display. The input parameters and image are a tshirt design and the processed image output is the processed shirt design image.

Users 'checkout' via an order form page, with a simple web form. Users select size and number of shirts they are purchasing. Image is uploaded to printing database.

Users have the option to upload their final design to an image gallery and specify a title for the design.

MVP for final project has features scaled-down.

Project MVP features

1. Main page with ASCII art generator
2. Page for each finished design with links to purchase
3. Gallery of submitted designs

### Specific Functionality

**Shirt Factory pages and interface**

#### Home page
  * Shirt design section displays blank white shirt initially

  * Design section options displayed via menu
    1. Upload image from file or URL and set design size and shirt color parameters
      * Transform image using ASCII generator
      * Resize and arrange transformed image on blank shirt in section  
      * Display original image thumbnail

    2. Finished design is uploaded to gallery with title and/or purchased and saved in database

#### Shirt page (order form page)
  * Displays final shirt image with form for user to specify order options

  * Order options
    1. size
    2. number of shirts

  * Option to upload design to gallery with title upon completing purchase

  * Payment
    * Uses link to Paypal's payment system CMS which opens in new window and handles financial transaction processing outside of this system.

#### Design gallery page
  * Displays shirt design and title in 'gallery' saved in database

  * Option to purchase design
    - takes user to order form page

### Possible additional Features
  1. Users create designer profile. Designer profile has gallery of user's designs like main gallery
  2. Allow users to add and format text only on shirt or with an uploaded image. Arrange both text and image elements in designer section.
  3. Full custom shirt design interface. This is mostly Javascript and it is a long-term goal of the project. I hope to investigate how I would accomplish this as part of my project, but it is not a listed goal for my final project.

### Data model

Database
  - Stores page templates
  - Stores shirt design database
    * shirt title, text of output, color of shirt, processed image size in pixels, original image, processed image
    * ? username
    * template parameters
      1. Python modules that will actually do the data transformation from the input parameters.

### Technical Components

Web Page html/css/js
  - Shirt designer section in Home page
    * Menu to select user action (upload image, select color for shirt and design)
    * Menu to select shirt color from palette - ? uses JS?
    * Option to rotate to 'front' or 'back' of shirt to place image
    * Apply changes

  - User can position and resize uploaded image on blank shirt
    * This involves JS
    * User can position and resize transformed image on blank shirt

  - Order/gallery upload form page
    * Users are displayed a final shirt design
    * Users choose to upload to gallery or upload to gallery *and* order shirts

  - Design gallery
    * Displays finished shirt design images in gallery form
    * Image links to order form for shirt

Python modules
  - ASCII art - converts image to grayscale then applies grid and substitutes alpha/numberic characters for image color in each grid returning a "ascii art" version of image
    * uses existing modules: pillow, PIL, numpy and module from 'Python playground'
  - Django module
    * Query database for pages to display
    * Make Classes for shirt design database columns and build SQL for queries
    * Interact with glitch, ASCII, and other direct image manipulation modules

### Timeline

Week 1: 5/2  - 5/6   | *Stage 1 & 2*
Week 2: 5/9  - 5/13  | *Stage 2 & 3*
Week 3: 5/16 - 5/20  | *Stage 3 & 4*
Week 4: 5/23 - 5/27  | *Stage 4 & 5*
Week 5: 5/30 - 6/3   | *Stage 5, 6, & 7*
Week 6: 6/6  - 6/9   | *review and refine*

####Stages

1. Make test page and initialize django database
  **Week 1**

2. Make test module for data transformation
  * Still deciding which module to make first
  * Options for first module
    1. upload image to shirt section, allow user to position and resize
    2. 'oregon trail' template, user adds text, output is fixed template with user text
  **Week 1 & 2**

3. Make shirt database and connect to functioning test module and page.
  * Begin testing first shirt design generator
  **Week 2 & 3**

4. Create and style site pages
  * home - start with *one* shirt design generator, ASCII art module
  * order form page
  * gallery page
  **Week 3 & 4**

5. Connect and test gallery and order page
  **Week 4 & 5**

6. Refine design and Set up order processing
  - Mostly outside of project scope...this is something that gives user an end point
  - Clicking on shirt in gallery takes user to order form for shirt
  **Week 5**

7. Add other design generators
    * Oregon Trail and glitch modules
    * Investigate full shirt designer interface
  **Week 5**

Extended Goal: Javascript interaction for shirt designer sections
  - I don't know exactly what to use and much work it takes
    * Resize and reposition image, alter generator effects via slide

Modules for extended Functionality
- oregon trail - takes base image and adds user-entered text to base image
- glitch - alters image by changing image file data directly to output altered version
  * uses existing modules: pillow, PIL, numpy, and github glitch module

Full site features:

1. Interactive custom tshirt designer
  * Users upload text, image, pic from clip art
2. Shirt generators
  * Templates for shirt designs with parameters user can set
  * Generators:
    * ASCII art - user uploads image, images is converted to ASCII art and rendered on the shirt
    * Oregon Trail - user inputs text, text is rendered along with vintage video game art
    * Glitch - users input image, image is altered via 'glitch' process that changes the appearance of the image
3. Marketplace
  * Users can upload designs they create to Marketplace
  * Any user can purchase shirt from marketplace, shirt creator gets percentage of sale
