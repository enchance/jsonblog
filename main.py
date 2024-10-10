import httpx

API_KEY = ''

def main():
    request = httpx.get('https://jsonplaceholder.typicode.com/users')
    print(request.json())


if __name__ == '__main__':
    main()
