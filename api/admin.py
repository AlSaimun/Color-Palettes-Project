from django.contrib import admin
from .models import ColorPalette, FavoritePalettes
#here register all model

class ColorPaletteAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_dominant_colors', 'display_accent_colors','last_update')
    
    def display_dominant_colors(self, obj):
        """convert all dominant colors to a string"""
        dominant_colors = obj.dominant_colors
        color_names = [item['name'] for item in dominant_colors]
        return ', '.join(color_names)
    display_dominant_colors.short_description = 'Dominant Colors'
    
    def display_accent_colors(self, obj):
        """convert all accent colors to a string"""
        accent_colors = obj.accent_colors
        colors = [item['color'] for item in accent_colors]
        return ', '.join(colors)
    display_accent_colors.short_description = 'Accent Colors'

admin.site.register(ColorPalette, ColorPaletteAdmin)
admin.site.register(FavoritePalettes)