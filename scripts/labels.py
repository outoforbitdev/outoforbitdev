import subprocess
from repos import populate_repos

def main():
    repos = populate_repos()
    for r in repos:
        cmd_str = "npx github-label-sync -l labels.json outoforbitdev/" + r["name"]
        cmd_list = cmd_str.split(" ")
        print(cmd_list)
        subprocess.run(cmd_list)

if __name__ == "__main__":
    main()