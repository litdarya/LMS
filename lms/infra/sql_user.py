from lms.domain.user import User

class SqlUser(User):

    def __init__(self, *, user_id):
        super().__init__(user_id=user_id)


    def __
