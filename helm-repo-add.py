# Until they fix https://github.com/helm/helm/issues/8036 by releasing HelmV4
# This stupid wrapper script can add the non private repos as part of a GitHubAction workflow
import yaml
import subprocess
import sys
print("Parsing and loading public repos from Chart.lock")
with open("Chart.yaml", "r") as chart_yaml_file:
    chart_yaml = yaml.load(chart_yaml_file, Loader=yaml.SafeLoader)['dependencies']

with open("Chart.lock", "r") as lock:
    chart_lock = yaml.load(lock, Loader=yaml.SafeLoader)['dependencies']
    for lock in chart_lock:
        if 'helm-private' in lock['repository']:
            continue
        for chart in chart_yaml:
            if chart['name'] != lock['name']:
                continue
            if "@" in chart['repository']:
                repo_name = chart['repository'][1:]
            else:
                repo_name = chart['name']
            add = subprocess.Popen(['helm', 'repo', 'add',
                                    repo_name, lock['repository']],
                                   universal_newlines=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout, stderr = add.communicate()
            exit = add.returncode
            if exit:
                print("Coulnd't add add repo:")
                print(stderr)
                sys.exit(exit)
            print(stdout)
