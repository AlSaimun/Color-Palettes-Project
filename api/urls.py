from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ColorPaletteViewSet, FavoritePalettesViewSet,UserLoginView,ColorPaletteSearchListView,UpdatePalette

router = DefaultRouter()
router.register(r'palettes', ColorPaletteViewSet, basename='colorpalette')
router.register(r'favorites', FavoritePalettesViewSet, basename='favoritepalettes')

urlpatterns = [
    path('login/',UserLoginView.as_view),
    path('palettes/', ColorPaletteSearchListView.as_view(), name='palette_search'),
    path('palettes/update/<int:pk>/', UpdatePalette.as_view(), name='update_palette'),
    path('', include(router.urls)),
]
