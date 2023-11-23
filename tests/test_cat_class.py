from mocking_bites.cat_class import CatFacts
from unittest.mock import Mock

def test_get_cat_fact():
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "fact": "Cats respond better to women than to men, probably due to the fact that women's voices have a higher pitch.",
        "length": 107
    }

    cat_facts = CatFacts(requester_mock)
    result = cat_facts.provide()
    assert result == "Cat fact: Cats respond better to women than to men, probably due to the fact that women's voices have a higher pitch."