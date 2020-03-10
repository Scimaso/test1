import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from basedatos import db_session,User as UserModel
from sqlalchemy import and_

class Usuarios(SQLAlchemyObjectType):
	class Meta:
	    model = UserModel
	    interfaces = (relay.Node, )



class Query(graphene.ObjectType):
	node = relay.Node.Field()
	usuario = SQLAlchemyConnectionField(Usuarios)
	encontrar_usuario = graphene.Field(lambda: Usuarios, username = graphene.String())
	todos_usuarios = SQLAlchemyConnectionField(Usuarios)

    def usuario_encontrados(self, args, context, info):
        query = Usuarios.get_query(context)
        username = args.get('nombre')
        return query.filter(UserModel.username == username).first()
