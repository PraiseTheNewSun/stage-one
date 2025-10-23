import django_filters
from .models import StringModel

class StringFilter(django_filters.FilterSet):
    # Define a custom range filter for price
    min_length = django_filters.NumberFilter(field_name="min_length")
    max_length = django_filters.NumberFilter(field_name="max_length")
    is_palindrome = django_filters.BooleanFilter(field_name='is_palindrome')
    contains_character = django_filters.CharFilter(field_name='contains_character')
    word_count = django_filters.NumberFilter(field_name='word_count')

    class Meta:
        model = StringModel
        fields = '__all__'