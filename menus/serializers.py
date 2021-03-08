from rest_framework import serializers
from menus.models import Menu, Dish


class MenuSerializer(serializers.ModelSerializer):
    dish_count = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'dish_count', 'created_date', 'updated_date')
        read_only_fields = ('created_date', 'updated_date')


class MenuIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', )


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'price', 'prepare_time_minutes', 'menu', 'is_vegetarian',
                  'created_date', 'updated_date')
        read_only_fields = ('created_date', 'updated_date')

    def to_representation(self, instance):
        self.fields['menu'] = MenuIdSerializer(read_only=True)
        return super(DishSerializer, self).to_representation(instance)


class MenuDetailSerializer(serializers.ModelSerializer):
    dish_set = DishSerializer(many=True, read_only=True)
    dish_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'description', 'dish_count', 'dish_set', 'created_date', 'updated_date')
        read_only_fields = ('created_date', 'updated_date')
