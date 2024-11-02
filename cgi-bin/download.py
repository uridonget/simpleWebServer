#!/usr/bin/env python3

import os
import cgi
import cgitb

# Enable debugging
cgitb.enable()

# Path to the download folder
DOWNLOAD_FOLDER = './resource/database'

# Generate the HTML response
def generate_html(files):
    html = '''Status: 200 OK\r
Content-Type: text/html\r\n\r

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>파일 다운로드</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        a {
            text-decoration: none;
            color: #007BFF;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>파일 다운로드</h1>
    <table>
        <thead>
            <tr>
                <th>파일 이름</th>
                <th>다운로드 링크</th>
            </tr>
        </thead>
        <tbody>'''
    
    for filename in files:
        html += f'''
            <tr>
                <td>{filename}</td>
                <td><a href="/upload/{filename}" download>다운로드</a></td>
            </tr>'''

    html += '''
        </tbody>
    </table>
</body>
</html>'''

    return html

# Get the list of files in the download folder
try:
    files = [f for f in os.listdir(DOWNLOAD_FOLDER) if os.path.isfile(os.path.join(DOWNLOAD_FOLDER, f))]
except Exception as e:
    files = []

# Generate and print the HTML response
print(generate_html(files))