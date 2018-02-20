import myapp.gen_py.users_types_pb2 as users_messages
import myapp.gen_py.users_types_pb2 as users_messages
import myapp.gen_py.users_pb2_grpc as user_service


class UserService(user_service.UsersServicer):

    def CreateUser(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        user = users_messages.User(username=request.username, user_id=1)
        return users_messages.CreateUserResult(user=user)

    def GetUsers(self, request, context):
        for user in request.user:
            user = users_messages.User(
                username=user.username, user_id=user.user_id
            )
            yield users_messages.GetUsersResult(user=user)
