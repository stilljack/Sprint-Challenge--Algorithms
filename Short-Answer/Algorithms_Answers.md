#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
 I believe this is at absolute worse linear time O(n), or likely, i believe even better -- closer to constant O(1) time. I would be lying if I said I understand the gradient between O(n) and O(1) and without googling extensively I don't think I can meaningfully explain why I am inclined to believe this.
  that being said, gesturing in that direction, the while loop has only one operation, an assignment composed of a's value  + sum(n*n). assignment is itself o(n) i believe and raising sum(n*n)should be relatively trivial, further we can i believe surmise that since we are increasing by sum(n*n) each loop until we reach sum(n*n*n), should i believe take n steps...

     I gotta brush up on my math, and my abilitity to answer these sorts of questions.

b) at first glance this appears to be two loops nested, so my first instinct is closer to O(n^2), however as we see that j actually increased by a factor of 2 each cycle, i believe we are close to O(n log n) -- I truly don't understand log however, my understanding from the last week is that O(n log n) captures these "partial double loops". i.e algos which capture a full iteration through a set at plus 30-50% (as a ball park, obviously the relationship is actually more nuanced as the performance of O(n log n) is more more acceptable than that for larger numbers and does not increase at an exponential rate, but the more reasonable logaritimic)


c) bunny ears is a recursive function which complicates matters as depending on the runtime that this function executes in will alter its performance, as far as my research this week indicated, almost always for the worse and in some cases much, much worse than an iterative function. that being said, I believe we would be expecting O(n) aproximately. There is only one check within bunnie ears and then the relaunch of itself n-1 times (for n total function executions total) -- so while O(n) I think is the correct rounded error, that does not necessarily capture the performance issues inherent to using a recursive function at all.

## Exercise II

   so our problem space is a n digit array of positive integers (even if you consider say mezanines or 13th floors being missing, there are only whole floors and ultimately the shape of the representation of the floors could be smoothed to being positive integers), we want to find the highest f such that the egg can be thrown off without breaking and we want to break as few eggs as possible so --

   if we take "break as few eggs as possible" and "we have plenty of eggs" to mean we should execute the most effective use of our compute available, without trying to overly cautious and trying to get the highest reasonable floor f -- the most obvious solution is to implement a binary sort, given that buildings are relatively small in number of floors (i.e. sub 200) and all floors are sorted and and positive integers -- our binary search should have a relatively easy time.

   binary search in plain english works by finding a middle or pivot point, generally in the middle of the array to be searched and checking if we need to go to right or left in the array to find the target, i.e. if the answer is higher or lower than the pivot index chosen -- thus we can choose a floor either at the middle point, if it breaks, we know we must go lower -- if it breaks we can then choose a pivot point some where in the middle of the lower half of the building's floors and further split and search recursively from there.

   e.g. if a building has a hundre floors, we choose fifty, throw an egg, it breaks, we know that 1-49 is the only possible valid choices so we try at 25, egg breaks, split again, eventually we get down to say 7 and it is succesful (i.e. we know that the target floor is now higher) so we then split the other way, etc, etc, etc until we have the highest floor where it doesnt break..
        ## O(Log n) [not O(n Log n)]
     ref code from assignment this week:
     def binary_search(arr, target):
    if len(arr) == 0:
    return -1 # array empty
    low = 0
       high = len(arr)-1
     while low <= high:
        mid = low + (high - low)//2
        print(f"target = {target}")
        print(f"low={low} high ={high} mid = {mid} arr[mid] = {arr[mid]}")
        if arr[mid] == target:
          return mid

        # If x is greater, ignore left half
        elif arr[mid] < target:
        low = mid + 1

        # If x is smaller, ignore right half
         else:
         high = mid - 1

    return -1 # not found

