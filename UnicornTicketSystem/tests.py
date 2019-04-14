from django.test import TestCase
# from models import item

class TestDjango(TestCase):

    def test_is_this_thing_on(self):
        self.assertEqual(1,1)

# class TestItemModel(TestCase):
#     def test_done_defaults_to_false(self):
#         item = Item(name="Create a test")
