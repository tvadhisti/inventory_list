# inventory_list
**1. Steps in implementing the task**
1. Create a new Django project.
To create a new Django project, I first created a new directory on my desktop, namely 'inventory_list.' Next, I opened the terminal inside that directory and created a virtual environment by running "python -m venv env." Afterward, I activated the virtual environment by running "source env/bin/activate" and created a 'requirements.txt' file in that directory. I installed the necessary dependencies using "pip install -r requirements.txt." Finally, I used "django-admin startproject inventory_list ." to create the Django project. After creating it, I opened the folder in Visual Studio Code and edited the 'ALLOWED_HOSTS'  in 'settings.py' to be "ALLOWED_HOSTS = ["*"]." I then deactivated the virtual environment.
After completing these steps, I created a '.gitignore' file in the 'inventory_list' directory.

2. Create an app with the name 'main' in that project.
I created the 'main' app by running "python manage.py startapp main" and registered it by adding 'main' to the 'INSTALLED_APPS' list in the 'settings.py' file located in the 'inventory_list' project directory.

3. Create a URL routing configuration to access the 'main' app.
first, I added the following code to the 'urls.py' file in the 'inventory_list' directory:
from django.urls import path, include
And then, I added the following line to the 'urlpatterns' list:
path('', include('main.urls')),
Next, I configured the URL routing for my 'main' app. First, I created a 'urls.py' file inside the 'main' app and imported “from main.views import show_main and added path('', show_main, name='show_main') in the url patterns
With these steps, I successfully created the 'main' app in my Django project and configured URL routing to access it.

4. Create a model in the 'main' app with the name 'Item' and the following mandatory attributes:
First, I added the following code to the 'models.py' file in the 'main' application directory:
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
Next, I created model migrations by running the following commands in the terminal:
python manage.py makemigrations
python manage.py migrate

These commands generated and applied the migrations for the 'Item' model to the local database.

5. Create a function in views.py that returns an HTML template containing your application name, your name, and your class.
First, I created the HTML file in a new directory called "templates" inside the main application. Then, I connected views to templates by adding from django.shortcuts import render in the views.py file located in the main application and added the following code:
def show_main(request):
    context = {
        'name': 'Tiva Adhisti Nafira Putri',
        'class': 'PBP KI'
    }

    return render(request, 'main.html', context)
Afterward, I modified the main.html file as follows:
<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>


6. Create a routing in urls.py to map the function in views.py to an URL.
I added the following code to the urls.py file inside the main app:
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    ]
Additionally, I defined the URL patterns inside the urls.py file inside the project's shopping_list directory using path() as follows:
path('main/', include('main.urls')),

7. Deploy your app to Adaptable so it can be accessed through the internet.
Before deploying, I created a new repository on GitHub named "inventory_list" and pushed the "inventory_list" in my local directory to that repository.
Since I had already connected Adaptable.io with GitHub, I chose the "inventory_list" repository as the basis for the application to be deployed and selected the master branch. For the deployment template, I chose the Python App Template, and for the database type, I selected PostgreSQL. Next, I adjusted the Python version and entered the following command in the start command section: "python manage.py migrate && gunicorn shopping_list.wsgi". I also entered the application name and finally deployed the application.

8. Create a README.md. 
I created the README.md before pushing "inventory_list" to GitHub. I created it using a text editor and placed it in the same directory as "inventory_list."

**2. Flow Diagram**

![Flow Diagram](https://github.com/tvadhisti/inventory_list/assets/127074983/cb98328f-3b82-45f0-b4f2-a64fa8123692)

