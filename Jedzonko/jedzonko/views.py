from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import DayName, Recipe, RecipePlan, Page, Plan
from random import shuffle



class LandingPageView(View):

    def get(self, request):
        recipes = Recipe.objects.all()
        recipes_list = [r for r in recipes]
        shuffle(recipes_list)

        context = {
            'recipe': recipes_list[:3],
        }

        try:
            page1 = get_object_or_404(Page, slug='contact')
            page2 = get_object_or_404(Page, slug='about')
            context['page1'] = page1
            context['page2'] = page2
        except Http404:
            pass

        return render(request, "index.html", context)


class PageDetailView(View):

    def get(self, request, slug):
        page = get_object_or_404(Page, slug=slug)
        ctx = {
            'page': page
        }
        return render(request, 'page.html', ctx)


class DashboardView(View):

    def get(self, request):
        plans = Plan.objects.all().order_by('-created')
        quantity_plans = plans.count()
        quantity_recipes = Recipe.objects.all().count()
        recipes_latest_plan = RecipePlan.objects.all().filter(plan=plans[0]).order_by('order')
        day_name = [day for day in list(DayName)]
        recipe_day = [recipe.day_name for recipe in recipes_latest_plan]
        plan_day = [day for day in day_name if day.name in recipe_day]

        context = {
            "quantity_plans": quantity_plans,
            "quantity_recipes": quantity_recipes,
            "latest_plan": plans[0],
            "recipes_latest_plan": recipes_latest_plan,
            "plan_day": plan_day,
        }
        return render(request, "dashboard.html", context)


