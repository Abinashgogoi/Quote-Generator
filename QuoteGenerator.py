import requests

def fetch_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        quote = response.json()
        content = quote["content"]
        author = quote["author"]
        return f'"{content}" - {author}'
    else:
        return "Failed to fetch a quote"

if __name__ == "__main__":
    print(fetch_random_quote())