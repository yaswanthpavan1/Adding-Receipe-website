from django.contrib import admin
from django.urls import path
from home.views import home, contact, about, yash_page
from django.conf import settings
from django.conf.urls.static import static
from vege.views import delete_recipe, recipes , update_recipe , login_page , register , logout_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('recipes/', recipes, name="recipes"),
    path('delete-recipe/<id>/', delete_recipe, name="delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name="update_recipe"),
    path('about/', about, name="about"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('register/', register, name="register"),

    path('yash-page/', yash_page, name='yash-page'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files (this line is unnecessary if you're not using a custom staticfiles_urlpatterns)
