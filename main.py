import httpx, os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('API_KEY')


def main():
    request = httpx.get('https://jsonplaceholder.typicode.com/users')
    print(request.json())
    print(API_KEY)


if __name__ == '__main__':
    main()
