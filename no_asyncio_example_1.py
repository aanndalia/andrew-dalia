import requests
import time


def fetch_data(url):
    response = requests.get(url)
    return response.text


def main():
    start = time.time()
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]
    results = []
    for url in urls:
        data = fetch_data(url)
        results.append(data)
        print(f"Data from {url}: {data[:50]}...")

    print(f'time: {time.time() - start} secs')

    return results


if __name__ == "__main__":
    main()
