import sqlite3
import json

def fillDatabase():

    #Create categories table:
    cursor.execute("create table Categories (id integer, name text)")
    categories = ['body', 'bodyColor', 'hair', 'hairColor', 'face', 'nose', 'eyes', 'eyesColor', 'eyebrows',
                  'eyebrowsColor', 'mouth', 'mouthColor']
    for idx, category in enumerate(categories, start=1):
        cursor.execute("INSERT INTO Categories (id, name) VALUES (?, ?)", (idx, category))

    #Create subcategory table:
    cursor.execute("create table Subcategories (id integer, name text, category_id integer)")
    subcategories = [('Light', 2), ('Medium', 2), ('Dark', 2),
                     ('Ash', 2), ('Copper', 2), ('Gold', 2), ('Neutral', 2), ('Rose', 2),
                     ('Short', 3), ('Medium', 3), ('Long', 3), ('Updo', 3),
                     ('Straight', 3), ('Wavy', 3), ('Curly', 3), ('Coily', 3),
                     ('Natural', 4), ('Dyed', 4),
                     ('Blacks', 4), ('Browns', 4), ('Blonds', 4), ('Reds', 4),
                     ('Pinks', 4), ('Blues', 4), ('Purples', 4), ('Greens/Yellows', 4), ('Whites/Grays', 4),
                     ('Smooth', 5), ('Hairy', 5), ('Mature', 5),
                     ('Double Eyelid', 7), ('Monolid', 7),
                     ('Natural', 8), ('Fantasy', 8),
                     ('Brown', 8), ('Blue', 8), ('Green/Gray', 8),
                     ('Natural', 10), ('Dyed', 10),
                     ('Blacks', 10), ('Browns', 10), ('Blondes', 10), ('Reds', 10), ('Misc Colors', 10),
                     ('Thin', 11), ('Full', 11), ('Human', 11), ('Vampire', 11),
                     ('Natural', 12), ('Gloss', 12), ('Matte', 12),
                     ('Nudes', 12), ('Browns', 12), ('Reds', 12), ('Pinks', 12), ('Purples', 12), ('Misc', 12)]
    for idx, subcat in enumerate(subcategories, start=1):
        cursor.execute("INSERT INTO Subcategories (id, name, category_id) VALUES (?, ?, ?)", (idx, subcat[0], subcat[1]))

    #Create assets table
    cursor.execute("create table Assets (id integer, script_name text, display_name text, category_id integer, "
                   "isFemale integer, isMale integer, canDelete integer)")

    #Create assetsSubcategories table
    cursor.execute("create table AssetsSubcategories (asset_id integer, subcategory_id integer)")

    #Create lipToSkin table
    cursor.execute("create table LipToSkin (bodyColor_id integer, mouthColor_id integer)")

    #Create templates table
    cursor.execute("create table Templates (template_id integer, name text, mc_id integer)")

    #Create characters table
    cursor.execute("create table Characters (id integer, name text, isFemale integer, template_id integer)")

    #Create TemplatesCategories table
    cursor.execute("create table TemplatesCategories (id integer, template_id integer, category_id integer, "
                   "status integer, shouldRemember integer)")

    # Create TemplatesSubcategories table
    cursor.execute("create table TemplatesSubcategories (template_id integer, subcat_id integer, status integer)")

    # Create templateAssets table
    cursor.execute("create table TemplatesAssets (template_id integer, asset_id integer)")

    # Create CategoriesCharacters table
    cursor.execute("create table CategoriesCharacters (temp_cat_id integer, char_id integer)")

    connection.commit()

    id_counter = 0

    with open("assets_female.json") as file:
        file_loaded = json.load(file)

        for key, asset in file_loaded.items():
            name = asset['displayName']
            category = asset['category']
            gender = asset['gender']
            sub_list = asset['subcategories']

            cursor.execute("select id from Categories where name = ?", (category,))
            category_id = cursor.fetchone()

            female = 0
            male = 0

            if gender == 'b':
                female = 1
                male = 1
            elif gender == 'f':
                female = 1
            elif gender == 'm':
                male = 1

            id_counter += 1

            cursor.execute("insert into Assets (id, script_name, display_name, category_id, "
                   "isFemale, isMale, canDelete) values (?,?,?,?,?,?,0)",
                           (id_counter, name, name, category_id[0], female, male,))
            connection.commit()

            for sub in sub_list:
                cursor.execute("insert into AssetsSubcategories (asset_id, subcategory_id) values (?,?)",
                               (id_counter, sub))
                connection.commit()

            if asset.get("skin tones"):
                tones = asset['skin tones']
                for bodyColor in tones:
                    cursor.execute("select id from Assets where script_name = ?", (bodyColor,))
                    bodyColor_id = cursor.fetchone()

                    cursor.execute("insert into LipToSkin (bodyColor_id, mouthColor_id) values (?,?)",
                                   (bodyColor_id[0], id_counter))
                    # print("inserted bodyColor ", bodyColor, " with id: ", bodyColor_id,
                    #       " and mouthColor ", name, " with id: ", id_counter)
                    connection.commit()


            # cursor.execute("select * from Assets where id = ?", (id_counter,))
            # res = cursor.fetchone()
            # print(id_counter, " : ", res)

    with open("assets_male.json") as file:
        file_loaded = json.load(file)

        for key, asset in file_loaded.items():
            name = asset['displayName']
            category = asset['category']
            sub_list = asset['subcategories']

            cursor.execute("select id from Categories where name = ?", (category,))
            category_id = cursor.fetchone()

            id_counter += 1

            cursor.execute("insert into Assets (id, script_name, display_name, category_id, "
                   "isFemale, isMale, canDelete) values (?,?,?,?,0,1,0)",
                           (id_counter, name, name, category_id[0],))
            connection.commit()

            # cursor.execute("select * from Assets where id = ?", (id_counter,))
            # res = cursor.fetchone()
            # print(id_counter, " : ", res)

            for sub in sub_list:
                cursor.execute("insert into AssetsSubcategories (asset_id, subcategory_id) values (?,?)",
                               (id_counter, sub))
                connection.commit()
                # print("Entered asset #", id_counter, "(", name, ") with subcategory #", sub)

            # cursor.execute("select * from AssetsSubcategories")
            # res = cursor.fetchall()
            # print(res)
