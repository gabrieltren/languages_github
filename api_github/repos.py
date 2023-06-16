from .api_consume import api_github_get
from decouple import config

IGNORE = config('IGNORE', cast=lambda v: [s.strip() for s in v.split(',')], default=[])


def repos_user(token):
    url = 'https://api.github.com/user/repos'
    params = {'affiliation': 'owner','page':1, 'per_page':100}
    headers = {'Authorization': f'token {token}'}
    repos_return = []
    while True:
        api_get = api_github_get(url,params, headers)
        if api_get.status_code != 200 or not api_get.json():
            break
        repos_return += api_get.json()
        params['page'] +=1
    return repos_return


def languages(token, url):
    headers = {'Authorization': f'token {token}'}
    api_get = api_github_get(url, headers=headers)
    if api_get.status_code != 200:
        return {}
    return api_get.json()
    
    
def repositories_languages(token):
    repositories = repos_user(token)
    totalizers = {'total': 0}
    for repos in repositories:
        lg = languages(token, repos['languages_url'])
        if len(lg.keys()) > 0:
            for k, v in lg.items():
                if k not in IGNORE:
                    # print(k, v)
                    totalizers['total'] +=int(v)
                    totalizers[k] = totalizers[k] + v if totalizers.get(k, None) else v

    return totalizers

def porcent_repo(token):
    totalizers = repositories_languages(token)
    total = totalizers.pop('total')
    total_json = {}
    if len(totalizers.keys())> 0:
        for k, v in totalizers.items():
            total_json[k] = round((v/total)*100, 2)
            
    return total_json