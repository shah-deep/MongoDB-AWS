# Group name: nokimchi
# Run app.py

from functions import *

def UI_controller(op):

    if(op=="A" or op=="a"):
        # Example: name: Yunseo Claire Han, gender: female, about: fake author
        d = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in input("Details in comma-separated key-value pair: \n").split(', ')}
        print(d)
        insertAuthor_f1(d)

    elif(op=="B" or op=="b"):
        # Example: 54, 7239928, 37492817
        a, w, b = [v for v in input("author_id, new work_id, new book_id : \n").split(', ')]
        print(a, w, b)
        updateWorkBookCnt_f2(a, w, b)

    elif(op=="C" or op=="c"):
        # Example: 54, She lives in South Florida with her three dogs and two cats. Chasing Jordan is her first novel. 
        i, ab = [v for v in input("author_id, new about: \n").split(', ')]
        updateAbout_f3(i, ab)
    
    elif(op=="D" or op=="d"):
        # Example: 16777266, female
        i, g = [v for v in input("author_id, Gender: \n").split(', ')]
        updateGender_f4(i, g.lower())

    elif(op=="E" or op=="e"):
        # Example: 32, https://images.gr-assets.com/authors/1331411219p5/32.jpg
        at, img = [v for v in input("author_id, image_url: \n").split(', ')]
        updateImage_f5(at, img)

    elif(op=="F" or op=="f"):
        # Example: name: Yunseo Claire Han, gender: female
        x = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in input("Enter record details in comma-separated key-value pair to select for deletion: \n").split(', ')}
        delete_f6(x)

    elif(op=="G" or op=="g"):
        # Example: Elaine Cunningham
        x = input("Author Name: ")
        pprint(series_by_author_f7(x))

    elif(op=="H" or op=="h"):
        # Example: 4, 5, 10
        s, b, l  = [int(v) for v in input("Range: min, max, limit \n").split(', ')]
        pprint(avg_rating_f8(s,b,l))

    elif(op=="I" or op=="i"):
        # Example: Elaine Cunningham
        x = input("Author Name: ")
        pprint(imgurl_f9(x))

    elif(op=="J" or op=="j"):
        # Example: 54
        x = input("Author ID: ")
        authordata_f10(x)

    elif(op=="K" or op=="k"):
        # Example: Female, 5
        g, l = [v for v in input("Gender, Limit : \n").split(', ')]
        pprint(gender_f11(g.lower(), int(l)))

    elif(op=="L" or op=="l"):
        # Example: Heidi W. Boehringer
        x = input("Author Name: ")
        pprint(about_f12(x))

    elif(op=="M" or op=="m"):
        # Example: 1000, 1005
        s, l = [int(v) for v in input("Range: min, max \n").split(', ')]
        pprint(text_rev_f13(s, l))

    elif(op=="N" or op=="n"):
        # Example: 
        # 50, 60
        # 5, 7
        f1, f2 = [int(v) for v in input("fans_count min, fans_count max : ").split(', ')]
        r1, r2 = [int(v) for v in input("ratings_count min, ratings_count max : ").split(', ')]
        pprint(fan_ratcnt_f14([f1, f2], [r1, r2]))

    elif(op=="O" or op=="o"):
        # Example: 15000, 20000
        s, l = [int(v) for v in input("Range: min, max \n").split(', ')]
        pprint(works_f15(s, l))

    elif(op=="X" or op=="x"):
        print("Thanks for using this application! \n")

    else:
        print("Please enter item alphabet from the menu...")

