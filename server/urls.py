"""
URL configuration for server project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from App import views
from rest_framework.routers import DefaultRouter
from App.views import QuestionViewSet

# Create a simple health check view
def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'message': 'CodeCraft Server is running!'
    })

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)  # Register your viewset with a proper prefix

urlpatterns = [
    path('', health_check, name='health_check'),  # Root endpoint for health checks
    path('admin/', admin.site.urls),
    path('api/languages/', views.GetLanguagesView.as_view(), name='get_languages'),
    path('api/compile/', views.CompileCodeView.as_view(), name='compile_code'),
    path('api/hints/', views.GenerateHintsView.as_view(), name='generate_hints'),
    path('api/askAI/', views.AskAIView.as_view(), name='ask_ai'),
    path('api/', include(router.urls)),  # Register the Question API endpoint under /api/
]