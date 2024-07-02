#1 Duplicate sandwich
def duplicate_sandwich(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) > 1:
            element = arr[i]
            break

    first_index = arr.index(element)
    second_index = arr.index(element, first_index + 1)
    return arr[first_index + 1:second_index]


#2 Conference Traveller

def conference_picker(cities_visited, cities_offered):
    for city in cities_offered:
        if city not in cities_visited:
            return city
    return 'No worthwhile conferences this year!'

#3 Sum of a nested list
def sum_nested(lst):
    total = 0
    for element in lst:
        if isinstance(element, list):
            total += sum_nested(element)
        else:
            total += element
    return total

#4 Disorganised page lists
def find_page_number(pages):
    n = [1]
    return [i for i in pages if n[-1] != i or n.append(n[-1]+1)]

#5 Describe a list
def describe_list(lst):
    if not lst:
        return "empty"
    elif len(lst) == 1:
        return "singleton"
    else:
        return "longer"











