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

XML, JSON, and HTML are all data delivery stack, but the differences are as follows:

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


## Assignment 3

**1. UserCreationForm in Django**

UserCreationForm is a built-in form class by Django for creating user registration forms in Django web applications.

Advantages:
1.	It helps us create sign-up forms quickly.
2.	It makes sure people type in usernames and passwords correctly.

Disadvantages:
1.	We will need to make it look nice with our own styles because it looks basic.
2.	It may not cover more complex user registration scenarios.

**2. Authentication and Authorization in Django Application**

Authentication involves confirming a user's identity, such as by checking their username and password.

Authorization involves deciding what a user is allowed to do once they are in, such as whether they are allowed to change or delete stuff.

Both are important because they work together to keep things secure. They work together to make sure important information is only seen and changed by the right people.

**3. Cookies in Website**

Cookies are small data files that are kept on a user's web browser when they are viewing a website They assist websites with remembering user information, such as username. Django uses cookies to keep track of users' identities when they visit a website. When the user log in, it writes a specific note (a session ID) on the computer. This note helps the website remember the user and the user’s stuff. Others cannot read or alter the note since it is secure.

**4. Are cookies secure to use? Is there potential risk to be aware of?**

Cookies are safe when we follow the rules, like keeping our data secret and using secure connections. Important cookie data must be concealed or encrypted for security reasons, and the website must employ a secure connection (HTTPS). Cookies, however, have the potential to expose the personal information or be utilised by hackers. Therefore, while using cookies on websites, it is crucial to adhere to security standards and consider privacy.

**5. Steps in implementing the task**

1. Implement registration, login, and logout functions to allow users to access the previous application.
   
   a. Creating a registration function
   
      I created a registration function in ```views.py``` within the ```main``` folder. Here's the code for the register function:

```def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

I also added three essential imports: redirect, UserCreationForm, and messages.

Next, I created a new HTML file named ```register.html``` within the main/templates folder and added the following code:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```
Lastly, I imported the register function in ```urls.py``` within the main folder and added a new path URL to the ```urlpatterns```, allowing access to this imported function.

   b. Creating a login function

   I created a login function in views.py within the main folder. Here's the code for the ```login_user``` function:
```
from django.contrib.auth import authenticate, login

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

Next, I created a new HTML file named ```login.html``` within the main/templates folder and added the following code:
```
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

Finally, I imported the ```login_user``` function in ```urls.py``` within the main folder and added a new path URL to the urlpatterns, allowing access to this imported function.

c. Creating a Logout Function

I added a logout function to ```views.py``` in the main directory by including the following code:
```
from django.contrib.auth import logout
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

I also integrated this code into the ```main.html``` file located in the main/templates folder:
```
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

inside ```main.html``` inside the main/template

Finally, I imported the ```logout_user``` function in ```urls.py``` within the main folder and added a new path URL to the urlpatterns, enabling access to this function.

2.  Create two user accounts with three dummy data entries for each account using the model previously created in the application.
   
I completed the registration form on the website using two different names, and for each account, I added three data entries by clicking the "add new product" button and filling out the product form.

3. Connect Item model with User.
   
To connect the Item model with the User, I imported the necessary code in the ```models.py``` file within the main subdirectory:
```
from django.contrib.auth.models import User
```
I then updated the existing Item model as follows:
```
class Product(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
```

I made modifications to the ```create_product``` function in ```views.py``` to:
```
def create_product(request):
form = ProductForm(request.POST or None)

if form.is_valid() and request.method == "POST":
    item = form.save(commit=False)
    item.user = request.user
    item.save()
    return HttpResponseRedirect(reverse('main:show_main'))
```
Additionally, I adjusted the ```show_main``` function in the following way:
```
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
```
I saved all the changes and ran the migrations for the model.


4. Display the information of the logged-in user, such as their username, and applying cookies, such as last login, on the main application page.

First, in the ```views.py``` file in the main directory, I imported the ```login_required``` code from ```django.contrib.auth.decorators```. This code ensures that only logged-in users can access the web page.
```
from django.contrib.auth.decorators import login_required
```

I applied the ```@login_required(login_url='/login')``` decorator above the ```show_main``` function to restrict access to authenticated users.

```
@login_required(login_url='/login')
```

To implement cookies:

After logging out from the website, I imported the necessary code to work with cookies. This included importing datetime and classes like HttpResponseRedirect and reverse from Django.

```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

I modified the ```login_user``` function. Inside the if user is not None block, I used the ```response.set_cookie``` method to set a "last_login" cookie with the current date and time.

```
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

In the show_main function, I added ```'last_login': request.COOKIES['last_login']``` to include the "last_login" cookie data in the response, which would be displayed on the web page.


then I modified the ```logout_user``` function to delete the "last_login" cookie upon logging out.

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Finally, I added the following code to the ```main.html``` template to display the last login session time:
```
<h5>Last login session: {{ last_login }}</h5>
```

## Assignment 1

**1. The Purpose of some CSS Element Selector**

A CSS element selector is used to select and apply a set of styles to all elements of a specific HTML tag type, such as p, h1, h2, a, and more. When we use an element selector, the chosen styles will be applied to every instance of that specific element type across your webpage. this maintains look consistency for those elements throughout the website.


**2. Some of the HTML5 tags**

<header>: This tag is located at the top of a webpage. It usually holds things like the website logo and menu buttons, making it easier for people to find their way around the site.

<button>: This tag creates a clickable button on a webpage. It's like the buttons we press on our phone or computer. we click it to do things, like sending a message or submitting a form.

<hr>: This tag adds a horizontal line to a webpage. It's like drawing a line from left to right. It's used to separate different parts of a page or make it look organized.


**3. Padding vs Margin**

Margin creates space outside of an element, creating space between elements, while padding creates space inside an element.


**3. Tailwind vs Bootstrap**

Tailwind CSS: we can choose it when we want to create a completely unique and custom look for the website, and if we do not mind starting from scratch.

Bootstrap: we can choose bootstrap when we want to save time by using ready-made designs and components. and it is good for creating a webpage with a consistent look.


**4. Steps in implementing the task**

I styled the first login page by adding a navbar to hold the logo. Then, I looked for a background image that matched my website's theme and used it as a cover for the login page. I created a card to contain the form and all its inputs, positioning the card in the center and adjusting the blur level to make it look better.

Styling the register page wasn't much different from how I styled the login page because I wanted to maintain a consistent design on my website when users are not logged in.

On the first main page, I started by making a sidebar on the left. I added stuff like a logo, lines, and links for 'dashboard' and 'logout.' I put the 'logout' link at the very bottom by adding 'bottom:30' in its css. And I also added icon images for 'dashboard' and 'logout' in the sidebar. I positioned the sidebar in 2 out of 12 sections. On the right side, I began with a welcoming message when the user is logged in. Then, I displayed the number of items that are already saved, designing it with a blue card and centering the text. After that, there is a table for inventory that I had created, a button for creating a product that changed color when hovered to make it more interactive, and I displayed the user's last login session. I kept it simple for easy user understanding and used two different colors for the table to make it clearer.

Styling the 'create_product' page was relatively brief. I added a navbar for the logo and the 'create_product' title using a card.

Throughout this website styling, I frequently used cards to make things look better.

