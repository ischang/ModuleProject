gayList = [2010,2,2009,4,1989,2009,7]
years_dict = dict()

for shit in gayList:
    if shit in years_dict:
        # append the new number to the existing array at this slot
        years_dict[shit].append(2)
    else:
        # create a new array in this slot
        years_dict[shit] = [3]
print years_dict