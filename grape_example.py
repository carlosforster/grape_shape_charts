from grape import grape
from random import choice
import pandas as pd
import webbrowser
import tempfile
import os

df = pd.DataFrame()
numbers="one two three four five six seven eight nine ten".split()
for i in range(10):
    df[numbers[i]] = [choice([0]*i+[1]*(9-i)) for m in range(20)]

print(df)

svg = grape(df, [["one", "two", "three", "four"],["five","six","seven"],
  ["eight", "nine"],["ten"]])

def display_html(html_content):
    # Create a temporary file with the .html suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        temp_file.write(html_content.encode('utf-8'))
        temp_file_path = temp_file.name

    # Open the temporary file in the default web browser
    webbrowser.open(f'file://{os.path.realpath(temp_file_path)}')

html_string = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sample HTML</title>
</head>
<body>
<style>
  svg {{background: aliceblue;}}
</style>
    <h1>GrapeShape charts</h1>
{svg}
</body>
</html>
"""

display_html(html_string)
