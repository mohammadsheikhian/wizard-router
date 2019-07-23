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
        required=False,
        label='ID',
        minimum=1,
        example=1,
        protected=False,
    )
    name = Field(
        Unicode(20),
        nullable=True,
        not_none=False,
        python_type=str,
        min_length=3,
        max_length=20,
        required=False,
        pattern=r'^[a-zA-Z]{1}[a-z-A-Z ,.\'-]{2,19}$',
        pattern_description='Only alphabetical characters, ., \' and space are'
            'valid',
        example='John Doe',
        label='Full Name',
    )


class OtherCard(Card):
    __mapper_args__ = {'polymorphic_identity': 'other'}


class MyCard(Card):
    __mapper_args__ = {'polymorphic_identity': 'my'}

