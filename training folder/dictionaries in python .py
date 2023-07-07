course={
    "title":"python",
    "teacher":"ordookhani",
    "duration":26,
    "tags":["python","programming","back_end","ordookhani","free"],
    "related courses":[
        {"title":"Java",
    "teacher":"dehyami",
    "duration":20,
    "tags":["Java","programming","back_end","dehyami","free"]    
        },
        {"title":"PHP",
    "teacher":"Avand",
    "duration":49,
    "tags":["php","programming","back_end","Avand","free"]   
        }
    ] 
}

print([i["title"] for i in course["related courses"]])


print({str(num):num for num in range(4)})
print({str(num):(num*2 if num%2==0 else num*3  )for num in range(4)})