from restfulpy.orm import DeclarativeBase, Field, SoftDeleteMixin, \
    ModifiedMixin, FilteringMixin, PaginationMixin, OrderingMixin
from sqlalchemy import Integer, String, Unicode


class Card(ModifiedMixin, OrderingMixin, FilteringMixin, PaginationMixin,
           SoftDeleteMixin, DeclarativeBase):

    __tablename__ = 'card'

    type_ = Field(String(50))
    __mapper_args__ = {
        'polymorphic_on': type_,
        'polymorphic_identity': __tablename__
    }

    id = Field(
        Integer,
        primary_key=True,
        readonly=True,
        not_none=True,
    )
    title = Field(
        Unicode(20),
        nullable=False,
        not_none=True,
    )
    avatar = Field(
        Unicode,
        nullable=True,
        not_none=False,
    )
    cvv2 = Field(
        Unicode(20),
        nullable=True,
        not_none=False,
    )
    description = Field(
        Unicode(20),
        nullable=True,
        not_none=False,
    )


class OtherCard(Card):
    __mapper_args__ = {'polymorphic_identity': 'other'}


class MyCard(Card):
    __mapper_args__ = {'polymorphic_identity': 'my'}

