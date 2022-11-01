#Gentry Atkinson

from random import choice

if __name__ == '__main__':
    play_list = ['rock']

    print('### Game of Rock ###')
    
    print('Choose your move: ', end='')
    p = input().strip()
    while p != 'quit':
        c = choice(play_list)
        if p not in play_list:
            play_list.append(p)
        pi = play_list.index(p)
        ci = play_list.index(c)

        print(f'Computer plays: {c}')

        if(pi == ci):
            print('Draw')
        elif abs(pi-ci) < abs(ci - (len(play_list) - pi)) :
            print(f'{p} beats {c}')
        else:
            print(f'{c} beats {p}')
        
        print('Choose your move: ', end='')
        p = input().strip()
    
    print('### Game of ', ', '.join(play_list), ' ###')