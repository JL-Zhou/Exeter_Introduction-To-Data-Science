#8.	Using the data structure below update the grades to be the sum of the marks and the classification
#should be according to Exeter's rules: 70+ Distinction, 60-69 Merit, 50-59 Pass, 40-49 Condonable Fail, 
#0-39 Fail.

jsonlike = {
        12345 : {
                "info":{
                    "name":"Rudy",
                    "course":{
                            "ECMM445":{"grade":0, "classification":"x", "marks":[50,29] },
                            "ECMM443":{"grade":0, "classification":"x", "marks":[10,4]},
                            "ECM3441":{"grade":0, "classification":"x", "marks":[40,24]},
                            "ECM3433":{"grade":0, "classification":"x", "marks":[24,34]},
                            },
                            "age":103,
                        }
                }
            }

for c in jsonlike[12345]["info"]["course"]:
    grade = sum(jsonlike[12345]["info"]["course"][c]["marks"])
    jsonlike[12345]["info"]["course"][c]["grade"] = grade
    if   grade > 70:
        jsonlike[12345]["info"]["course"][c]["classification"] = "Distinction"
    elif grade > 60:
        jsonlike[12345]["info"]["course"][c]["classification"] = "Merit"
    elif grade > 50:
        jsonlike[12345]["info"]["course"][c]["classification"] = "Pass"
    else:
        jsonlike[12345]["info"]["course"][c]["classification"] = "Fail"
print(jsonlike)