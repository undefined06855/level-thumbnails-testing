import os
import json
import time

f_arr = os.listdir("./thumbs")
content = []
for file in f_arr:
  file_s = str(file)
  file_s2 = file_s.strip(".png")
  content.append(file_s2)
json_dict = {"lastUpdated": int(time.time()), "level_ids": content}
print(json.dumps(json_dict,indent=4))
