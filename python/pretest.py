with open('sub', 'r') as f:
    lines = f.readlines()

selected_lines = [line for line in lines if line.startswith(('vmess://', 'ss://', 'ssr://', 'trojan://'))]

with open('python/pretest', 'w') as f:
    f.writelines(selected_lines)
