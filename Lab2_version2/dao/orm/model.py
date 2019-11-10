from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, UniqueConstraint, Boolean
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class ormTest(Base):
    __tablename__ = 'orm_test'

    test_id = Column(Integer, primary_key=True, autoincrement=True)
    test_name = Column(String(63), nullable=False)
    test_variant = Column(Integer, nullable=False)

    orm_questions = relationship('ormQuestion', cascade="all,delete")

    __table_args__ = (
        UniqueConstraint('test_name', 'test_variant'),
    )

    def __init__(self, test_name, test_variant, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_name = test_name
        self.test_variant = test_variant


class ormQuestion(Base):
    __tablename__ = 'orm_question'
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    question_text = Column(String(511), nullable=False)
    test_id = Column(Integer, ForeignKey('orm_test.test_id'))

    question_variants = relationship('ormQuestionVariant', cascade="all,delete")


class ormQuestionVariant(Base):
    __tablename__ = 'orm_question_variant'

    answer_variant_id = Column(Integer, primary_key=True, autoincrement=True)
    answer_variant_text = Column(String(511), nullable=False)
    answer_check = Column(Boolean, default=False, nullable=False)
    question_id = Column(Integer, ForeignKey('orm_question.question_id', ondelete='CASCADE'))