def initAssets():
    global connection
    connection = sqlite3.connect('assets.db')
    global cursor
    cursor = connection.cursor()

    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table'")
    table_count = cursor.fetchone()[0]

    if table_count == 0:
        fillDatabase()

    connection.commit()

def getCategories():
    cursor.execute("SELECT name FROM Categories")
    res = cursor.fetchall()
    categories = [row[0] for row in res]
    return categories

def getSubcats(cat_id):
    cursor.execute("select * from Subcategories where category_id = ?", (cat_id,))
    return cursor.fetchall()

def getActiveSubcats(asset_id):
    cursor.execute("select * from AssetsSubcategories where asset_id = ?", (asset_id,))
    return cursor.fetchall()

def CreateNewTemplate(name, mc_name, gender):
    cursor.execute("select template_id from Templates order by template_id desc")
    res = cursor.fetchone()

    temp_id = 1
    if res is not None:
        temp_id = res[0] + 1

    # Create MC:
    isFemale = 0
    if gender == 'Female':
        isFemale = 1
    char_id = addNewCharacter(mc_name, isFemale, temp_id)

    # Create template:
    cursor.execute("insert into Templates (template_id, name, mc_id) values (?,?,?)", (temp_id, name, char_id))

    # Update categories:
    cursor.execute("select id from TemplatesCategories order by id desc")
    res = cursor.fetchone()

    temp_cat_id = 1
    if res is not None:
        temp_cat_id = res[0] + 1

    for cat_id in range(12):
        cursor.execute("insert into TemplatesCategories (id, template_id, category_id, status, shouldRemember)"
                   "values (?,?,?,1,0)", (temp_cat_id, temp_id, cat_id + 1))
        temp_cat_id += 1

    # Update Subcategories:
    cursor.execute("select count(*) from Subcategories")
    subcats_num = cursor.fetchone()[0]

    for subcat in range(subcats_num):
        cursor.execute("insert into TemplatesSubcategories (template_id, subcat_id, status)"
                       "values (?,?,1)", (temp_id, subcat + 1))

    # Update Assets:
    cursor.execute("select id from Assets")
    assets_ids = cursor.fetchall()

    for obj in assets_ids:
        cursor.execute("insert into TemplatesAssets (template_id, asset_id)"
                       "values (?,?)", (temp_id, obj[0]))

    # Update CategoriesCharacters
    cursor.execute("select id from TemplatesCategories where template_id = ?", (temp_id,))
    temp_cat_ids = cursor.fetchall()

    for id in temp_cat_ids:
        cursor.execute("insert into CategoriesCharacters (temp_cat_id, char_id)"
                       "values (?,?)", (id[0], char_id))
    connection.commit()

