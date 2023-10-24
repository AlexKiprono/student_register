from django.db import models

# Create your models here.

class Student(models.Model):
    image         = models.ImageField()
    firstname     = models.CharField(max_length=255)
    lastname      = models.CharField(max_length=255)
    email         = models.EmailField(max_length=255, unique=True)
    adm_no        = models.CharField(max_length=255,unique=True)
    grade         = models.CharField(max_length=255)
    status        = models.CharField(max_length=255)
    date_joined   = models.DateField(max_length=255)
    
    def __str__(self):
        return self.firstname




# {% load static %}
# <!DOCTYPE html>
# <html lang="en">

# <head>
#   <meta charset="utf-8">
#   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#   <link rel="apple-touch-icon" sizes="76x76" href="{% static 'img/apple-icon.png' %}">
#   <link rel="icon" type="image/png" href="{% static 'img/favicon.png' %}">
#   <title>HOME</title>
  
#   <!-- Fonts and icons -->
#   <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700" rel="stylesheet">
  
#   <!-- Nucleo Icons -->
#   <link href="{% static 'css/nucleo-icons.css' %}" rel="stylesheet">
#   <link href="{% static 'css/nucleo-svg.css' %}" rel="stylesheet">
  
#   <!-- Font Awesome Icons -->
#   <script src="https://kit.fontawesome.com/42d5adcbca.js" crossorigin="anonymous"></script>
  
#   <!-- CSS Files -->
#   <link id="pagestyle" href="{% static 'css/argon-dashboard.css' %}" rel="stylesheet">
# </head>

# <body>
#   {% for message in messages %}
#     <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
#       <strong>Message:</strong> {{ message }}
#       <button type="button" class="close" data-dismiss="alert" aria-label="Close"></button>
#       <span aria-hidden="true">&times;</span>
#     </div>
#   {% endfor %}

#   <div class="container">
#     {% if user.is_authenticated %}
#       <h3>Hello</h3>
#       <h4>You're successfully logged in</h4>
#       <a href="{% url 'sign_out' %}">
#         <div class="shadow p-3 mb-5 bg-body-tertiary rounded">Get Started</div>
#       </a>
#     {% else %}
#       <div class="row">
#         <div class="col-xl-4 col-lg-5 col-md-7 d-flex flex-column mx-lg-0 mx-auto">
#           <div class="card card-plain pb-5 text-start">
#             <div class="card-header pb-5 text-start">
#               <h1>Hello,<br>Welcome to My Django Website!</h1>
#               <br>
#               <br>
#               <h4>Please log in</h4>
#             </div>
#           </div>
#         </div>
#         <div class="col-6 d-lg-flex d-none h-100 my-auto pe-0 position-absolute top-0 end-0 text-center justify-content-center flex-column">
#           <div class="position-relative h-100 m-3 px-7 border-radius-lg d-flex flex-column justify-content-center overflow-hidden">
#             <span class="mask opacity-6"></span>
            
#             <a href="{% url 'sign_in' %}">
#               <button type="button" class="shadow p-3 mb-5 bg-body-tertiary rounded">SIGN IN</button>
#             </a>
#             <br>
#             <a href="{% url 'sign_up' %}">
#               <button type="button" class="shadow p-3 mb-5 bg-body-tertiary rounded">SIGN UP</button>
#             </a>
#           </div>
#         </div>
#       </div>
#     {% endif %}
#   </div>
# </body>
# </html>
