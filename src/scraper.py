import re
import json

HEADER = "First Name,Last Name,Mobile Phone,E-mail Address,City,Job Title,Department\n"

with open ("../Employees.html", "r") as html:
    htmlStr = html.read()

    match = re.search('var data=(\[\{.*\}\]);', htmlStr)
    if match:
        jsonStr = match.group(1)
        jsonData = json.loads(jsonStr)

        with open ("../Employees.csv", "w") as csv:
            csv.write(HEADER)
            for jsonEmployee in jsonData:
                csv.write("\"" + jsonEmployee["firstName"] + "\",")
                csv.write("\"" + jsonEmployee["lastName"] + "\",")
                csv.write("\"" + jsonEmployee["mobilePhone"] + "\",")
                csv.write("\"" + jsonEmployee["workEmail"] + "\",")
                csv.write("\"" + jsonEmployee["location"] + "\",")
                csv.write("\"" + jsonEmployee["jobTitle"] + "\",")
                csv.write("\"" + jsonEmployee["department"] + "\"\n")
    else:
        raise Exception.new("Couldn't find the employee data in the html file")