# Group name: nokimchi
# Run app.py

from pprint import pprint

global db, cl

def insertAuthor_f1(indata):
    print("Inserting Author...")
    cl.insert_one(indata)
    checkRecord(indata)

def updateWorkBookCnt_f2(id, workdata, bookdata):
    print("Updating Author Data...")
    cl.update_one({"_id": id}, {"$inc": {"works_count":1}, "$push": {"work_ids": workdata, "book_ids": bookdata} })
    checkRecord({"_id": id})

def updateAbout_f3(id, newValue):
    print("Updating Author Data...")
    cl.update_one({"_id": id}, {"$set": {"about":newValue}})
    checkRecord({"_id": id, "about":newValue})

def updateGender_f4(id, newValue):
    print("Updating Author Data...")
    cl.update_one({"_id": id}, {"$set": {"gender":newValue}})
    checkRecord({"_id": id, "gender":newValue})

def updateImage_f5(id, newValue):
    print("Updating Author Data...")
    cl.update_one({"_id": id}, {"$set": {"image_url":newValue}})
    checkRecord({"_id": id, "image_url":newValue})


def checkRecord(cdata):
    for _ in cl.find(cdata).limit(1):
        print("Record Updated Successfully") 
        return True

    print("Error: Updated Failed")
    return False

def delete_f6(filter):
    x = cl.delete_many(filter)
    print(x.deleted_count, "documents deleted.")
    for _ in cl.find(filter).limit(1):
        print("Error: Delete Failed") 
        return False

    print("Records Deleted Successfully")
    return True


def series_by_author_f7(aname):
    wids = []
    for x in cl.find({"name":aname}, {'work_ids':1}):
        wids += x['work_ids']

    if(wids==[]):
        return []

    titles = []
    for x in db.series.find({"works.work_id": {"$in": wids}}, {"title":1}):
        titles.append(x['title'])
    
    return titles


def avg_rating_f8(minr, maxr, limit):   
    names = []
    query = {"average_rating": {"$gte": minr, "$lte": maxr}}
    project = {"_id":0, "name": 1, "average_rating": 1}
    for x in cl.find(query, project).limit(limit):
        names.append(f"Name: {x['name']}, Rating: {x['average_rating']}")

    return names


def imgurl_f9(name):
    img = []
    for x in cl.find({"name":name}, {'image_url':1}):
        img.append(x['image_url'])
        
    return img


def authordata_f10(id):
    for x in cl.find({"_id":id}):
        pprint(x)
        return x


def gender_f11(g, l):
    gl = []
    for x in cl.find({"gender":g}, {'name':1}).limit(l):
        gl.append(x['name'])
        
    return gl

def about_f12(name):
    ab = []
    for x in cl.find({"name":name}, {'about':1}):
        ab.append([x['_id'], x['about']])
        
    return ab

def text_rev_f13(minr, maxr):   
    names = []
    query = {"text_reviews_count": {"$gte": minr, "$lte": maxr}}
    project = {"_id":0, "name": 1, "text_reviews_count": 1}
    for x in cl.find(query, project):
        names.append(f"Name: {x['name']}, Cnt: {x['text_reviews_count']}")

    return names

def fan_ratcnt_f14(fans, ratin):   
    names = []
    query = {"fans_count": {"$gte": fans[0], "$lte": fans[1]}, "ratings_count": {"$gte": ratin[0], "$lte": ratin[1]}}
    project = {"_id":0, "name": 1, "fans_count": 1, "ratings_count": 1}
    for x in cl.find(query, project):
        names.append(f"Name: {x['name']}, fans_count: {x['fans_count']}, ratings_count: {x['ratings_count']}")

    return names

def works_f15(minr, maxr):   
    names = []
    query = {"works_count": {"$gte": minr, "$lte": maxr}}
    project = {"_id":0, "name": 1, "works_count": 1}
    for x in cl.find(query, project):
        names.append(f"Name: {x['name']}, Cnt: {x['works_count']}")

    return names
