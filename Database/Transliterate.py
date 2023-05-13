import json

# Opening JSON file
f = open('TRANSCRIPT.json', 'r', encoding='utf-8')

data = json.load(f)
print(data)


def TranscriptPhoenician():
    return None

def PhoenicianTranscript():
    return None





# Closing file
f.close()