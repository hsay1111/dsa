

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def first_position(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(cards) - 1, condition)

def last_position(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid < len(cards)-1 and cards[mid+1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'right'
        else:
            return 'left'
    return binary_search(0, len(cards) - 1, condition) 

def first_and_last_position(cards, query):
    return first_position(cards, query), last_position(cards, query)

print(first_and_last_position([5,7,7,8,8,10], 8))
