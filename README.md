# inventory_list


| Data | Information     |     
| :---:   | :---: | 
| **Website URL** |https://inventorymanagement.adaptable.app | 


## Assignment 1

**1. Steps in implementing the task**
1. Create a new Django project.
   
To create a new Django project, I first created a new directory on my desktop, namely 'inventory_list.' Next, I opened the terminal inside that directory and created a virtual environment by running ```python -m venv env```. Afterward, I activated the virtual environment by running ```source env/bin/activate``` and created a 'requirements.txt' file in that directory. I installed the necessary dependencies using ```pip install -r requirements.txt```, Finally, I used ```django-admin startproject inventory_list .``` to create the Django project. After creating it, I opened the folder in Visual Studio Code and edited the 'ALLOWED_HOSTS'  in 'settings.py' to be ```ALLOWED_HOSTS = ["*"]```. I then deactivated the virtual environment.
After completing these steps, I created a '.gitignore' file in the 'inventory_list' directory.

2. Create an app with the name 'main' in that project.
   
I created the 'main' app by running ```python manage.py startapp main``` and registered it by adding ```main,``` to the 'INSTALLED_APPS' in the 'settings.py' file located in the 'inventory_list' project directory.

3. Create a URL routing configuration to access the 'main' app.
   
first, I added the following code to the 'urls.py' file in the 'inventory_list' directory:

```
from django.urls import path, include
```
And then, I added the following line to the 'urlpatterns' list:

```
path('', include('main.urls')),
```

Next, I configured the URL routing for my 'main' app. First, I created a 'urls.py' file inside the 'main' app and imported ```from main.views import show_main``` and added ```path('', show_main, name='show_main')``` in the url patterns
With these steps, I successfully created the 'main' app in my Django project and configured URL routing to access it.

4. Create a model in the 'main' app with the name 'Item' and the following mandatory attributes:
   
First, I added the following code to the 'models.py' file in the 'main' application directory:

```
from django.db import models

class Item(models.Model):
...
```
  
and add the attributes with their own types
    
Next, I created model migrations by running the following commands in the terminal:

```
python manage.py makemigrations
python manage.py migrate
```
These commands generated and applied the migrations for the 'Item' model to the local database.

5. Create a function in views.py that returns an HTML template containing your application name, your name, and your class.
   
First, I created the HTML file in a new directory called "templates" inside the main application. Then, I connected views to templates by adding ```from django.shortcuts import render``` in the views.py file located in the main application and added the following code:

```
def show_main(request):

    context = {
    
        'name': 'Tiva Adhisti Nafira Putri',
        
        'class': 'PBP KI'
        
    }
    
    return render(request, 'main.html', context)
```
    
Afterward, I modified the main.html file

6. Create a routing in urls.py to map the function in views.py to an URL.

I added the following code to the urls.py file inside the main app:

```
from django.urls import path
from main.views import show_main

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    ]
```
    
Additionally, I defined the URL patterns inside the urls.py file inside the project's shopping_list directory using path() as follows:

```
path('main/', include('main.urls')),
```

7. Deploy your app to Adaptable so it can be accessed through the internet.
   
Before deploying, I created a new repository on GitHub named "inventory_list" and pushed the "inventory_list" in my local directory to that repository.
Since I had already connected Adaptable.io with GitHub, I chose the "inventory_list" repository as the basis for the application to be deployed and selected the master branch. For the deployment template, I chose the Python App Template, and for the database type, I selected PostgreSQL. Next, I adjusted the Python version and entered the following command in the start command section: "python manage.py migrate && gunicorn shopping_list.wsgi". I also entered the application name and finally deployed the application.

8. Create a README.md.
    
I created the README.md before pushing "inventory_list" to GitHub. I created it using a text editor and placed it in the same directory as "inventory_list."

**2. Flow of Client Requests to a Django Web App and Its Response**

