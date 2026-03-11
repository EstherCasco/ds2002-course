import os
from pymongo import MongoClient

def main():
        url= os.getenv("MONGODB_ATLAS_URL")
        user= os.getenv("MONGODB_ATLAS_USER")
        password = os.getenv("MONGODB_ATLAS_PWD")

        if url is None or user is None or password is None:
            print("Error: MongoDB environment variables are missing.")
            return

       #Connection
        client = MongoClient(url, username=user, password=password)
        db = client["bookstore"]
        authors = db["authors"]
        total = authors.count_documents({})

        #Reports
        print("Bookstore Author Report")
        print("Total number of authors:", total)
        print()

        #Authors
        for author in authors.find():
                print("Name: ", author["name"])
                print("Nationality: ", author["nationality"])
                print()

        client.close() #closing connection

if __name__ == "__main__":
        main()
