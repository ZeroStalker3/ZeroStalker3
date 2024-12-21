import requests

def fetch_stats():
    # Fetch the GitHub stats using API
    stats_url = "https://github-readme-stats.vercel.app/api?username=ZeroStalker3&show_icons=true&theme=radical&layout=compact"
    langs_url = "https://github-readme-stats.vercel.app/api/top-langs/?username=ZeroStalker3&layout=compact&theme=radical"
    
    stats = requests.get(stats_url).content.decode()
    langs = requests.get(langs_url).content.decode()
    
    return stats, langs

def update_readme(stats, langs):
    with open("README.md", "r") as file:
        readme = file.readlines()
    
    start = readme.index("## 📈 **Статистика GitHub**\n")
    end = start + 5  # Assuming 5 lines of stats
    
    readme[start+2] = f'<img src="{langs}" alt="языки программирования" />\n'
    readme[start+4] = f'<img src="{stats}" alt="статистика" />\n'
    
    with open("README.md", "w") as file:
        file.writelines(readme)

if __name__ == "__main__":
    stats, langs = fetch_stats()
    update_readme(stats, langs)
