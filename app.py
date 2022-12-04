# Made with <3 by team nokimchi
# Use this command to run the application: python app.py


import pymongo
import functions as fn
from ui_controller import UI_controller
import os

def appUI():
    mainmenu = """
    Select Option: 

    A. Insert author with [name: string] 
    B. Update Add author [work_id: string, book_id: string, and increment works_count: int] using [_id: string] 
    C. Update author [about: string] using [_id: string] 
    D. Update author [gender: string] using [_id: string] 
    E. Update author [imageurl: string] using [_id: string] 
    F. Delete author 
    G. List of Series [title: string] by author [name: string] (combining 2 tables) 
    H. Find authors who have an average rating in given range 
    I. Find image urls using [name: string] 
    J. Get all data of author using [_id: string] 
    K. Get authors with particular [gender: string] 
    L. Get author about info using [name: string] 
    M. Find authors with text_reviews_count in given range 
    N. Find authors with fans_count & ratings_count in given ranges
    O. Find authors with works_count in given range 

    X. EXIT

    """
    try:
        while(True):        
            option = input(mainmenu)
            UI_controller(option)
            
            if(option=='X' or option=='x'):
                return -1
                exit(0)
            
            _ = input("\nPress Enter to Continue...")
            os.system('cls')

    except Exception as e: 
        print(e)
        print("Error!")
        _ = input("\nPress Enter to Continue...")
        os.system('cls')
        appUI()

    


if __name__=="__main__":
    myclient = pymongo.MongoClient("mongodb://ec2-3-235-20-235.compute-1.amazonaws.com:27020/test")

    fn.db = myclient["nosql_project"]
    fn.cl = fn.db["authors"]
    
    appUI()

