# Create classes used by GraphQL to map our DB Models
# GraphQL: is a single endpoint for front end developers to reference
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import *


# Import Plant Model and make usable by Graphene:
class Plant(SQLAlchemyObjectType):

    class Meta:
        model = PlantModel
        # Node establishes a global id reference for any instances of the Model Type:
        interfaces = (graphene.relay.Node, )


# Import Tags Model and make usable by Graphene:
class Tags(SQLAlchemyObjectType):

    class Meta:
        model = TagsModel
        # Node establishes a global id reference for any instances of the Model Type:
        interfaces = (graphene.relay.Node, )


# Entrypoint for READ-ONLY access for models:
class Query(graphene.ObjectType):

    node = graphene.relay.Node.Field()

    all_plants = SQLAlchemyConnectionField(Plant)
    all_tags = SQLAlchemyConnectionField(Tags)

    # We define the Plant as the Viewer of the corresponding data:
    plant = graphene.Field(Plant, plantId=graphene.Int())

    # Must tie Viewers besides node to a resolve function:
    def resolve_plant(self, info, plantId):
        query = Plant.get_query(info)
        return query.filter(PlantModel.plantId == plantId).first()


schema = graphene.Schema(query=Query, types=[Plant])

# Example Query to get plant info:
'''
query{
    plant(plant_id:1227) {
        plant_code
        plant_name
        plant_capacity
    }
}
'''

# Example Query to get first 10 Tags associated to a Plant:
# edge: returns an array of nodes that can be referenced in a client app like
## res.data.plant.Tags.edges.map(a => <Text>{a.node.text}</Text>)
'''
query{
    plant(plant_id:1227){
        plant_code
        plant_name
        Tags(first:10){
            edges{
                node{
                    tag_name
                    tag_type
                }
            }
        }
    }
}
'''
