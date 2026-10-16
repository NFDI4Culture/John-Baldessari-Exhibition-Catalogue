import csv
from pathlib import Path

src = Path(r'C:\git\loe-posit\data\output-plan-b-readable.csv')

with src.open('r', encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))

for row in rows:
    title = row.get('title', '')
    if title is None:
        row['title'] = ''
        continue
    title = title.strip()
    if not title:
        row['title'] = ''
        continue
    words = []
    for token in title.split():
        token = token.strip()
        if not token:
            continue
        if token.isupper() and len(token) > 1:
            words.append(token.title())
        else:
            words.append(token[:1].upper() + token[1:].lower())
    row['title'] = ' '.join(words)

with src.open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f'Normalised {len(rows)} titles in {src}')
