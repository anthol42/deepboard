
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace(
    "./assets/",
    "https://raw.githubusercontent.com/anthol42/deepboard/main/assets/"
)
with open("README_pypi.md", "w", encoding="utf-8") as f:
    f.write(content)
