import json

nb = json.load(open('solution.ipynb', encoding='utf-8'))
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code':
        continue
    outputs = c.get('outputs', [])
    if not outputs:
        continue
    ec = c.get('execution_count', '?')
    print(f"\n{'='*60}")
    print(f"CELL {ec} (index {i})")
    print(f"{'='*60}")
    for o in outputs:
        if o.get('output_type') == 'stream':
            text = o.get('text', [])
            if isinstance(text, list):
                print(''.join(text), end='')
            else:
                print(text, end='')
        elif o.get('output_type') == 'execute_result':
            data = o.get('data', {})
            if 'text/plain' in data:
                tp = data['text/plain']
                if isinstance(tp, list):
                    print(''.join(tp), end='')
                else:
                    print(tp, end='')
        elif o.get('output_type') == 'error':
            print(f"ERROR: {o.get('ename','')}: {o.get('evalue','')}")
