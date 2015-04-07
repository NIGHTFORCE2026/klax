# DEFINE UNIT TESTS
import unittest
from flask import current_app
from app import create_app, db

class BasicTestCase(unittest.TestCase):
    # setUp, tearDown run before each test
    def setUp(self):
        """ create an app for testing and activate its current_app context """
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """ remove current_app context and database """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    # test_ executed as tests
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])


    
