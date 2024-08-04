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

def randomOfOne(number_of_options):
    temp_list = []
    for i in range(number_of_options):
        temp_list.append(random.randint(1, 10))

    sumOfWeights = sum(temp_list)
    weights = []

    for i, value in enumerate(temp_list):
        weights.append(round(value/sumOfWeights, 2))
    
    print("Weights from Randomgen: ", weights)


    #checks if nthe sum is not one
    if sum(weights)!=1:
       weights = randomOfOne(number_of_options)

    
    return weights



if __name__ == "__main__":
    print(randomOfOne(4))

