from nanohttp import context
from nanohttp.contexts import Context
from restfulpy.orm import DBSession
from sqlalchemy_media import StoreManager

from .models import MyCard, OtherCard


def insert(): # pragma: no cover

    my_card1 = MyCard(
        name='my card 1',
    )
    DBSession.add(my_card1)

    my_card2 = MyCard(
        name='my card 2',
    )
    DBSession.add(my_card2)

    my_card3 = MyCard(
        name='my card 3',
    )
    DBSession.add(my_card3)

    my_card4 = MyCard(
        name='my card 4',
    )
    DBSession.add(my_card4)

    my_card5 = MyCard(
        name='my card 5',
    )
    DBSession.add(my_card5)

    other_card_1 = OtherCard(
        name='other card 1',
    )
    DBSession.add(other_card_1)

    other_card_2 = OtherCard(
        name='other card 2',
    )
    DBSession.add(other_card_2)

    other_card_3 = OtherCard(
        name='other card 3',
    )
    DBSession.add(other_card_3)
    DBSession.commit()
