#Author: CHINMAYA KAUNDANYA
#This program is an example of selection sort

#Selection sort iterates all the elements and if the smallest element in the list is found then that number
#is swapped with the first

#Best->    O(n^2);
#Average-> O(n^2); 
#Worst->    O(n^2)

def selectionSort(List):
    for i in range(len(List) - 1): #For iterating n - 1 times
        minimum = i
        for j in range( i + 1, len(List)): # Compare i and i + 1 element
            if(List[j] < List[minimum]):
                minimum = j
        if(minimum != i):
            List[i], List[minimum] = List[minimum], List[i]
    return List

if __name__ == '__main__':
    List = [9, 2, 5, 1, 8, 7, 3, 4]
    print('Sorted List:',selectionSort(List))