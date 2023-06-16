from decouple import config
from api_github import repos
import time

TOKEN = config('TOKEN', default=None)
IGNORE = config('IGNORE', cast=lambda v: [s.strip() for s in v.split(',')], default=[])

ta = time.time()
ret = repos.porcent_repo(TOKEN)
print(time.time() - ta)

for k, v in ret.items():
    print(f'{k}: {v}%')

print(f"{round(time.time() - ta, 3)}s")
print(time.ctime(), time.time())