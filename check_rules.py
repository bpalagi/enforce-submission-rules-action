import sys
from github import Github

github = Github(sys.argv[1])
repo = github.get_repo('KTH/devops-course', lazy=False)

pr = repo.get_pull(1650)

commits = pr.get_commits()

num_students = 0

readme = repo.get_contents('README.md').decoded_content

print(readme)

# for commit in commits:
#     files = commit.files
#     for file in files:
#         filename = file.filename
#         contents = repo.get_contents(filename, ref=commit.sha).decoded_content

            