from rest_framework import routers
from menus.views import MenuViewset, DishViewset

router = routers.DefaultRouter()
router.register(r'menu', MenuViewset)
router.register(r'dish', DishViewset)