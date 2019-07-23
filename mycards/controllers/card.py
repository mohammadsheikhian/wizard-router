from nanohttp import json, HTTPNotFound, int_or_notfound
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession

from ..models.card import Card


class CardController(ModelRestController):
    __model__ = Card

    @json
    @Card.expose
    def get(self):
        return DBSession.query(Card)

#    @json(prevent_form='709 Form Not Allowed')
#    @Card.expose
#    def get(self, id):
#        id = int_or_notfound(id)
#        card = DBSession.query(Card).get(id)
#        if not member:
#            raise HTTPNotFound()
#
#        return card
#
