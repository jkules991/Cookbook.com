from flask_testing import TestCase
from application import app, db
from application.models import Recipes, Instructions
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        # Create table schema
        db.create_all()

        # Create tests
        test_recipe = Recipes(r_name="Fajitas2", ingredients="Salt and pepah",
                            prep_t =2, cook_t=2
                            )
        test_instructions= Instructions(portions=1, prep_method="Buy the Fajitas",
                                        cook_method="eat the fajitas", recipe_id=1
                                         )

        # save sample data to database
        db.session.add(test_recipe)
        db.session.add(test_instructions)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

# Testing webpage GET responses
class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home_page'))
        self.assertEqual(response.status_code, 200)

class TestCreate(TestBase):
    def test_create_get(self):
        response = self.client.get(url_for('create_page'))
        self.assertEqual(response.status_code, 200)

class TestCreate2(TestBase):
    def test_create2_get(self):
        response = self.client.get(url_for('create_page2'))
        self.assertEqual(response.status_code, 200)

class TestSearch(TestBase):
    def test_search_get(self):
        response = self.client.get(url_for('search_page'))
        self.assertEqual(response.status_code, 200)

class TestRName(TestBase):
    def test_r_name_get(self):
        response = self.client.get(url_for('result_name'))
        self.assertEqual(response.status_code, 200)

class TestRPrep(TestBase):
    def test_r_prep_get(self):
        response = self.client.get(url_for('result_prep'))
        self.assertEqual(response.status_code, 200)

class TestRCook(TestBase):
    def test_r_cook_get(self):
        response = self.client.get(url_for('result_cook'))
        self.assertEqual(response.status_code, 200)

class TestRPortions(TestBase):
    def test_r_portions_get(self):
        response = self.client.get(url_for('result_portions'))
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_delete_get(self):
        response = self.client.get(url_for('delete_page', num=1))
        self.assertEqual(response.status_code, 200)

class TestEdit(TestBase):
    def test_edit_get(self):
        response = self.client.get(url_for('edit_page', num= 1))
        self.assertEqual(response.status_code, 200)


#testing add functionality

class TestAddR(TestBase):
    def test_add_rec(self):
        response = self.client.post(
            url_for('create_page'),
            data = dict(r_name="test1",
            ingredients="testing",
            prep_t=2,
            cook_t=1),
            follow_redirects=True
        )
        self.assertIn(b'Create',response.data)

class TestAddIns(TestBase):
    def test_add_ins(self):
        response = self.client.post(
            url_for('create_page2'),
            data = dict(portions=1,
            prep_method="testing1",
            cook_method="testing2"),
            follow_redirects=True
        )
        self.assertIn(b'Create2',response.data)