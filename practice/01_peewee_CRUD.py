from helper_functions import clear_screen
clear_screen()

# ===========
# PEEWEE CRUD
# ===========


# 1. CREATE A PEEWEE MODEL AND SQLITE DATABASE
# Create a SQLite Database called cats.db through peewee
'''
It should have the following columns:
    - cat_id (the primary key)
    - cat_name
    - cat_age
    - owner_name
'''
import peewee as p

db = p.SqliteDatabase('cats.db')

class Cats(p.Model):
    cat_id = p.AutoField(primary_key=True)
    cat_name = p.CharField()
    cat_age = p.IntegerField()
    owner_name = p.CharField()

    class Meta:
        database = db

    def get_info(self):
        return f"{self.cat_name}, age {self.cat_age} is owned by {self.owner_name}"
        
    @classmethod
    def create(cls, **query):
        cat_name = query['cat_name']
        owner_name = query.get('owner_name')

        # make them capitalized and strip extra space
        # title will capitalize every separate word
        cat_name = cat_name.strip().title()
        owner_name = owner_name.strip().title()

        # put the changed values back into the dictionary before calling super
        query['cat_name'] = cat_name
        query['owner_name'] = owner_name

        return super().create(**query)


db.connect()
db.create_tables([Cats])


# 2. CREATE A ROW USING INPUTS
# Ask the user for inputs for the cat_name, owner_name, and age to create new rows
# in the database

while True:
    
    print("Welcome to Cat Land! Choose an option:")
    print("1. Add a new cat: ")
    print("2. See all cats")
    print("3. See all cats of specific owner")
    print("4. See the youngest cat")
    print("exit - leave the program")
    option = input("Enter an option: ")

    if option == '1':
        input_cat_name = input("Enter a cat name: ")
        input_owner_name = input("Enter a owner name: ")
        input_cat_age = int(input("Enter a cat age: "))

        Cats.create(cat_name=input_cat_name, owner_name=input_owner_name, cat_age=input_cat_age)

    elif option == '2':
        all_cats = Cats.select().order_by(Cats.cat_name.desc())
        for cat_obj in all_cats:
            print(cat_obj.get_info())
        print()

    elif option == '3':
        owner_name = input("Enter an owner name to see all their cats: ")
        cats_of_owner = Cats.select().where(Cats.owner_name == owner_name)

        if len(cats_of_owner) > 0:
            print(f"These are {owner_name}'s cats")
            for cat_obj in cats_of_owner:
                print(cat_obj.get_info())

        else:
            print(f"Couldn't find any cats with the owners name of {owner_name}")

    elif option == '4':
        youngest_cat = Cats.select().order_by(Cats.cat_age.asc()).first()
        print("This is the youngest cat!")
        print(youngest_cat.get_info())


    elif option.lower() == 'exit':
        print("Thanks for using the program")
        break

    else:
        print("Invalid choice, choose again!")





# 3. OVERRIDE THE CREATE FUNCTION
# Override the create function to make sure that every cat_name and
# owner_name gets stored as a capitalized version. (e.g. "max" or "MAX" should
# be stored as "Max") Don't stop anything from being created, just make it so
# the first letter is capitalized and that it is stored without leading or
# trailing spaces.

# .capitalize() .strip()


# 4. ADD A GET_INFO METHOD TO THE CAT CLASS
# In your Cat class, add a method called "get_info" that returns the
# cat's name, owner name and age in a nicely formatted string.



# 5. MAKE A MENU AND ADD A READ OPTION
# Make a menu. Option 1 is to add a new cat (for what you did in #1)
# Option 2 is to see all cats. When option 2 is selected, make it so that the
# cats print out in reverse alphabetical order by cat_name. The menu should
# repeat until the user enters "exit"



# 6. READ A SPECIFIC SUBSET (OPTION 3)
# Add option 3. Option 3 should ask for an owner's name. If the owner name
# exists, make it show all the cats with that owner_name. If the owner_name
# doesn't exist in the database, display a message that that owner couldn't be
# found, and go back to the menu.



# 6. FIND THE YOUNGEST CAT (OPTION 4)
# Add option 4. Option 4 should display the the get_info of the youngest cat 
# in the database. For simplicity, if there is a tie for the youngest, you 
# can just display one. (If you want a little extra challenge, feel free to
# try and write code that accounts for a tie for youngest age)


# 7. UPDATE A ROW  (OPTION 5)
# Add option 5. Enter a cat's id to get it, then enter a new name, and save
# that name. For time's sake you can assume the Id entered will always be valid


# 8. DELETE A ROW (OPTION 6)
# Add option 6. Enter a cat's id to get it, then delete it. Print out a
# message that it was deleted.
