for line in open('Bot_run.bat', 'r'):
    if 'OWM_TOKEN' in line:
        OWM_TOKEN = line.split('=')[-1].strip()
    if 'API_TOKEN' in line:
        API_TOKEN = line.split('=')[-1].strip()
        break
