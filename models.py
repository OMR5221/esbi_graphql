# Define the models from our db tables:
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

# Local file imports:
from database import Base, engine


class PlantModel(Base):
    __tablename__ = 'es_plant_dim'
    __table_args__ = {'extend_existing': True}

    plantId = Column('plant_id', Integer, primary_key=True)
    Tags = relationship("TagsModel")


class TagsModel(Base):
    __tablename__ = 'es_tags_dim'
    __table_args__ = {'extend_existing': True}

    tagId = Column('tag_id', Integer, primary_key=True)
    plantId = Column('plant_id', Integer, ForeignKey("es_plant_dim.plant_id"))


Base.prepare(engine)
