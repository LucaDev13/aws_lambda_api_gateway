import json
from service import app
from tests.conftest import apigw_event, apigw_event_POST_request


def test_magnum_lambda_handler_with_get_request(apigw_event, mocker):
    ret = app.handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert data["aws_service"] == "Lambda"
    assert data["lambda_handler"] == "Mangum"
    assert data["aws_service"] == "Lambda"
    assert isinstance(data, dict)


def test_magnum_lambda_handler_with_post_request(apigw_event_POST_request, mocker):
    ret = app.handler(apigw_event_POST_request, "")
    data = json.loads(ret["body"])
    assert ret["statusCode"] == 200
    assert data['service_name'] == 'API'
    assert data['price'] == 30
    assert data['offer'] is True
