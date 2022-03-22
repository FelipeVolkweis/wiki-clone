import re

content = "# CSS and java\r\n\nCSS is a language that can be used to add style to an [HTML](/wiki/HTML) page."
header = re.search("^# .*", content)
result = header.group()[:-1][2:]
print(result)