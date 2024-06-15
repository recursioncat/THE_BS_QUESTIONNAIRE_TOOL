import random

class UnfinishedList(Exception):
    pass

def WeightedRandom(li:list, limit:int):
    
    if sum(li)!= 1:
        raise UnfinishedList("The Weights Do not add Up to One")
    
    final_list = []
    for index, value in enumerate(li):
        final_list += list([index]*(int(round(value*limit))))
    
    if len(final_list)<limit:
        final_list.append(li.index(random.choice(li)))
    
    random.shuffle(final_list)
    
    return final_list


