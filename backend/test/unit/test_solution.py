import pytest

import unittest.mock as mock

from src.controllers.recipecontroller import RecipeController
from src.static.diets import from_string

# add your test case implementation here
# @pytest.mark.unit
# def test():
#     pass

@pytest.mark.unit
def test_get_recipe_available_optimal_normal():
    """ Assert that get_recipe returns the optimal normal recipe. """
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d1"
            },
            "name": "Vinager",
            "quantity": 210.0,
            "unit": "milliliter"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d2"
            },
            "name": "Yeast",
            "quantity": 3.0,
            "unit": "block"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d3"
            },
            "name": "Baking Powder",
            "quantity": 3.0,
            "unit": "pack"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d4"
            },
            "name": "Sugar",
            "quantity": 300.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d5"
            },
            "name": "Flour",
            "quantity": 450.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d6"
            },
            "name": "Salt",
            "quantity": 275.0,
            "unit": "gram"
        }
    ]

    sut = RecipeController(mocked_dao)
    
    result = sut.get_recipe(diet=from_string(""), take_best=True)

    # print(result)

    assert result == "Pancakes"

@pytest.mark.unit
def test_get_recipe_available_optimal_vegetarian():
    """ Assert that get_recipe returns the optimal vegetarian recipe. """
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d1"
            },
            "name": "Vinager",
            "quantity": 210.0,
            "unit": "milliliter"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d2"
            },
            "name": "Yeast",
            "quantity": 3.0,
            "unit": "block"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d3"
            },
            "name": "Baking Powder",
            "quantity": 3.0,
            "unit": "pack"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d4"
            },
            "name": "Sugar",
            "quantity": 300.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d5"
            },
            "name": "Flour",
            "quantity": 450.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d6"
            },
            "name": "Salt",
            "quantity": 275.0,
            "unit": "gram"
        }
    ]

    sut = RecipeController(mocked_dao)
    
    result = sut.get_recipe(diet=from_string("vegetarian"), take_best=True)

    # print(result)

    assert result == "Pancakes"

@pytest.mark.unit
def test_get_recipe_available_random_vegetarian():
    """ Assert that get_recipe returns a random vegetarian recipe. """
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d1"
            },
            "name": "Vinager",
            "quantity": 210.0,
            "unit": "milliliter"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d2"
            },
            "name": "Yeast",
            "quantity": 3.0,
            "unit": "block"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d3"
            },
            "name": "Baking Powder",
            "quantity": 3.0,
            "unit": "pack"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d4"
            },
            "name": "Sugar",
            "quantity": 300.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d5"
            },
            "name": "Flour",
            "quantity": 450.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d6"
            },
            "name": "Salt",
            "quantity": 275.0,
            "unit": "gram"
        }
    ]

    sut = RecipeController(mocked_dao)
    
    result = sut.get_recipe(diet=from_string("vegetarian"), take_best=False)

    # print(result)

    assert result == "Pancakes"

@pytest.mark.unit
def test_get_recipe_available_random_vegan():
    """ Assert that get_recipe returns a random vegan recipe. """
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d1"
            },
            "name": "Vinager",
            "quantity": 210.0,
            "unit": "milliliter"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d2"
            },
            "name": "Yeast",
            "quantity": 3.0,
            "unit": "block"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d3"
            },
            "name": "Baking Powder",
            "quantity": 3.0,
            "unit": "pack"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d4"
            },
            "name": "Sugar",
            "quantity": 300.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d5"
            },
            "name": "Flour",
            "quantity": 600.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d6"
            },
            "name": "Salt",
            "quantity": 275.0,
            "unit": "gram"
        },
        {
            "_id": {
                "$oid": "6649f1f0077613df3ef4f7d7"
            },
            "name": "Walnuts",
            "quantity": 30.0,
            "unit": "gram"
        }
    ]

    sut = RecipeController(mocked_dao)
    
    result = sut.get_recipe(diet=from_string("vegan"), take_best=False)

    # print(result)

    assert result == "Whole Grain Bread"

@pytest.mark.unit
def test_get_recipe_unavailable():
    """ Assert that get_recipe returns None when no recipe available. """
    mocked_dao = mock.MagicMock()
    mocked_dao.find.return_value = [
        
    ]

    sut = RecipeController(mocked_dao)
    
    result = sut.get_recipe(diet=from_string("normal"), take_best=True)

    # print(result)

    assert result == None