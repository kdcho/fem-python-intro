import requests

def create_query(language, min_stars=50000):
    query = f"stars:>{min_stars} "

    for language in language:
        query += f"language:{language} "

    return query

def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    query = create_query(languages)
    parameters = {"q": query, "sort": sort, "order": order}
    response = requests.get(gh_api_repo_search_url, params=parameters)

    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"Error fetching data from GitHub API: {status_code}")
    else:
        response_json = response.json()["items"]
        return response_json

if __name__ == "__main__":
    languages = ["Python", "Javascript", "Ruby"]
    results = repos_with_most_stars(languages)

    query = create_query(languages)

    for result in results:
        language = result["language"]
        starts = result["stargazers_count"]
        name = result["name"]

        print(f"{name} is written in {language} and has {starts} stars")