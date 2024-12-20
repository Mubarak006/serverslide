# Ex.05 Design a Website for Server Side Processing
## Date:27-11-24

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
~~~
math.html

<html>
    <head>
        <style>
            body {
                background: linear-gradient(135deg, #2C3E50, #061320);
                background-repeat: no-repeat;
                background-size: cover;
                background-position: center;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100vh;
                
            }

            h1 {
                color: green ;
                font-style: oblique;
                text-align: center;
                font-size: 70;
                

            }

            .inputs {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                background-color: red (211, 211, 211, 0.278);
                width: 400px;
                height: 300px;
                padding: 20px;
                border-radius: 10px;
            }

            form {
                display: flex;
                flex-direction: column;
                width: 100%;
                gap: 10px;
            }

            label {
                font-size: 20px;
                color: rgb(255, 234, 0);
            }

            input {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 14px;
                width: 100%;
            }

            button {
                padding: 10px;
                background-color:  violet (0, 94, 255);
                color: red;
                border: none;
                border-radius: 5px;
                font-size: 14px;
            }



        </style>
    </head>
    <body>
        <h1>Power of a lamp filament </h1><br>
        <h2>MUBARAK R (24900694)</h2>
        <div class="inputs">
            <form method="POST">
                {% csrf_token %}
                <label for="input1">Enter the intensity of the bulb:</label>
                <input type="text" id="input1" name="intensity" placeholder="Enter Intensity" value="{{I}}"></input>(in Wm<sup>2</sup>)<br/>
                <label for="input2">Enter the resistance of the bulb</label>
                <input type="text" id="input2" name="resistance" placeholder="Enter Resistance" value="{{R}}"></input>(in ohm)<br/>
                <button type="submit">Submit</button>
            </form>
            <label for="ans">Answer: </label>
            <input type="text" id="ans" value="{{power}}" readonly>
        </div>
    </body>
</html>


view.py

from django.shortcuts import render
def lightpower(request):
    context={}
    context['power'] = "0"
    context['i'] = "0"
    context['r'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        i = request.POST.get('intensity','0')
        r = request.POST.get('resistance','0')
        print('request=',request)
        print('intensity=',i)
        print('resistance=',r)
        power = (int(i) *int(i)) * (int(r))
        context['power'] = power
        context['i'] = i
        context['r'] = r
        print('power=',power)
    return render(request,'mathapp/math.html',context)

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('poweroflight/',views.lightpower,name="poweroflight"),
    path('',views.lightpower,name="poweroflightroot")
]
~~~

## SERVER SIDE PROCESSING:
![alt text](<Screenshot (80).png>)


## HOMEPAGE:
![alt text](<Screenshot (81).png>)


## RESULT:
The program for performing server side processing is completed successfully.
