#Author: CHINMAYA KAUNDANYA
#This program is an example of insertion sort using Python

#  In Insertion sort elements get sorted in a same way playing
#  cards sort. Insertion sort is good for collections that are 
#  very small or nearly sorted. Otherwise it's not a good sorting algorithm:
#  it moves data around too much. Each time an insertion is made,
#  all elements in a greater position are shifted.

#  Best O(n); Average O(n^2); Worst O(n^2)

def insertionSort(List):
    for i in range(1, len(List)):
        currentNumber = List[i]

        # Moving elements of array, that are 
        # greater than current number, to one position ahead. 

        j = i-1
        while j >=0 and currentNumber < List[j] : 
            List[j+1] = List[j] 
            j -= 1
        List[j+1] = currentNumber 

    return List

if __name__ == '__main__':
    List = [9, 2, 5, 1, 8, 7, 3, 4, 6]
    print('Sorted List:',insertionSort(List))