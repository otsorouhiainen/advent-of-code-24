def main():
  file = open("day1-input.txt", "r")
  result = 0
  list1 = []
  list2 = []
  for line in file:
    split = line.split()
    list1.append(split[0])
    list2.append(split[1])
  
  sortedList1 = sorted(list1)
  sortedList2 = sorted(list2)

  for i in range(len(sortedList1)):
    x = int(sortedList1[i])
    y = int(sortedList2[i])
    if x > y:
      result = result + (x - y)
    else:
      result = result + (y - x)
  print(result)


if __name__=="__main__":
    main()