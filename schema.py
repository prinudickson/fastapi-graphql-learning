from graphene import ObjectType, String, Schema

class Query(ObjectType):
    #This defines a Field `hello` in our schema with a single arguement `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()
    # our Resolver method takes the GraphQL context (root, info) as well as
    # Arguement (name) for the field and returns data for the query response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return f'See ya!'

schema = Schema(query=Query)

#Testing

# # we can query for our field (with the default argument)
# query_string = '{ goodbye }'
# result = schema.execute(query_string)
# print(result.data['goodbye'])
# print(result.data)
# # "Hello stranger!"

# # or passing the argument in the query
# query_with_argument = '{ hello(name: "GraphQL") }'
# result = schema.execute(query_with_argument)
# print(result.data['hello'])
# print(result.data)
# # "Hello GraphQL!"