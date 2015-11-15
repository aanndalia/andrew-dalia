import time

def get_subsets(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [[], arr]
    
    prev_subs = get_subsets(arr[0:-1])
    last = arr[-1]
    new_subs = []
    for psub in prev_subs:
        new_subs.append(psub + [last])
        
    return prev_subs + new_subs

def get_subsets2(arr, d):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [[], arr]
    
    arr_t = tuple(arr)
    if arr_t in d:
        prev_subs = d[arr_t]
    else:    
        prev_subs = get_subsets(arr[0:-1])
        
    last = arr[-1]
    new_subs = []
    for psub in prev_subs:
        new_subs.append(psub + [last])
    
    all_subs = prev_subs + new_subs
    if arr_t not in d:
        d[arr_t] = all_subs
        
    return all_subs
    
def main():
    arr = [1,2,3,4,5,6,7]
    
    time1 = time.time()
    subsets = get_subsets(arr)
    print subsets
    print len(subsets)
    print "time", (time.time() - time1)
    
    time2 = time.time()
    subsets2 = get_subsets2(arr, {})
    print subsets2
    print len(subsets2)
    print "time dp", (time.time() - time2)
    
main()
    