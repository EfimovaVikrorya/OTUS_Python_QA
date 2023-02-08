import pytest
import requests


@pytest.mark.regression
@pytest.mark.parametrize('user_id,id,title,body', [
    (1, 1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
     'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto')
])
def test_comments(user_id, id, title, body):
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    assert r.status_code == 200
    row = r.json()
    assert row['userId'] == user_id
    assert row['id'] == id
    assert row['title'] == title
    assert row['body'] == body


@pytest.mark.regression
@pytest.mark.parametrize('id,name,email,body', [
    (5, 'vero eaque aliquid doloribus et culpa',
     'Hayden@althea.biz',
     'harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et')
])
def test_comments_post_id(id, name, email, body):
    r = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
    assert r.status_code == 200
    for row in r.json():
        if row['id'] == id:
            assert row['name'] == name
            assert row['email'] == email
            assert row['body'] == body


@pytest.mark.regression
def test_user():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    assert r.status_code == 200
    for row in r.json():
        if row['id'] == 1:
            assert row['name'] == "Leanne Graham"
            assert row['username'] == "Bret"
            assert row['phone'] == "1-770-736-8031 x56442"


@pytest.mark.regression
def test_comments_json():
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    assert r.status_code == 200
    for row in r.json():
        assert 'postId' in row
        assert 'id' in row
        assert 'name' in row
        assert 'email' in row
        assert 'body' in row


@pytest.mark.regression
def test_post_1_comments():
    r = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
    assert r.status_code == 200
    for row in r.json():
        assert 'postId' in row
        assert 'id' in row
        assert 'name' in row
        assert 'email' in row
        assert 'body' in row
