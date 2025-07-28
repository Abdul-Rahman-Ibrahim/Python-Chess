from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import HomeView, LegalMoveValidationView, ResetView, GetLegalMoveView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('check-move/', csrf_exempt(LegalMoveValidationView.as_view()), name='move-validator'),
    path('reset/', ResetView.as_view(), name='reset'),
    path('legal-move/', csrf_exempt(GetLegalMoveView.as_view()), name='legal-move'),
]