"""Test file for project."""

import flask
import sample.app
import sample.resource


def test_flask_app_is_returned_from_main():
    shaayan = sample.resource.Person(name="Shaayan", year=1988)
    app = sample.app.main(shaayan)

    assert isinstance(app, flask.Flask)


def test_that_age_of_person_method_is_run(mocker):
	mock = mocker.Mock()
	mock.age_of_person.return_value = 33
	mock.name = "Subhayan"
	expected_ouput = {
		"name":"Subhayan",
		"age": 33
	}
	app = sample.app.main(mock)
	assert isinstance(app, flask.Flask)

	app.config['TESTING'] = True

	with app.test_client() as client:
		response = client.get('/sample')

	assert response.status_code == 200
	assert response.json == expected_ouput
	mock.age_of_person.assert_called()
