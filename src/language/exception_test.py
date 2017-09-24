'''
Created on Sep 24, 2017

@author: andy
'''
d = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

def test():
    while True:
        try:
            i = int(input('Num of the day: '))
        except ValueError:
            print('Not a number of day!')
        else:
            print(d.get(i, 'No such 1day!'))
    

if __name__ == '__main__':
    test()