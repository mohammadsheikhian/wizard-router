from nanohttp import context
from nanohttp.contexts import Context
from restfulpy.orm import DBSession
from sqlalchemy_media import StoreManager

from .models import MyCard, OtherCard


def insert(): # pragma: no cover

    my_card1 = MyCard(
        title='my card 1',
        avatar='https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto/gigs/59968744/original/6d9924b6f58a09e5b9c64feb39b557e96f4a765b/give-you-a-one-dollar-virtual-bank-card.jpg',
    )
    DBSession.add(my_card1)

    my_card2 = MyCard(
        title='my card 2',
        avatar='https://www.themelooks.org/club/crypcard/wp-content/uploads/2018/11/1529504445888.jpg',
    )
    DBSession.add(my_card2)

    my_card3 = MyCard(
        title='my card 3',
        avatar='https://theexchange.africa/wp-content/uploads/2018/09/Visa.jpg',
    )
    DBSession.add(my_card3)

    my_card4 = MyCard(
        title='my card 4',
        avatar='https://techcrunch.com/wp-content/uploads/2017/04/biometric_040517.jpg?w=730&crop=1',
    )
    DBSession.add(my_card4)

    my_card5 = MyCard(
        title='my card 5',
        avatar='https://www.themelooks.org/club/crypcard/wp-content/uploads/2018/11/1529504445888.jpg',
    )
    DBSession.add(my_card5)

    other_card_1 = OtherCard(
        title='other card 1',
    )
    DBSession.add(other_card_1)

    other_card_2 = OtherCard(
        title='other card 2',
        avatar='https://ecobank.com/img/eco/Ecobank_Card_PAC-Prepaid_SalaryXPress_EN_MGD_HR.png',
    )
    DBSession.add(other_card_2)

    other_card_3 = OtherCard(
        title='other card 3',
        avatar='https://techcrunch.com/wp-content/uploads/2017/04/biometric_040517.jpg?w=730&crop=1',
    )
    DBSession.add(other_card_3)
    DBSession.commit()