def getTemplate(name):
    cursor.execute("select * from Templates where name = ?", (name,))
    return cursor.fetchone()

def getTemplateNames():
    cursor.execute("select name from Templates")
    res = cursor.fetchall()

    list = []
    for obj in res:
        list.append(obj[0])

    return list

def addNewCharacter(name, isFemale, temp_id):
    cursor.execute("select id from Characters order by id desc")
    res = cursor.fetchone()

    char_id = 1
    if res is not None:
        char_id = res[0] + 1

    cursor.execute("insert into Characters (id, name, isFemale, template_id) values (?,?,?,?)",
                       (char_id, name, isFemale, temp_id))

    connection.commit()
    return char_id

def getCharacter(id):
    cursor.execute("select * from Characters where id = ?", (id,))
    return cursor.fetchone()

def getCharacterByName(name):
    cursor.execute("select * from Characters where name = ?", (name,))
    return cursor.fetchone()

def getRelatives(temp_id, mc_id):
    cursor.execute("select id, name, isFemale from characters where id <> ? and template_id = ?", (mc_id, temp_id))
    return cursor.fetchall()
def isOriginalTemplate(name):
    cursor.execute("select 1 from Templates where name = ?", (name,))
    res = cursor.fetchone()

    # print("res is ", res)

    return res is None

def isOriginalAsset(script_name, category, gender):
    cursor.execute("select id from Categories where name = ?", (category,))
    cat_id = cursor.fetchone()[0]
    # print(cat_id)
    if gender == "Female":
        cursor.execute("select 1 from Assets where script_name = ? and category_id = ? and isFemale = 1",
                       (script_name, cat_id))
    elif gender == "Male":
        cursor.execute("select 1 from Assets where script_name = ? and category_id = ? and isMale = 1",
                       (script_name, cat_id))
    else:
        cursor.execute("select 1 from Assets where script_name = ? and category_id = ? and (isFemale = 1 or isMale = 1)",
                       (script_name, cat_id))
    res = cursor.fetchone()
    # print(res)
    return res is None

def updateAssetDisplayName(asset_id, display_name):
    cursor.execute("update Assets set display_name = ? where id = ?", (display_name, asset_id))
    connection.commit()

def updateSubcategories(asset_id, subcats_ids):
    cursor.execute("delete from AssetsSubcategories where asset_id = ?", (asset_id,))
    for subcat in subcats_ids:
        cursor.execute("insert into AssetsSubcategories values (?,?)", (asset_id, subcat))
    connection.commit()


def GetCatGenderFromStr(string):
    cat_id = 0
    isFemale = 0
    isMale = 0
    if string == "Body Type (Female)":
        cat_id = 1
        isFemale = 1
    elif string == "Body Type (Male)":
        cat_id = 1
        isMale = 1
    elif string == "Skin Tone":
        cat_id = 2
        isFemale = 1
        isMale = 1
    elif string == "Hairstyle (Female)":
        cat_id = 3
        isFemale = 1
        isMale = 0
    elif string == "Hairstyle (Male)":
        cat_id = 3
        isFemale = 0
        isMale = 1
    elif string == "Hair color":
        cat_id = 4
        isFemale = 1
        isMale = 1
    elif string == "Face Shapes (Female)":
        cat_id = 5
        isFemale = 1
        isMale = 0
    elif string == "Face Shapes (Male)":
        cat_id = 5
        isFemale = 0
        isMale = 1
    elif string == "Nose (Female)":
        cat_id = 6
        isFemale = 1
        isMale = 0
    elif string == "Nose (Male)":
        cat_id = 6
        isFemale = 0
        isMale = 1
    elif string == "Eye Shapes (Female)":
        cat_id = 7
        isFemale = 1
        isMale = 0
    elif string == "Eye Shapes (Male)":
        cat_id = 7
        isFemale = 0
        isMale = 1
    elif string == "Eye Colors":
        cat_id = 8
        isFemale = 1
        isMale = 1
    elif string == "Eyebrows (Female)":
        cat_id = 9
        isFemale = 1
        isMale = 0
    elif string == "Eyebrows (Male)":
        cat_id = 9
        isFemale = 0
        isMale = 1
    elif string == "Eyebrow Colors":
        cat_id = 10
        isFemale = 1
        isMale = 1
    elif string == "Lip Shapes (Female)":
        cat_id = 11
        isFemale = 1
        isMale = 0
    elif string == "Lip Shapes (Male)":
        cat_id = 11
        isFemale = 0
        isMale = 1
    elif string == "Lip Colors":
        cat_id = 12
        isFemale = 1
        isMale = 1
    return (cat_id, isFemale, isMale)

