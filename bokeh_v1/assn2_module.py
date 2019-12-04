import pandas as pd
import numpy as np

roll_set_dict = {'17d070060': 0, '16d070049': 0, '17d070051': 0, '183074022': 0, '16d070058': 0, '15d070004': 1, '16d070026': 1, '193076001': 1, 'rk': 1, '194076011': 1, '16d070024': 2, '15d070008': 2, '15d070051': 2, '16d070016': 2, '173074016': 2, 'yogesh': 3, '183074002': 3, '193071001': 3, '15d070016': 3, '170070049': 3, '16d070023': 4, '193070021': 4, '193074008': 4, '183070028': 4, '16d070028': 4, '19v972009': 5, '17d070054': 5, '183074009': 5, '163079019': 5, '194178002': 5, '16d070053': 6, '18i170013': 6, '173074017': 6, '17d070039': 6, '170070048': 6, '17d070061': 7, '16d070062': 7, 'karan': 7, '16d070061': 7, '170070041': 7, '15d070032': 8, '160070049': 8, '16d070030': 8, '16d070059': 8, '17d070058': 8, '194366003': 8, 'naren': 8}


set_list = {0:[(1,800),(2,500),(0.5,100)],
            1:[(1,900),(3,400),(0.5,200)],
            2:[(1,1000),(2,300),(0.5,500)],
            3:[(1,700),(3,200),(0.7,400)],
            4:[(1,1100),(2,100),(0.7,300)],
            5:[(1,1200),(3,200),(0.5,400)],
            6:[(1,600),(2,300),(0.7,100)],
            7:[(1,1300),(3,400),(0.7,200)],
            8:[(1,1400),(2,500),(0.5,300)],
            }
admin_roll_list = ['naren', 'rk', 'yogesh', 'karan']

def get_problem1_csv(roll):
    n=10000
    set_number = roll_set_dict.get(roll)
    if set_number==None:
        print ('Roll number not in roll set')
    else:
        alpha = set_list.get(set_number)[0][1]
        if alpha==None:
            print ('Set number {set_number} has no data')
        else:
            data = alpha*np.random.weibull(1,n)
            df = pd.DataFrame({'Failure_time':np.around(data,3)})
            df['Sample#'] = df.index + 1
            df=df[['Sample#','Failure_time']]
            csv = df.to_csv(index=False)
            return (csv, 'prob1')

def get_problem2_csv(roll):
    n=50000
    set_number = roll_set_dict.get(roll)
    if set_number==None:
        print ('Roll number not in roll set')
    else:
        beta = set_list.get(set_number)[1][0]
        alpha = set_list.get(set_number)[1][1]
        if alpha==None:
            print ('Set number {set_number} has no data')
        else:
            data = alpha*np.random.weibull(beta,n)
            df = pd.DataFrame({'Failure_time':np.around(data, 3)})
            df['Sample#'] = df.index + 1
            df=df[['Sample#','Failure_time']]
            csv = df.to_csv(index=False)
            return (csv, 'prob2')

def get_problem3_csv(roll):
    n=100
    set_number = roll_set_dict.get(roll)
    if set_number==None:
        print ('Roll number not in roll set')
    else:
        beta = set_list.get(set_number)[2][0]
        alpha = set_list.get(set_number)[2][1]
        if alpha==None:
            print ('Set number {set_number} has no data')
        else:
            data = alpha*np.random.weibull(beta,n)
            df = pd.DataFrame({'Failure_time':np.around(data, 3)})
            df['Sample#'] = df.index + 1
            df=df[['Sample#','Failure_time']]
            csv = df.to_csv(index=False)
            return (csv, 'prob3')

