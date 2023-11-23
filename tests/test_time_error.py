from unittest.mock import Mock
from mocking_bites.time_error import TimeError

'''
Given I have a TimeError object
I can get the difference between the local PC time and the server time
'''
def test_for_difference_between_external_and_local_time():
    requester_mock = Mock(name='requester')
    response_mock = Mock(name='response')
    time_mock = Mock(name='time')

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "abbreviation": "GMT",
        "client_ip": "2a02:c7c:bec2:d300:6d3f:8c42:bf55:adf8",
        "datetime": "2023-11-23T11:12:14.197795+00:00",
        "day_of_week": 4,
        "day_of_year": 327,
        # "dst": false,
        # "dst_from": null,
        "dst_offset": 0,
        # "dst_until": null,
        "raw_offset": 0,
        "timezone": "Europe/London",
        "unixtime": 1234567890,
        "utc_datetime": "2023-11-23T11:12:14.197795+00:00",
        "utc_offset": "+00:00",
        "week_number": 47
    }
    time_mock.time.return_value = 1234567890.5


    time_error = TimeError(requester_mock, time_mock)
    result = time_error.error()
    assert result == -0.5