class RecipeDetailsView(View):

    def get(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        recipesarr = recipe.ingredients.split("\r\n")
        context = {
            'recipe': recipe,
            'ingredients': recipesarr
        }
        return render(request, "app-recipe-details.html", context)

    def post(self, request, id):
        recipes = get_object_or_404(Recipe, id=id)
        if request.POST.get("like") == 'like':
            recipes.votes += 1
            recipes.save()
        elif request.POST.get("like") == 'unlike':
            recipes.votes -= 1
            recipes.save()
        return RecipeDetailsView().get(request, id)


class RecipeListView(View):

    def get(self, request):

        search_query = request.GET.get('search', '')
        if search_query:
            recipes = Recipe.objects.filter(Q(name__icontains=search_query))
        else:
            recipes = Recipe.objects.all().order_by("-votes", "created")
        recipes_paginator = Paginator(recipes, 50)
        page_num = request.GET.get('page')
        page = recipes_paginator.get_page(page_num)
        paginator_page = recipes_paginator.page_range

        context = {
            'count': recipes_paginator,
            'page': page,
            'paginator': paginator_page
        }
        return render(request, "app-recipes.html", context)


class RecipeAddView(View):

    def get(self, request):
        return render(request, "app-add-recipe.html")

    def post(self, request):
        recipe_name = request.POST.get('name')
        recipe_description = request.POST.get('description')
        recipe_preparation_time = request.POST.get('preparation_time')
        recipe_ingredients = request.POST.get('ingredients')
        recipe_preparation_description = request.POST.get('preparation_description')
        if recipe_name != '' and recipe_description != '' and recipe_preparation_time != '' \
                and recipe_ingredients != '' and recipe_preparation_description != '':
            try:
                recipe_preparation_time = int(recipe_preparation_time)

                Recipe.objects.create(
                    name=recipe_name,
                    description=recipe_description,
                    preparation_time=recipe_preparation_time,
                    ingredients=recipe_ingredients,
                    preparation_description=recipe_preparation_description,
                )
                return RecipeListView().get(request)
            except ValueError:
                messages.error(request, "Błędne dane !!")
                return redirect('/recipe/add/')
        else:
            messages.error(request, "Uzupełnij wszystkie pola!!")
            return redirect('/recipe/add/')


class RecipeModifyView(View):

    def get(self, request, id):
        recipes = get_object_or_404(Recipe, id=id)
        context = {
            'recipe': recipes,
        }
        return render(request, 'app-edit-recipe.html', context)

    def post(self, request, id):
        recipe = get_object_or_404(Recipe, id=id)
        recipe_name = request.POST.get('name')
        recipe_description = request.POST.get('description')
        recipe_preparation_time = request.POST.get('preparation_time')
        recipe_ingredients = request.POST.get('ingredients')
        recipe_preparation_description = request.POST.get('preparation_description')
        if recipe_name != '' and recipe_description != '' and recipe_preparation_time != '' \
                and recipe_ingredients != '' and recipe_preparation_description != '':
            try:
                recipe_preparation_time = int(recipe_preparation_time)

                recipe.name = recipe_name
                recipe.description = recipe_description
                recipe.preparation_time = recipe_preparation_time
                recipe.ingredients = recipe_ingredients
                recipe.preparation_description = recipe_preparation_description
                recipe.save()
                return RecipeListView().get(request)
            except ValueError:
                messages.error(request, "Błędne dane !!")
                return RecipeModifyView().get(request, id)
        else:
            messages.error(request, "Uzupełnij wszystkie pola!!")
            return RecipeModifyView().get(request, id)


class PlanDetailsView(View):

    def get(self, request, id):
        plan = get_object_or_404(Plan, id=id)
        recipes_plan = RecipePlan.objects.all().filter(plan=plan).order_by('order')
        day_name = [day for day in list(DayName)]
        recipe_day = [recipe.day_name for recipe in recipes_plan]
        plan_day = [day for day in day_name if day.name in recipe_day]

        context = {
            "plan": plan,
            "recipes_plan": recipes_plan,
            "plan_day": plan_day,
        }
        return render(request, 'app-details-schedules.html', context)

    def post(self, request, id):
        recipe_plan = get_object_or_404(RecipePlan, pk=request.POST.get('recipe_plan'))
        recipe_plan.delete()
        return PlanDetailsView().get(request, id)


class PlanListView(View):

    def get(self, request):
        plans = Plan.objects.all().order_by('name')
        plan_paginator = Paginator(plans, 50)
        page_num = request.GET.get('page')
        page = plan_paginator.get_page(page_num)
        content = {
            'plan_paginator': plan_paginator,
            'page': page
        }
        return render(request, "app-schedules.html", content)


class PlanAddView(View):

    def get(self, request):
        return render(request, 'app-add-schedules.html')

    def post(self, request):
        plan_name = request.POST.get('plan_name')
        plan_description = request.POST.get('description_plan')

        if len(plan_name) == 0 or len(plan_description) == 0:
            message = 'Uzupełnij wszystkie pola !'
            content = {
                'message': message,
            }
            return render(request, 'app-add-schedules.html', content)
        elif len(plan_name) > 64:
            message = 'Nazwa planu jest za długa (max 64 znaki) !'
            content = {
                'message': message,
            }
            return render(request, 'app-add-schedules.html', content)
        else:
            new_plan = Plan.objects.create(name=plan_name, description=plan_description)
            return PlanDetailsView().get(request, new_plan.pk)


class PlanAddRecipeView(View):

    def get(self, request, message=None):
        recipe = Recipe.objects.all()
        plan = Plan.objects.all()
        day_name = list(DayName)
        ctx = {
            'recipe': recipe,
            'plan': plan,
            'day_name': day_name,
            'message': message
        }
        return render(request, 'app-schedules-meal-recipe.html', ctx)

    def post(self, request):
        plan_meal_name = request.POST.get('meal_name')
        recipe_plan = get_object_or_404(Plan, pk=request.POST.get('plan'))
        plan_order = request.POST.get('order')
        plan_recipe = get_object_or_404(Recipe, pk=request.POST.get('recipe'))
        day_name = request.POST.get('day_name')

        if plan_meal_name != "" and plan_order != "" and day_name != "":
            try:
                order = int(plan_order)
                if day_name not in [day.name for day in DayName]:
                    raise ValueError

                RecipePlan.objects.create(
                    meal_name=plan_meal_name,
                    recipe=plan_recipe,
                    order=order,
                    plan=recipe_plan,
                    day_name=day_name
                )
                return PlanDetailsView().get(request, recipe_plan.pk)

            except ValueError:
                message = "Błędne dane !"
                return PlanAddRecipeView().get(request, message)

        else:
            message = "Uzupełnij wszystkie pola !"
            return PlanAddRecipeView().get(request, message)


class PlanModifyView(View):

    def get(self, request, plan_id):
        plan = get_object_or_404(Plan, pk=plan_id)
        context = {
            'plan': plan
        }
        return render(request, "app-edit-schedules.html", context)

    def post(self, request, plan_id):
        plan = get_object_or_404(Plan, pk=plan_id)
        plan_name = request.POST.get('planName')
        plan_description = request.POST.get('planDescription')

        if plan_name != '' and plan_description != '':
            if len(plan_name) > 64:
                messages.error(request, "Nazwa planu jest za długa (max 64 znaki) !")
                return PlanModifyView().get(request, plan.pk)
            else:
                plan.name = plan_name
                plan.description = plan_description
                plan.save()
                return PlanDetailsView().get(request, plan.pk)
        else:
            messages.error(request, "Uzupełnij wszystkie pola !")
            return PlanModifyView().get(request, plan.pk)
