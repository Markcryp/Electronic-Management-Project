from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from config import Base, Session

class Electronic(Base):
    __tablename__ = 'electronics'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    features = relationship('Feature', back_populates='electronic', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Electronic(name={self.name}, brand={self.brand}, price={self.price})>"

    @classmethod
    def add_electronic(cls, name, brand, price):
        session = Session()
        electronic = cls(name=name, brand=brand, price=price)
        session.add(electronic)
        session.commit()

    @classmethod
    def list_electronics(cls):
        session = Session()
        return session.query(cls).all()

    @classmethod
    def find_by_name(cls, name):
        session = Session()
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def delete_electronic(cls, electronic_id):
        session = Session()
        electronic = session.query(cls).get(electronic_id)
        if electronic:
            session.delete(electronic)
            session.commit()

    @classmethod
    def update_electronic(cls, electronic_id, name, brand, price):
        session = Session()
        electronic = session.query(cls).get(electronic_id)
        if electronic:
            electronic.name = name
            electronic.brand = brand
            electronic.price = price
            session.commit()

class Feature(Base):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    feature_name = Column(String, nullable=False)
    electronic_id = Column(Integer, ForeignKey('electronics.id'))
    electronic = relationship('Electronic', back_populates='features')

    def __repr__(self):
        return f"<Feature(name={self.feature_name})>"

    @classmethod
    def add_feature(cls, electronic_id, feature_name):
        session = Session()
        feature = cls(feature_name=feature_name, electronic_id=electronic_id)
        session.add(feature)
        session.commit()
    
    @classmethod
    def get_features(cls, electronic_id):
        session = Session()
        return session.query(cls).filter_by(electronic_id=electronic_id).all()
