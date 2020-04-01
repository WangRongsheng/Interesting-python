import json

with open("未命名.ipynb",encoding="utf-8") as fp:
    content = json.load(fp)

with open("demo.py","w",encoding="utf-8") as fp:
    for item in content["cells"]:
        fp.writelines([i.rstrip()+"\n" for i in item["source"]])