def getAssetsByGender(data, getOnlyDeletables = True):
    if getOnlyDeletables:
        onlyDeletables = " and canDelete = 1"
    else:
        onlyDeletables = ""

    if data[1] and not data[2]:
        cursor.execute("select script_name from Assets where category_id = ? and isFemale = 1" + onlyDeletables,
                       (data[0],))
    elif data[2] and not data[1]:
        cursor.execute("select script_name from Assets where category_id = ? and isMale = 1" + onlyDeletables,
                       (data[0],))
    elif data[1] and data[2]:
        cursor.execute("select script_name from Assets where category_id = ? and isMale = 1 and isFemale = 1"
                       + onlyDeletables,(data[0],))
    res = cursor.fetchall()
    list = []
    for obj in res:
        list.append(obj[0])
    list.sort()
    return list

def addAsset(script_name, display_name, genders, cat, subcategories):
    cursor.execute("select id from Assets order by id desc")
    id = cursor.fetchone()[0] + 1

    cursor.execute("select id from Categories where name = ?", (cat,))
    category_id = cursor.fetchone()[0]

    isFemale = 0
    isMale = 0
    if genders == 'Female' or genders == 'Both':
        isFemale = 1
    if genders == 'Male' or genders == 'Both':
        isMale = 1

    script_name = script_name.title()
    display_name = display_name.title()

    cursor.execute("insert into Assets (id, script_name, display_name, category_id, "
                   "isFemale, isMale, canDelete) values (?,?,?,?,?,?,1)",
                   (id, script_name, display_name, category_id, isFemale, isMale))
    # print("New asset created! ID: ", id , ", script name: ", script_name, ", display name:", display_name, ", category: ",
    #       cat, "(", category_id, "), gender: ", genders, "(", isFemale, ", ", isMale, ").")

    for sub in subcategories:
        cursor.execute("insert into AssetsSubcategories (asset_id, subcategory_id) values (?,?)",
                        (id, sub))
        # print("subcategory: ", sub)
    connection.commit()

def getAssetData(catGender, name):
    string = ""
    if catGender[1] == 0:
        string = " and isMale = " + str(catGender[2])
    elif catGender[2] == 0:
        string = " and isFemale = " + str(catGender[1])

    cursor.execute("select * from Assets where category_id = ? and script_name = ?" + string,
                   (catGender[0], name))
    data = cursor.fetchone()
    return data


def deleteAsset(data, asset_name):
    # print(category, gender, asset_name)
    if data[1] and not data[2]:
        cursor.execute("select id from Assets where category_id = ? and isFemale = 1 and script_name = ?",
                       (data[0], asset_name))
    elif data[2] and not data[1]:
        cursor.execute("select id from Assets where category_id = ? and isMale = 1 and script_name = ?",
                       (data[0], asset_name))
    elif data[1] and data[2]:
        cursor.execute("select id from Assets where category_id = ? and isFemale = 1 and isMale = 1 and script_name = ?",
                       (data[0], asset_name))

    id = cursor.fetchone()[0]
    # print(id)
    cursor.execute("delete from AssetsSubcategories where asset_id = ?", (id,))
    cursor.execute("delete from Data where asset_id = ?", (id,))
    cursor.execute("delete from Assets where id = ?", (id,))

    connection.commit()
