
def solution(A, B):
    moves = [(+2, +1), (-2, +1), (-2, -1), (+2, -1)]
    
    answer = [0,0]
    index = 0 

    while not answer[0] == A and not answer[1] == B:
        index = index + 1 

        if index > 100000 or index < -100000:
            break 

        for possible_move in moves:
            answer[0] = answer[0] + possible_move[0]
            answer[0] = answer[1] + possible_move[1]

        if answer[0] == A and answer[1] == B:
            break

solution(4, 5) 