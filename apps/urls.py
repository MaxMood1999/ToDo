from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from apps.views import RegisterView, LoginView
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