def getAllAssets():
    allAssets = {}

    #Female Body types:
    cursor.execute("select * from Assets where isFemale = 1 and category_id = 1")
    res = cursor.fetchall()

    fem1 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        fem1.append(line)
        # print(line)
    fem1.sort()
    allAssets["Female Body Types"] = fem1

    # Male Body types:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 1")
    res = cursor.fetchall()

    male1 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        male1.append(line)
        # print(line)
    male1.sort()
    allAssets["Male Body Types"] = male1

    #All body colors:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 2")
    res = cursor.fetchall()

    both2 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        both2.append(line)
        # print(line)
    both2.sort()
    allAssets["All Body Colors"] = both2

    # Female hair types:
    cursor.execute("select * from Assets where isFemale = 1 and category_id = 3")
    res = cursor.fetchall()

    fem3 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        fem3.append(line)
        # print(line)
    fem3.sort()
    allAssets["Female Hairstyles"] = fem3

    # Male hair types:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 3")
    res = cursor.fetchall()

    male3 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        male3.append(line)
        # print(line)
    male3.sort()
    allAssets["Male Hairstyles"] = male3

    # All hair colors:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 4")
    res = cursor.fetchall()

    both4 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        both4.append(line)
        # print(line)
    both4.sort()
    allAssets["All Hair Colors"] = both4

    # Female faces:
    cursor.execute("select * from Assets where isFemale = 1 and category_id = 5")
    res = cursor.fetchall()

    fem5 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        fem5.append(line)
        # print(line)
    fem5.sort()
    allAssets["Female Face Shapes"] = fem5

    # Male faces:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 5")
    res = cursor.fetchall()

    male5 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        male5.append(line)
        # print(line)
    male5.sort()
    allAssets["Male Face Shapes"] = male5

    # Female noses:
    cursor.execute("select * from Assets where isFemale = 1 and category_id = 6")
    res = cursor.fetchall()

    fem6 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        fem6.append(line)
        # print(line)
    fem6.sort()
    allAssets["Female Noses"] = fem6

    # Male noses:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 6")
    res = cursor.fetchall()

    male6 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        male6.append(line)
        # print(line)
    male6.sort()
    allAssets["Male Noses"] = male6

    # Female eyes
    cursor.execute("select * from Assets where isFemale = 1 and category_id = 7")
    res = cursor.fetchall()

    fem7 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        fem7.append(line)
        # print(line)
    fem7.sort()
    allAssets["Female Eye Shapes"] = fem7

    # Male eyes:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 7")
    res = cursor.fetchall()

    male7 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        male7.append(line)
        # print(line)
    male7.sort()
    allAssets["Male Eye Shapes"] = male7

    # All eye colors:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 8")
    res = cursor.fetchall()

    both8 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        both8.append(line)
        # print(line)
    both8.sort()
    allAssets["All Eye Colors"] = both8

    # Female eyebrows
    cursor.execute("select * from Assets where isFemale = 1 and category_id = 9")
    res = cursor.fetchall()

    fem9 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        fem9.append(line)
        # print(line)
    fem9.sort()
    allAssets["Female Eyebrows"] = fem9

    # Male eyebrows:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 9")
    res = cursor.fetchall()

    male9 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        male9.append(line)
        # print(line)
    male9.sort()
    allAssets["Male Eyebrows"] = male9

    # All eyebrow colors:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 10")
    res = cursor.fetchall()

    both10 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        both10.append(line)
        # print(line)
    both10.sort()
    allAssets["All Eyebrow Colors"] = both10

    # Female mouth
    cursor.execute("select * from Assets where isFemale = 1 and category_id = 11")
    res = cursor.fetchall()

    fem11 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        fem11.append(line)
        # print(line)
    fem11.sort()
    allAssets["Female Lips"] = fem11

    # Male mouth:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 11")
    res = cursor.fetchall()

    male11 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        male11.append(line)
        # print(line)
    male11.sort()
    allAssets["Male Lips"] = male11

    # All mouth colors:
    cursor.execute("select * from Assets where isMale = 1 and category_id = 12")
    res = cursor.fetchall()

    both12 = []
    for row in res:
        line = row[2] + " (" + row[1] + ")"
        line.replace("}", "\n")
        both12.append(line)
        # print(line)
    both12.sort()
    allAssets["All Lip Colors"] = both12

    return allAssets