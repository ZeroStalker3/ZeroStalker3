import requests

def fetch_stats():
    stats_url = "https://github-readme-stats.vercel.app/api?username=ZeroStalker3&show_icons=true&theme=radical&layout=compact"
    langs_url = "https://github-readme-stats.vercel.app/api/top-langs/?username=ZeroStalker3&layout=compact&theme=radical"
    return stats_url, langs_url

def update_readme(stats_url, langs_url):
    try:
        with open("README.md", "r", encoding="utf-8") as file:
            readme = file.readlines()
        start = -1
        for i, line in enumerate(readme):
            if "## 📈 **Статистика GitHub**" in line:
                start = i
                break
        if start == -1:
            raise ValueError("Не найдена строка '## 📈 **Статистика GitHub**' в файле README.md.")
        readme[start+2] = f'  <img src="{langs_url}" alt="языки программирования" />\n'
        readme[start+4] = f'  <img src="{stats_url}" alt="статистика" />\n'
        
        with open("README.md", "w", encoding="utf-8") as file:
            file.writelines(readme)
    
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    stats_url, langs_url = fetch_stats()
    update_readme(stats_url, langs_url)
