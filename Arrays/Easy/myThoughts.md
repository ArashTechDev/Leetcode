This problem was extremely easy to solve in O(nlogn) via squaring all elements and then sorting it. 
Completing it in O(n) took a bit of effort, 
  I basically went through each element once and if it was <0:
                                                              It would be sent to a list (decreasing order) , lets call it decList
                                                if it was 0:
                                                              It would be added to the list we will return , lets call it returnList
                                                if it was >0:
                                                              It would be compared with the last element in decList, i.e. decList[-1] and then the smaller squared num would be placed in the returnList
    
