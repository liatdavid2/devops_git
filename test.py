from app import app

def testURLHome():
    response = app.test_client().get("/")
    assert response.status_code == 200

def testURLbase():
    response = app.test_client().get("/base")
    assert response.status_code == 200


def testURLbaseHTMLText():
    response = app.test_client().get("/base")
    assert b"Todo list" in response.data
    assert b"delete" in response.data