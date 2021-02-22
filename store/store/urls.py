"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib         import admin
from django.urls            import path

from apps.cart.views        import *
from apps.core.views        import *
from apps.stores.views      import *

from apps.stores.api        import *


urlpatterns = [
    # frontpage urls start
    path('', frontPage, name="frontPage"),
    # frontpage urls end

    # cartPage urls start
    path('cart/', cartPage, name="cartPage"),
    # cartPage urls end

    # contactPage urls start
    path('contact/', contactPage, name="contactPage"),
    # contactPage urls end

    # aboutPage urls start
    path('about/', aboutPage, name="aboutPage"),
    # aboutPage urls end

    # stores api urls start
    path('api/add_to_cart/', api_add_to_cart, name="api_add_to_cart"),
    # stores api urls end

    # admin urls start
    path('admin/', admin.site.urls),
    path('<slug:category_slug>/<slug:slug>/', product_detail, name="product_detail"),
    path('<slug:slug>/', category_detail, name="category_detail")
    # admin urls end

]
