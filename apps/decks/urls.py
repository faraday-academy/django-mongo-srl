from django.urls import include, path
from rest_framework_nested import routers

from .views import (
    DecksViewSet,
    DeckCardsViewSet
)

router = routers.SimpleRouter()
router.register('', DecksViewSet)

# register a `/decks/:id/cards` url here
cards_router = routers.NestedSimpleRouter(router, '', lookup='deck')
cards_router.register('cards', DeckCardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cards_router.urls)),
]
