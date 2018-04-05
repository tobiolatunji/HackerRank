
# Quartiles
# Given an array, , of  integers, calculate the respective first quartile (), 
# second quartile (), and third quartile (). It is guaranteed that , , and  are integers.





# Standard Deviation
# Given an array, , of  integers, calculate and print the standard deviation. 
# Your answer should be in decimal form, rounded to a scale of  decimal place 
# (i.e.,  format). An error margin of  will be tolerated for the standard deviation.

def stanDev(N, X):
    mean = findMean(N, X)
    numerator = sum(map(lambda x: (x-mean)**2, X))
    result = round((numerator/N)**0.5, 1)
    return result

def findMean(n, X):
    mean = sum(X)/n
    return mean
    
if __name__ == "__main__":
    N = int(input().strip())
    X = list(map(int, input().strip().split()))
    result = stanDev(N, X)
    print (result)




# Weighted Means
# Given an array, , of  integers and an array, , representing the respective 
# weights of 's elements, calculate and print the weighted mean of 's elements. 
# Your answer should be rounded to a scale of  decimal place (i.e.,  format).    


def weightedMean(N, X, W):
    numerator = sum(map(lambda x, y: x*y, X, W))
    denom = sum(W)
    result = round(numerator/denom, 1)
    return result

if __name__ == "__main__":
    N = int(input().strip())
    X = list(map(int, input().strip().split()))
    W = list(map(int, input().strip().split()))
    result = weightedMean(N, X, W)
    print (result)






# mean, media, mode
# Given an array, , of  integers, calculate and print the respective mean, median, 
# and mode on separate lines. If your array contains more than one modal value, 
# choose the numerically smallest one.

def mean_median_mode(n, X):
    mean = findMean(n, X)
    median = findMedian(n, X)
    mode = findMode(X)
    return mean, median, mode
  
def findMean(n, X):
    mean = round(sum(X)/n,1)
    return mean

def findMedian(n,X):
    X = sorted(X)
    if n%2==0:
        median = (X[n//2] + X[(n//2)-1])/2
        return median
    else:
        median = X[n//2]
        return median
    
def findMode(X):
    count_dict = {}
    X = sorted(X)
    max_count = 1
    mode = X[0]
    for i in X:
        if i in count_dict:
            count_dict[i]+=1
            if count_dict[i] > max_count:
                max_count = count_dict[i]
                mode = i
        else:
            count_dict[i] = 1
    return mode
    

    
if __name__ == "__main__":
    n = int(input())
    X = list(map(int, input().strip().split(' ')))
    mean, median, mode = mean_median_mode(n, X)
    print('{}\n{}\n{}'.format(mean,median,mode))



# Array left rotation

# A left rotation operation on an array of size  shifts each of the 
# array's elements  unit to the left. For example, if left rotations are performed 
# on array , then the array would become .

# Given an array of  integers and a number, , perform  left rotations 
# on the array. Then print the updated array as a single line of 
# space-separated integers.

def array_left_rotation(a, n, k):
    new_a = a[:]
    for i in range(n):
        new_a[i - k] = a[i]
    return new_a
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')



# Digit Sum Recur

# Given an integer, we need to find the super digit of the integer.
# We define super digit of an integer  using the following rules:
# If  has only  digit, then its super digit is .
# Otherwise, the super digit of  is equal to the super digit of the digit-sum of . 
# Here, digit-sum of a number is defined as the sum of its digits.
# For example, super digit of  will be calculated as:
"""
super_digit(9875) = super_digit(9+8+7+5) 
                  = super_digit(29) 
                  = super_digit(2+9)
                  = super_digit(11)
                  = super_digit(1+1)
                  = super_digit(2)
                  = 2.
"""
# You are given two numbers  and . You have to calculate the super digit of .
# is created when number  is concatenated  times. That is, if  and , then .


#!/bin/python3

import sys

def digitSum(n, k):
    # Complete this function
    p = int(n) * k
    return digitSumRecur(p)

def digitSumRecur(p):
    if len(str(p))==1:
        return p
    else:
        p = list(str(p))
        p = sum([*map(int, p)])
        return digitSumRecur(p)
            

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = digitSum(n, k)
    print(result)





# math

#Consider two points,  and . We consider the inversion or point reflection, , 
#of point  across point  to be a  rotation of point  around .

#Given  sets of points  and , find  for each pair of points and print two 
# space-separated integers denoting the respective values of  and  on a new line.

#!/bin/python3

import os
import sys

#
# Complete the findPoint function below.
#
def findPoint(px, py, qx, qy):
    x = qx - px
    y = qy - py
    rx = qx + (qx - px)
    ry = qy + (qy - py)
    return rx, ry


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    for n_itr in range(n):
        pxPyQxQy = input().split()

        px = int(pxPyQxQy[0])

        py = int(pxPyQxQy[1])

        qx = int(pxPyQxQy[2])

        qy = int(pxPyQxQy[3])

        result = findPoint(px, py, qx, qy)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
    


    

# SQL

# Advanced Joins

# Q1
# You are given a table, Projects, containing three columns: Task_ID, Start_Date and 
# End_Date. It is guaranteed that the difference between the End_Date and the Start_Date 
# is equal to 1 day for each row in the table.
# If the End_Date of the tasks are consecutive, then they are part of the same project. 
# Samantha is interested in finding the total number of different projects completed.

# Write a query to output the start and end dates of projects listed by the number 
# of days it took to complete the project in ascending order. If there is more than 
# one project that have the same number of completion days, then order by the 
# start date of the project.

# WITH t AS (SELECT End_Date d, ROW_NUMBER() OVER(ORDER BY End_Date) i 
# FROM Projects GROUP BY End_Date) SELECT MIN(d),MAX(d) 
# FROM t GROUP BY DATEDIFF(day,i,d);

select sday, eday from 
(select min(s) sday, max(d) eday from 
(SELECT min(Start_Date) s, End_Date d, ROW_NUMBER() OVER(ORDER BY End_Date) i from 
Projects GROUP BY End_Date) 
as subquery 
GROUP BY DATEDIFF(day,i,d)) 
as subquery2 
order by datediff(day,sday,eday), sday;


# Q2
# You are given three tables: Students, Friends and Packages. 
# Students contains two columns: ID and Name. Friends contains two columns: ID and 
# Friend_ID (ID of the ONLY best friend). Packages contains two columns: ID and Salary 
# (offered salary in $ thousands per month).

# Write a query to output the names of those students whose best friends got offered 
# a higher salary than them. Names must be ordered by the salary amount offered to 
# the best friends. It is guaranteed that no two students got same salary offer.

select s.name from 
students s 
left join packages p on s.id = p.id 
inner join friends f on s.id = f.id 
left join packages p2 on f.friend_id = p2.id 
where p.salary < p2.salary 
order by p2.salary ;  


# Q3
# You are given a table, Functions, containing two columns: X and Y.
# Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.
# Write a query to output all such symmetric pairs in ascending order by the value of X.

with 
t as (select *, row_number() over(order by x) id from functions), 
t3 as (select t.x, t.y from t cross join t t2 
where t.id <> t2.id and t.x = t2.y and t.y=t2.x), 
t4 as (select *, row_number() over(order by x) id from t3) 
select x,y from t4 where id <= (select max(id)/2 from t4);