import falcon
import jwt
from falcon import Request, Response

from chat.adapters.database import repositories, storage
from chat.application import errors

user_repo = repositories.UserRepo(users=storage.Storage.users)


class AuthComponent:

    def process_resource(self, req: Request, resp: Response, resource, params):
        if req.path == "/api/users/login":
            """
            Not authorized users cat use only login path
            """
        else:
            user_validate_status = False
            auth_type = None
            req_token = None
            auth = req.get_header("Authorization")
            if auth:
                auth_type, req_token = auth.split()
            if auth_type == "Bearer":
                key = storage.Storage.secret_key
                try:
                    payload = jwt.decode(req_token, key, algorithms=["HS256"])
                except jwt.exceptions.InvalidSignatureError:
                    raise errors.AuthError
                user_id = payload.get("id")
                if user_repo.get_by_id(user_id):
                    req.context.update({"user_id": user_id})
                    user_validate_status = True
            if not user_validate_status:
                resp.status = falcon.HTTPBadRequest
                raise errors.AuthError
