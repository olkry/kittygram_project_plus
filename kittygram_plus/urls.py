from django.urls import include, path

from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views

from cats.views import CatViewSet, OwnerViewSet, LightCatViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)
router.register(r'mycats', LightCatViewSet, basename='mycats')

urlpatterns = [
    path('', include(router.urls)),
    # path('api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]


'''
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0OTI5Njk5MSwiaWF0IjoxNzQ5MjEwNTkxLCJqdGkiOiJiN2YwMDkxOTg5MDE0YjEzYjE0NGE5NTM4MjcwOWNmYSIsInVzZXJfaWQiOjF9.yeIjuJz4_BXfnal6iL-MQ6dqUfcczR9q9uYPiQFPSOU",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5Mjk2OTkxLCJpYXQiOjE3NDkyMTA1OTEsImp0aSI6IjE1MTA1N2NlNGJmNTQyZDNiMTcxM2I4NGFjMTA5Y2NiIiwidXNlcl9pZCI6MX0.-yLK0GJdzmc5ARnR1JbiyM46WDLUdB-jddLMUxCZ03A"
}
'''
