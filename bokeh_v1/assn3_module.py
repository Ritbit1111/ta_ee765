import pandas as pd
import numpy as np

roll_set_dict = {'17d070060': 0, '16d070049': 0, '17d070051': 0, '183074022': 0, '16d070058': 0, '15d070004': 1, '16d070026': 1, '193076001': 1, 'rk': 1, '194076011': 1, '16d070024': 2, '15d070008': 2, '15d070051': 2, '16d070016': 2, '173074016': 2, 'yogesh': 3, '183074002': 3, '193071001': 3, '15d070016': 3, '170070049': 3, '16d070023': 4, '193070021': 4, '193074008': 4, '183070028': 4, '16d070028': 4, '19v972009': 5, '17d070054': 5, '183074009': 5, '163079019': 5, '194178002': 5, '16d070053': 6, '18i170013': 6, '173074017': 6, '17d070039': 6, '170070048': 6, '17d070061': 7, '16d070062': 7, 'karan': 7, '16d070061': 7, '170070041': 7, '15d070032': 8, '160070049': 8, '16d070030': 8, '16d070059': 8, '17d070058': 8, '194366003': 8, 'naren': 8, 'om':8}


set_list = {0:[(0.5,10),(4,500),(0.4,200), (0.8,10e-8)],
            1:[(0.7,10),(3,600),(0.4,400), (0.8,2*10e-8)],
            2:[(0.5,20),(2,700),(0.4,300), (0.8,3*10e-8)],
            3:[(0.7,20),(4,800),(0.6,500), (0.7,10e-7)],
            4:[(0.5,30),(3,500),(0.6,100), (0.7,2*10e-7)],
            5:[(0.7,30),(3,600),(0.6,100), (0.7,3*10e-7)],
            6:[(0.5,10),(4,700),(0.8,200), (0.6,10e-6)],
            7:[(0.7,20),(3,800),(0.8,300), (0.6,2*10e-6)],
            8:[(0.5,30),(2,800),(0.8,400), (0.6,3*10e-6)],
            }
admin_roll_list = ['naren', 'rk', 'yogesh', 'karan']

def get_problem1_csv(roll):
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
            df['Sample'] = df.index + 1
            df=df[['Sample','Failure_time']]
            csv = df.to_csv(index=False)
            return (csv, 'prob1')

def get_problem2_csv(roll):
    nl=100
    nh=900
    set_number = roll_set_dict.get(roll)
    if set_number==None:
        print ('Roll number not in roll set')
    else:
        beta_l = set_list.get(set_number)[0][0]
        beta_h = set_list.get(set_number)[1][0]
        alpha_l = set_list.get(set_number)[0][1]
        alpha_h = set_list.get(set_number)[1][1]
        if alpha_l==None:
            print ('Set number {set_number} has no data')
        else:
            ntotal = 0
            while(ntotal!=nl+nh):
                data_l = alpha_l*np.random.weibull(beta_l,nl)
                data_h = alpha_h*np.random.weibull(beta_h,nh)
                data_merged = np.concatenate((data_l, data_h))
                data_merged = np.around(data_merged, 3)
                ntotal = len(data_merged)
            np.random.shuffle(data_merged)
            df = pd.DataFrame({'Failure_time':data_merged})
            df['Sample'] = df.index + 1
            df=df[['Sample','Failure_time']]
            csv = df.to_csv(index=False)
            return (csv, 'prob2')

def get_alpha(E, A, T):
    alpha = A * np.exp(E*1.6e-19/(1.38e-23*(T+273)))
    return alpha

def get_problem3_csv(roll):
    n=100
    set_number = roll_set_dict.get(roll)
    if set_number==None:
        print ('Roll number not in roll set')
    else:
        beta = 2
        alpha_80 = get_alpha(set_list.get(set_number)[3][0], set_list.get(set_number)[3][1], 80)
        alpha_100 = get_alpha(set_list.get(set_number)[3][0], set_list.get(set_number)[3][1], 100)
        alpha_120 = get_alpha(set_list.get(set_number)[3][0], set_list.get(set_number)[3][1], 120)
        if alpha_80==None:
            print ('Set number {set_number} has no data')
        else:
            data_80 = alpha_80*np.random.weibull(beta,n)
            data_100 = alpha_100*np.random.weibull(beta,n)
            data_120 = alpha_120*np.random.weibull(beta,n)
            df = pd.DataFrame({'Failure_time_T=80':np.around(data_80, 3),'Failure_time_T=100':np.around(data_100, 3),'Failure_time_T=120':np.around(data_120, 3) })
            df['Sample'] = df.index + 1
            df=df[['Sample', 'Failure_time_T=80', 'Failure_time_T=100', 'Failure_time_T=120']]
            csv = df.to_csv(index=False)
            return (csv, 'prob3')

