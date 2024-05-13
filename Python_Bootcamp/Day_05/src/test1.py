import requests


def test() -> None:
    response: requests.Response = requests.get(
        "http://localhost:8888/?species=Time%20Lord"
    )
    print("TEST #1")
    print("Link: http://localhost:8888/?species=Time%20Lord")
    print("HTTP Header: ")
    print(response.headers)
    print(f"Content: {response.content.decode()}")
    print()
    assert response.content == b'{"credentials": "Rassilon"}'

    response = requests.get("http://localhost:8888/?species=Cyberman")
    print("TEST #2")
    print("Link: http://localhost:8888/?species=Cyberman")
    print("HTTP Header: ")
    print(response.headers)
    print(f"Content: {response.content.decode()}")
    print()
    assert response.content == b'{"credentials": "John Lumic"}'

    response = requests.get("http://localhost:8888/?species=Judoon")
    print("TEST #3")
    print("Link: http://localhost:8888/?species=Judoon")
    print("HTTP Header: ")
    print(response.headers)
    print(f"Status code: {response.status_code}")
    print(f"Content: {response.content.decode()}")
    print()
    assert response.status_code == 200
    assert (
        response.content
        == b'{"credentials": "Shadow Proclamation Convention 15 Enforcer"}'
    )

    response = requests.get("http://localhost:8888/?species=Ood")
    print("TEST #4")
    print("Link: http://localhost:8888/?species=Ood")
    print("HTTP Header: ")
    print(response.headers)
    print(f"Status code: {response.status_code}")
    print(f"Content: {response.content.decode()}")
    print()
    assert response.status_code == 200
    assert response.content == b'{"credentials": "Klineman Halpen"}'

    response = requests.get("http://localhost:8888/?species=Slitheen")
    print("TEST #5")
    print("Link: http://localhost:8888/?species=Slitheen")
    print("HTTP Header: ")
    print(response.headers)
    print(f"Status code: {response.status_code}")
    print(f"Content: {response.content.decode()}")
    print()
    assert response.status_code == 200
    assert response.content == b'{"credentials": "Coca-Cola salesman"}'

    response = requests.get("http://localhost:8888/")
    print("TEST #6")
    print("Link: http://localhost:8888/")
    print("HTTP Header: ")
    print(response.headers)
    print(f"Status code: {response.status_code}")
    print(f"Content: {response.content.decode()}")
    print()
    assert response.status_code == 404
    assert response.content == b'{"credentials": "Unknown"}'

    response = requests.get("http://localhost:8888/?spec=Lol")
    print("TEST #7")
    print("Link: http://localhost:8888/?spec=SAAABAKA")
    print("HTTP Header: ")
    print(response.headers)
    print(f"Status code: {response.status_code}")
    print(f"Content: {response.content.decode()}")
    print()
    assert response.status_code == 404
    assert response.content == b'{"credentials": "Unknown"}'

    print("Tests passed!")


if __name__ == "__main__":
    test()
