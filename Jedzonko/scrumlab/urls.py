"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin


from jedzonko import views as v

urlpatterns = [
    path('', v.LandingPageView.as_view(), name='landing_page'),
    path('admin/', admin.site.urls),
    path('page/<slug:slug>/', v.PageDetailView.as_view(), name='page_detail'),
    path('main/', v.DashboardView.as_view(), name='dashboard'),
    path('recipe/<int:id>/', v.RecipeDetailsView.as_view(), name='recipe_details'),
    path('recipe/list/', v.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/add/', v.RecipeAddView.as_view(), name='recipe_add'),
    path('recipe/modify/<int:id>/', v.RecipeModifyView.as_view(), name='recipe_modify_id'),
    path('plan/<int:id>/', v.PlanDetailsView.as_view(), name='plan_details'),
    path('plan/list/', v.PlanListView.as_view(), name='plan_list'),
    path('plan/add/', v.PlanAddView.as_view(), name='plan_add'),
    path('plan/add-recipe/', v.PlanAddRecipeView.as_view(), name='plan_add-recipe'),
    path('plan/modify/<int:plan_id>/', v.PlanModifyView.as_view(), name='plan_modify_id'),
]
