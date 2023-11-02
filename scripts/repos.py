def generate_readme():
    repos = populate_repos()
    readme = open(r"../REPOSITORIES.md", "w")
    readme.write("# Repository Guide\n")
    write_repo_header(readme)
    for r in repos:
        write_repo_line(r, readme)
    readme.close()

def populate_repos():
    return [
        { "name": "action-semantic-release", "type": "Action", "dependabot": ":white_check_mark:" },
        { "name": "action-docker-publish", "type": "Action", "dependabot": ":white_check_mark:" },
        { "name": "action-npm-publish", "type": "Action", "dependabot": ":x:" },
        { "name": "action-docker-test", "type": "Action", "dependabot": ":white_check_mark:" },
        { "name": "docker-node", "type": "Docker", "dependabot": ":white_check_mark:" },
        { "name": "docker-dotnet-aspnet", "type": "Docker", "dependabot": ":x:" },
        { "name": "docker-dotnet-reactapp", "type": "Docker", "dependabot": ":x:" },
        { "name": "docker-dotnet-sdk", "type": "Docker", "dependabot": ":x:" },
        { "name": "canary-dotnet-reactapp", "type": "Canary", "dependabot": ":white_check_mark:" },
        { "name": "oodts", "type": "Library", "dependabot": ":x:" },
        { "name": "oodreactts", "type": "Library", "dependabot": ":x:" },
        { "name": "oodgraphics", "type": "Library", "dependabot": ":x:" },
        { "name": "oodreacttemplate", "type": "Template", "dependabot": ":x:" }
    ]

def write_repo_header(readme):
    header    = "| Type | Repository | Dependabot | Version | Scorecard | Pipelines | Issues |\n"
    separator = "|------|------------|------------|---------|-----------|-----------|--------|\n"
    readme.write(header)
    readme.write(separator)

def write_repo_line(repo, readme):
    line = "| " + repo["type"] \
    + " | [" + repo["name"] + "](https://github.com/outoforbitdev/" + repo["name"] \
    + ") | " + repo["dependabot"] + " " \
    + version(repo) \
    + scorecard(repo) \
    + pipelines(repo) \
    + issues(repo) \
    + "\n"
    readme.write(line)

def version(repo):
    return "| <a href='https://github.com/outoforbitdev/" + repo["name"] + "/releases/latest'><img alt='Latest release' src='https://img.shields.io/github/v/release/outoforbitdev/" + repo["name"] + "?logo=github&label=%20'></a> " \

def scorecard(repo):
    return "| <a href='https://securityscorecards.dev/viewer/?uri=github.com/outoforbitdev/" + repo["name"] + "'><img alt='OpenSSF Scorecard' src='https://api.securityscorecards.dev/projects/github.com/outoforbitdev/" + repo["name"] + "/badge'></a> " \

def pipelines(repo):
    return "| <a href='https://github.com/outoforbitdev/" + repo["name"] + "/actions/workflows/test.yml'><img alt='Test states' src='https://img.shields.io/github/actions/workflow/status/outoforbitdev/" + repo["name"] + "/test.yml?label=Test'></a>" \
    + "<br><a href='https://github.com/outoforbitdev/" + repo["name"] + "/actions/workflows/release.yml'><img alt='Release states' src='https://img.shields.io/github/actions/workflow/status/outoforbitdev/" + repo["name"] + "/release.yml?label=Release'></a>"

def issues(repo):
    return "| <a href='https://github.com/outoforbitdev/" + repo["name"] + "/issues'><img alt='Open issues' src='https://img.shields.io/github/issues/outoforbitdev/" + repo["name"] + "?logo=github&label=Issues'></a> " \
    + "<br><a href='https://github.com/outoforbitdev/" + repo["name"] + "/pulls'><img alt='Open PRs' src='https://img.shields.io/github/issues-pr/outoforbitdev/" + repo["name"] + "?logo=github&label=PRs'></a> |"

if __name__ == "__main__":
    generate_readme()
