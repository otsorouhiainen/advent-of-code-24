def main():
  file = open("day1-input.txt", "r")
  result = 0
  list1 = []
  list2 = []
  for line in file:
    split = line.split()
    list1.append(split[0])
    list2.append(split[1])
  
  sortedList1 = list1
  sortedList2 = list2

  for i in range(len(sortedList1)):
    occurences = sortedList2.count(sortedList1[i])
    result = result + int(sortedList1[i]) * occurences

  print(result)

if __name__=="__main__":
    main()