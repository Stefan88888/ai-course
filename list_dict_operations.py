tools = ["python", "Git"]
tools.append("Docker")      #add Docker
tools.append("SQL")         #add SQL
tools.remove("Git")         #Remove Git from list
print(len(tools))           #count how mny names hve in list
print("python" in tools)

project = {"name": "AI course", "progress": 6}

project["status"] = "in progress"           #add new key
project["progress"] = 7                     #change "progress": 6

print(project)

#key ={
#    "status": "in progress"
#}
#project[]