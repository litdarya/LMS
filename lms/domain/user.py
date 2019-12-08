import lms.infra.db.postgres_executor as pe

class Student:
    def __init__(self, *, user_id):
        self.user_id = user_id

    def get_info(
            self,
            *,
            params=('name', 'email', 'telephone', 'city', 'info', 'vk_link', )
    ):
        pass

    def ge
