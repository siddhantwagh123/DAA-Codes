'''Implement a problem of activity selection problem with K persons.

Statement:- Given two arrays S[] and E[] of size N denoting starting and closing time of the shops and an integer value K denoting the 
number of people, the task is to find out the maximum number of shops they can visit in total if they visit each shop optimally based 
on the following conditions:

* A shop can be visited by only one person
* A person cannot visit another shop if its timing collide with i'''

def max_shops_visited(S, E, K):
    #Step 1:Pair and sort the shops based on end time and start time
    shops = sorted(zip(S, E), key=lambda x: (x[1], x[0]))
    
    #Step 2:Initialize a list to track the end time of the last shop visited by each person
    persons = [0] * K  #List of size K initialized to 0
    
    #Step 3:Greedily assign shops to persons
    count = 0
    for shop in shops:
        for i in range(K):
            if persons[i] <= shop[0]:  #Person i can visit this shop
                persons[i] = shop[1]  #Update the end time for person i
                count += 1
                break  #Move to the next shop after assigning to a person
                
    return count

#Take input from user
S = list(map(int,input("Enter the start times of the shops: ").split()))
E = list(map(int,input("Enter the end times of the shops: ").split()))
K = int(input("Enter the number of people: "))


result = max_shops_visited(S, E, K)
print("The maximum number of shops that can be visited is:", result)
