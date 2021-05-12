import json, requests

# 【重要】大佬Github的ID
user = 'WangRongsheng'

repo_list = []
page_id = 1
while True:
    url = 'https://api.github.com/users/{}/repos?page={}'.format(user, page_id)
    print(url)
    r = requests.get(url)
    repo_array = json.loads(r.content.decode('utf-8'))
    if len(repo_array) == 0:
        break
    for repo in repo_array:
        if not repo['fork']:
            repo_list.append([repo['name'], repo['stargazers_count'], repo['forks_count']])
    page_id += 1

# 排序
repo_list = sorted(repo_list, key=lambda x: x[1], reverse=True)

print('=' * 55)
print('\n'.join(['{: <40}★{: <10}\tfork {} '.format(*repo) for repo in repo_list]))
print('=' * 55)
print('{: <40}★{: <10}\tfork {} '.format('total', sum([i[1] for i in repo_list]), sum([i[2] for i in repo_list])))
