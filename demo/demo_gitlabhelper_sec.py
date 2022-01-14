from astar_devopstool.gitlabhelper import Gitlab
import configparser
from datetime import datetime, timedelta
import time
cp = configparser.ConfigParser()
cp.read('token.conf')

url = cp.get('gitlab', 'url')
token = cp.get('gitlab', 'token')

print(url)
print(token)

gl = Gitlab(url, token)
projects = gl.projects.list(search='QGisPlugins')
branches = ['dev']


start_time = time.time()
s = gl.statistical_submission(start_time=datetime.now() - timedelta(days=30),
                              end_time=datetime.now(),
                              projects=projects,
                              branches=branches
                              )
end_time = time.time()
print(s)

print({k: v['additions'] - v['deletions'] for k, v in s.items()})
print("time left:", end_time - start_time)
