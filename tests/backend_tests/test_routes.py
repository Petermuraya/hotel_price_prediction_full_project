def solution(A):
    steps = 0
    for i in range(len(A)):
        mod = i % 4
        desired = None
        if mod == 0:
            desired = 'positive'
        elif mod in (1, 3):
            desired = 'zero'
        else:  # mod == 2
            desired = 'negative'
        
        current = A[i]
        
        if desired == 'positive':
            if current == 0:
                return -1
            elif current < 0:
                steps += 1
        elif desired == 'zero':
            if current != 0:
                steps += 1
        elif desired == 'negative':
            if current == 0:
                return -1
            elif current > 0:
                steps += 1
    return steps