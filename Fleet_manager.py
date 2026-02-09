def Display_menu(names,ranks,divs,ids):
 while True:
        print("----MENU----")
        print("Database: 1")
        print("Add members: 2")
        print("remove members: 3")
        print("update rank: 4")
        print("display roster: 5")
        print("search_crew: 6")
        print("filter_by_division: 7")
        print("count officers: 8")
        print("Payroll: 9")
        option = input("Please slecect an option :")

        if option == "1":
            print(names)
            print(ranks)
            print(divs)
            print(ids)
        elif option  == "2":
            names, ranks, divs, ids = add_members(names, ranks, divs, ids)
        elif option == "3":
            names,ranks,divs,ids = remove_members(names,ranks,divs,ids)
        elif option == "4":
            names,ranks,ids = update_members(names,ranks,ids)
        elif option == "5":
            names,ranks,divs,ids = display_roster(names,ranks,divs,ids)
        elif option == "6":
            names,ranks,divs,ids = search_crew(names, ranks, divs, ids)
        elif option == "7":
            names,divs = filter_by_division(names, divs)
        elif option == "8":
            ranks = count_officers(ranks)
        elif option == "9":
            ranks = calculate_payroll(ranks)


def init_database():
    n = ["Picard", "Riker", "Data", "Worf","B'Etor"]
    r = ["Captain", "Commander", "Lt.Commander", "Lieutenant","Commander"]
    d = ["Command", "Command", "Operations", "Security","First officer"]
    ids = ["12", "16", "23", "42","23"]

    return n,r,d,ids

def add_members(names,ranks,divs,ids):
    name = input(("What is the name: "))
    rank = input("What is the rank: ")
    div = input("What is the division: ")
    while True:
        id_new = input("What is the id: ")
        if id_new in ids:
            print("Already exists add new id:")
        else:
            names.append(name)
            ranks.append(rank)
            divs.append(div)
            ids.append(id_new)
            print("Added")
            break

    return names, ranks , divs , ids
    
def remove_members(names,ranks,divs,ids):
    id_slct = input("What is the id of the person you are trying to delete:")
    index = ids.index(id_slct)
    names.pop(index)
    ranks.pop(index)
    divs.pop(index)
    ids.pop(index)
    print("Everything is deleted")
    return names,ranks,divs,ids


def update_members(names,ranks,ids):
    ids_slct = input("what is the id of the person you are trying to add:")
    index = ids.index(ids_slct)
    rank_change = input("What rank would you like to change it to:")
    ranks[index] = rank_change
    print(ranks)
    print("Updated")
    return names , ranks , ids

def display_roster(names,ranks,divs,ids):
    for i in range(len(ids)):
        print(f'name:',names[i],'rank:',ranks[i],'Divison:',divs[i],'ID:',ids[i])
        
    
    return names,ranks,divs,ids





names,ranks,divs,ids = init_database()
Display_menu(names, ranks, divs, ids)
    