from rest_framework import serializers
from .models import ColorPalette, FavoritePalettes

class ColorPaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorPalette
        fields = '__all__'
    def update(self, instance, validated_data): 
        """For update Color palettes"""
        instance.name = validated_data.get('name', instance.name)
        instance.dominant_colors = validated_data.get('dominant_colors', instance.dominant_colors)
        instance.accent_colors = validated_data.get('accent_colors', instance.accent_colors)
        instance.save()
        return instance

class FavoritePalettesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePalettes
        fields = '__all__'