![Flow Diagram](https://github.com/tvadhisti/inventory_list/assets/127074983/b15b12e1-5a40-4417-be6f-923ce340c6ba)


**3. Definition of Virtual Environment**

A virtual environment is an isolated space for the package and dependencies. It manages dependencies and separates project packages from each other. We can create a Django web application without a virtual environment but this may cause conflicts.

**4. MVC, MVT, and MVVM**

MVC, MVT, and MVVM are three popular design patterns in software development

1. MVC (Model-View-Controller) -> common in traditional web and desktop applications

Model: stores the application data

View: displays data

Controller: manages communication between Model and View

2. MVT (Model-View-Template) -> used in web frameworks like Django
   
Model: stores the application data

View: displays data

Template: defines how data is displayed (e.g. HTML)

3. MVVM (Model-View-ViewModel) -> common in modern web applications.
   
Model: stores the application data

View: displays data

ViewModel: it serves as a link between the model and the view and it handles UI logic


## Assignment 2

**1. GET Form vs POST Form in Django**

GET: Data is sent in the URL, which can make it visible, and it is stored in the browser history. It is suitable for non sensitive data and it has URL length limitations.

POST: Data is sent in the background, not visible in the URL, and not stored in the browser history. It is suitable for sensitive data, like usernames and passwords, and has no limitation on the length of the values.

**2. XML vs JSON vs HTML**

XML, JSON, and HTML are all data delivery stack, but the differences are:

1. XML was designed to carry data and it is good to use when data structure flexibility and readability are important

2. JSON is used for lightweight data exchange and it is good for APIs and data sent between a web server and a web app

3. HTML is used for creating web pages and it focuses on how content looks and is presented

**3. Why is JSON often used in data exchange between modern web applications?**

JSON provides simplicity and readability. It is easy to understand for both humans and machines. The syntax consists of key-value pairs and arrays. It works well with any programming language and is perfect for web applications, especially those that use JavaScript.

**4. Steps in implementing the task**
1. Create a form input to add a model object to the previous app

Firstly, I created a folder called 'templates' in the root directory and designed a ```base.html``` template to serve as the foundational structure for my website. Next, I made modifications to the ```settings.py``` file located in the 'inventory_list' directory, updating it to include the line: ```'DIRS': [BASE_DIR / 'templates'],```. Following that, I made adjustments to the ```main.html``` file to utilize ```base.html``` as its template.

Next, I created ```forms.py``` inside ```main``` folder and added the following code:

```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "description"]

```

I also added  additional imports in the ```views.py``` file, located within the ```main``` folder. Afterward, I created a new function:
```
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```

Following this, I added the following two lines within the ```show_main``` function:
```
items = Item.objects.all()
```
```
'items': items
```

I also imported the ```create_product``` function within the ```urls.py``` file located in the ```main``` folder and included the following code:
```path('create-product', create_product, name='create_product'),```

Lastly, I created a new file named ```create_product.html```. This code represents a webpage template designed for adding a new product. It extends another template called ```base.html```. 

Additionally, I inserted codes into ```main.html``` to display product data in a table format and included a button for redirection to the form page.

2. Add 5 views to view the added objects in HTML, XML, JSON, XML by ID, and JSON by ID formats.

I started with XML. I imported the following into ```views.py``` within the ```main``` folder:
```
from django.http import HttpResponse
from django.core import serializers
````
I then created a function called ```show_xml``` that creates a variable to store all fetched 'Item' objects:
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
Next, i imported ```show_xml``` function in ```urls.py``` inside ```main``` folder and also added the path

Next, I worked on the JSON version. I followed the same steps in both ```views.py``` and ```urls.py```, but this time, I implemented it in JSON format instead of XML.


3. Create URL routing for each of the views added in point 2.
I created two functions:
```
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
I then imported these functions into ```urls.py``` within the ```main``` folder and added the following paths:
```
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```
These paths are used for routing XML and JSON requests with specific IDs.

**4. POSTMAN**

HTML
![Image 20-09-23 at 02 55](https://github.com/tvadhisti/inventory_list/assets/127074983/23711750-b858-447b-89ed-c1222bac23b6)

XML
![Image 20-09-23 at 02 58](https://github.com/tvadhisti/inventory_list/assets/127074983/72f2631c-d2cb-4a9b-b3cb-f2790c5cdcc1)
![Image 20-09-23 at 02 52](https://github.com/tvadhisti/inventory_list/assets/127074983/97886948-083e-4a57-8407-aa154e477595)

JSON
![Image 20-09-23 at 02 57](https://github.com/tvadhisti/inventory_list/assets/127074983/b5051ddf-4b7f-4350-892f-9a28948c8ece)
![Image 20-09-23 at 02 52 (3)](https://github.com/tvadhisti/inventory_list/assets/127074983/30dc8ade-b37e-49e7-946d-f06eb0f507cb)





