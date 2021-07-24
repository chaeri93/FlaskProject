from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'매트릭스'})
print(movie['star'])

target_star = movie['star']
same_stars = list(db.movies.find({'star':target_star},{'_id':False}))
for target in same_stars:
    print(target['title'])

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})#0이라는 문자열을 넣어줘 DB에 있는 타입들 통일시키기
