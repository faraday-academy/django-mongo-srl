from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import viewsets
from .models import Deck
from apps.cards.models import Card
from apps.cards.views import CardSerializer


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'


class DecksViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()


class DeckCardsViewSet(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all()

    def list(self, request, deck_pk):
        cards = Card.objects.filter(deck=deck_pk)
        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)
