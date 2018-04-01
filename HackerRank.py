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

