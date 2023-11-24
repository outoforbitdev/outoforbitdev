from repos import write_repo_header, write_repo_line, top_repos

def generate_readme():
    repos = top_repos()
    readme = open(r"../README.md", "w")
    readme.write("### Hi there 👋\n\n")
    readme.write("## [Roadmap](ROADMAP.md)\n\n")
    readme.write("## Top Repositories\n\n")
    write_repo_header(readme)
    for r in repos:
        write_repo_line(r, readme)
    readme.write("\n\n### [Full Repository Guide](./REPOSITORIES.md)")
    readme.close()

if __name__ == "__main__":
    generate_readme()