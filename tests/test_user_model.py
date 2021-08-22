import unittest
from app.models import Roles,Users,AnonymousUser,Permission


class UserModelTestCase(unittest.TestCase):
    def test_roles_and_permissions(self):
        Roles.insert_roles()
        self.assertFalse(Permission.WRITE_ARTICLES)
    def test_moderator_role(self):
        r=Roles.query.filter_by(name='Moderator').first()
        u=Users(email='mwasheberit@gmail.com',password='cat',role=r)
        self.assertTrue(u.can(Permission.MODERATE_COMMENTS))
        self.assertFalse(u.can(Permission.ADMINISTER))
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
    def test_anonymous_user(self):
        u=AnonymousUser()
        self.assertFalse(u.can(Permission.ADMINISTER))