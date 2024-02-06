import subprocess
from repos import populate_repos

def main():
    repos = populate_repos()
    confirmation = input("Do you want to update labels on all repos? ('y' to confirm): ").lower()
    if confirmation not in ["y", "yes", "yeah", "ye"]:
        return
    token = input("Enter Github access token: ")
    for r in repos:
        cmd_str = "npx github-label-sync -a " + token + " -l labels.json outoforbitdev/" + r["name"]
        cmd_list = cmd_str.split(" ")
        print(cmd_list)
        subprocess.run(cmd_list)

if __name__ == "__main__":
    main()