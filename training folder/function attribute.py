def school_avg(l):
    return (sum(l)/len(l))


school_avg.name = "Imam Reza"

school_avg.amount_of_courses = 8

print(dir(school_avg))
print(school_avg.__dict__) 
setattr(school_avg,"grade",2)

print(school_avg.__dict__) 

x = getattr(school_avg,"name")
print(x)

delattr(school_avg,"amount_of_courses")

print(school_avg.__dict__) 
