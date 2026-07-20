import os
import re

base_dir = r"c:\Users\y_tar\Desktop\yahya web site"
old_url = "https://yourdomain.com"
new_url = "https://yahyafarag.github.io/yahya-web-site"

def replace_in_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if old_url in content:
                    content = content.replace(old_url, new_url)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {filepath}")

replace_in_files(base_dir)
print("Finished updating URLs in HTML files.")
