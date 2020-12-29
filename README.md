# Milestone 4 | Geezer.com 

##### What does it do and what does it need to fulfill?
This Milestone Project serves as the completion of the Full Stack
Web Developer Course offered by Code Institute.
It implements HTML5, CSS3, Javascript, and Python.
This application allows a shopper to search for products
related to comic books and sports collectible items in an
e-commerce store. The site also allows an administrator to
edit and delete shopping items.

### Practicality of Project:
The application uses Django 3, encouraging rapid development in 
a model-template-view architecture pattern. The project utilizes
SQLite3 database dependency and is managed via Git and Github. 
It is deployed to Heroku. 

##### The Stripe online payment system
was used for this e-commerce website. Sample/Test credit card numbers can 
be used when utilizing <a href="https://stripe.com/docs/testing#cards">this</a>
site.

#### User Stories 
_Generic (unregistered site user) User:
As a generic user...
I want to be able to view a list of products for 
sale so that I can select some for purchase.
I want to be able to view a category of 
products for sale so that I can find what 
i'm looking for.
I want to be able to view individual product details.
I want to identify any deals that may be 
available so that I can save money on my 
purchases.
I want to sort the available products so that I can Identify the best 
product for me.
_Registered User:
I want to easily register for membership to the site so that I can 
check past purchases.
I want to be able to save my payment method
I want to be able to view items in my shopping bag.
I want to be able to adjust quantitites of items in my 
bag.
I want to feel my personal payment 
information is secure.
I want to be able to recover my password easily.
_Admin & Store Management (Superuser):   
I want to add a 
product so I can add new items in my store. 
I want to edit/update/delete products as 
they become available or go out of stock 
so that I can manage my site correctly 
for shoppers. 
I want to be able to edit 
images, product prices, descriptions and 
other product criteria.

#### Design
The site is simple and has a straight-forward
splash page that gets a visitor "up and going" in regards
to shopping the site. The navigation is also a "no frills"
and simplistic way of getting around the site. 

#### Font
Roboto was used as a font and sans-serif was used as a backup.

#### Wireframing and Entity Relationship Diagrams
Both are available in the main files as:
    _Milestone_4_ERMD.pdf and
    _Milestone-4-Wireframes.pdf

#### Languages, Frameworks, Editors & Version Control:

* HTML, CSS, JS & Python ~ core languages used to create this multi-page CRUD application.
* <a href="https://www.djangoproject.com/">Django</a> ~ Used as the architectural engine following the model-template-view approach.
* <a href="https://getbootstrap.com/"> Bootstrap Framework</a> ~ Used as the core structuring layout for the application, ensuring mobile-first design and screen size fluidity.
* Bootstrap's <a href="https://getbootstrap.com/docs/4.3/getting-started/introduction/#js">Imported Javascript & JQuery</a> ~ For the Modal and Responsive Navbar expand & collapse functionality.
* <a href="https://git-scm.com/">Git</a> ~ Installed on local device and integrated to PyCharm as a Plugin to enable version controlling.
* <a href="https://www.heroku.com/">Heroku</a> ~ A cloud platform as a service enabling deployment for this CRUD application.