import csv
from pathlib import Path

p = Path(r'C:\git\loe-posit\data\output-plan-b-readable.csv')

with p.open('r', encoding='utf-8', newline='') as f:
    rows = list(csv.DictReader(f))

if not rows:
    raise SystemExit('CSV is empty')

remove = {'depth_cm', 'inventory_number', 'catalog_number', 'exhibited_at', 'notes', 'creator_qid', 'object_type_qid', 'materials_qids'}
keep = [c for c in rows[0].keys() if c not in remove]

with p.open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keep)
    writer.writeheader()
    for row in rows:
        writer.writerow({k: row.get(k, '') for k in keep})

print('Columns kept:', keep)
print('Row count:', len(rows))
