import pandas as pd
import numpy as np

group_dict = {1:{'proj_num':1 ,'A':1e-8, 'Ea':0.7, 'n_RH':-0.5, 'beta':2, 'beta_mechanism_change':10, 'Rm':100, 'Tm':65, 'Ri':75, 'Ti':40},
              2:{'proj_num':3, 'A':1e-10, 'Ea':0.85, 'n_RH':-1, 'beta':2, 'beta_mechanism_change':11, 'Rm':35, 'Tm':65, 'Ri':15, 'Ti':40},
              3:{'proj_num':2, 'A':7e-8, 'Ea':0.75, 'n_RH':-1.25, 'beta':3, 'beta_mechanism_change':12, 'Rm':120, 'Tm':75, 'Ri':75, 'Ti':40},
              4:{'proj_num':2, 'A':7e-8, 'Ea':0.75, 'n_RH':-1.25, 'beta':2, 'beta_mechanism_change':10, 'Rm':120, 'Tm':80, 'Ri':75, 'Ti':40},
              5:{'proj_num':2, 'A':1.2e-8, 'Ea':0.7, 'n_RH':-0.5, 'beta':2, 'beta_mechanism_change':9, 'Rm':120, 'Tm':70, 'Ri':75, 'Ti':40},
              6:{'proj_num':2, 'A':1.2e-8, 'Ea':0.7, 'n_RH':-0.5, 'beta':3, 'beta_mechanism_change':11, 'Rm':120, 'Tm':75, 'Ri':75, 'Ti':40},
              7:{'proj_num':2, 'A':3e-9, 'Ea':0.9, 'n_RH':-1.75, 'beta':3, 'beta_mechanism_change':10, 'Rm':120, 'Tm':65, 'Ri':75, 'Ti':40},
              8:{'proj_num':3, 'A':1e-10, 'Ea':0.85, 'n_RH':-1, 'beta':3, 'beta_mechanism_change':10, 'Rm':35, 'Tm':70, 'Ri':15, 'Ti':40},
              9:{'proj_num':2, 'A':3e-9, 'Ea':0.9, 'n_RH':-1.75, 'beta':2, 'beta_mechanism_change':12, 'Rm':120, 'Tm':65, 'Ri':75, 'Ti':40},
              10:{'proj_num':3, 'A':7e-9, 'Ea':0.75, 'n_RH':-1.25, 'beta':3, 'beta_mechanism_change':12, 'Rm':30, 'Tm':75, 'Ri':15, 'Ti':40},
              11:{'proj_num':1, 'A':1e-9, 'Ea':0.8, 'n_RH':-0.75, 'beta':3, 'beta_mechanism_change':12, 'Rm':100, 'Tm':75, 'Ri':75, 'Ti':40},
              12:{'proj_num':1, 'A':5e-11, 'Ea':0.9, 'n_RH':-0.9, 'beta':2, 'beta_mechanism_change':8, 'Rm':100, 'Tm':70, 'Ri':75, 'Ti':40},
              13:{'proj_num':1, 'A':3e-8, 'Ea':0.8, 'n_RH':-1.5, 'beta':2.5, 'beta_mechanism_change':10, 'Rm':100, 'Tm':70, 'Ri':75, 'Ti':40},
              14:{'proj_num':2, 'A':6e-11, 'Ea':0.9, 'n_RH':-0.9, 'beta':2, 'beta_mechanism_change':11, 'Rm':120, 'Tm':65, 'Ri':75, 'Ti':40},
              15:{'proj_num':2, 'A':6e-11, 'Ea':0.9, 'n_RH':-0.9, 'beta':3, 'beta_mechanism_change':9, 'Rm':105, 'Tm':80, 'Ri':75, 'Ti':40},
              16:{'proj_num':3, 'A':7e-9, 'Ea':0.75, 'n_RH':-1.25, 'beta':2, 'beta_mechanism_change':10, 'Rm':30, 'Tm':80, 'Ri':15, 'Ti':40},
              17:{'proj_num':3, 'A':1.5e-10, 'Ea':0.9, 'n_RH':-1.75, 'beta':2, 'beta_mechanism_change':10, 'Rm':30, 'Tm':65, 'Ri':15, 'Ti':40},
              18:{'proj_num':3, 'A':1.5e-10, 'Ea':0.9, 'n_RH':-1.75, 'beta':3, 'beta_mechanism_change':12, 'Rm':30, 'Tm':75, 'Ri':15, 'Ti':40},
              19:{'proj_num':2, 'A':5e-10, 'Ea':0.85, 'n_RH':-1, 'beta':2, 'beta_mechanism_change':11, 'Rm':125, 'Tm':65, 'Ri':75, 'Ti':40},
              20:{'proj_num':2, 'A':5e-10, 'Ea':0.85, 'n_RH':-1, 'beta':3, 'beta_mechanism_change':10, 'Rm':110, 'Tm':75, 'Ri':75, 'Ti':40},
              21:{'proj_num':1, 'A':2e-9, 'Ea':0.9, 'n_RH':-1.75, 'beta':2, 'beta_mechanism_change':10, 'Rm':100, 'Tm':65, 'Ri':75, 'Ti':40},
              22:{'proj_num':1, 'A':2e-10, 'Ea':1, 'n_RH':-2, 'beta':2.5, 'beta_mechanism_change':8, 'Rm':100, 'Tm':75, 'Ri':75, 'Ti':40},
              23:{'proj_num':2, 'A':5e-10, 'Ea':0.85, 'n_RH':-1, 'beta':2.5, 'beta_mechanism_change':9, 'Rm':115, 'Tm':70, 'Ri':75, 'Ti':40},
              24:{'proj_num':1, 'A':5e-8, 'Ea':0.75, 'n_RH':-1.25, 'beta':3, 'beta_mechanism_change':12, 'Rm':100, 'Tm':70, 'Ri':75, 'Ti':40},
        }

proj_dict  = {1:[1, 11, 12, 13, 21, 22, 24], 2:[3, 4, 5, 6, 7, 9, 14, 15, 19, 20, 23], 3:[2, 8, 10, 16, 17, 18]}

N_total = 500
D_total = 1000
N_latent_per = 10 # This in "percent"
beta_latent = 0.5

def get_RH(x, Ri, Rm, Tm, Ti):
    ''' I/p Param : Temperature , O/P : RH (Boundary case) '''
    slope_ = (Ri - Rm)/(Tm - Ti)
    intercept_ = (Rm*Tm - Ri*Ti)/(Tm - Ti)
    return np.where(x<Ti, Rm, np.where(x<Tm, slope_*x + intercept_, 0))

def get_beta(T, RH, beta, beta_mechanism_change, Ri, Rm, Tm, Ti):
    RH_boundary = get_RH(T, Ri, Rm, Tm, Ti)
    return beta if RH<RH_boundary else beta_mechanism_change



def get_data(grp_no, result):
    param = group_dict.get(grp_no)
    if param==None:
        df= pd.DataFrame()
        return df.to_csv(index=False)

    proj_num = param.get('proj_num')
    A = param.get('A')
    Ea = param.get('Ea')
    n_RH = param.get('n_RH')
    beta = param.get('beta')
    Ri = param.get('Ri')
    Rm = param.get('Rm')
    Ti = param.get('Ti')
    Tm = param.get('Tm')
    beta_mechanism_change = param.get('beta_mechanism_change')

    df= pd.DataFrame()
    df['Dummy']=pd.Series(np.zeros(N_total))
    count=1
    for e in result:
        T = e[2]
        Rh = e[3]
        N = e[0]
        D = e[1]

        alpha = A * (Rh)**n_RH * np.exp(Ea * 1.6e-19 /(1.38e-23*(T+273)))
        alpha_latent = alpha/20

        beta_healthy = get_beta(T, Rh, beta, beta_mechanism_change, Ri, Rm, Tm, Ti)

        N_latent = int(N * N_latent_per/100)
        N_healthy = N-N_latent

        data_healthy = alpha * np.random.weibull(beta_healthy, N_healthy)
        data_latent = alpha_latent * np.random.weibull(beta_latent, N_latent)

        data_healthy = data_healthy[data_healthy<D]
        data_latent = data_latent[data_latent<D]

        data = np.append(data_healthy, data_latent)
        np.random.shuffle(data)

        if proj_num==1:
            df[f'{count}:T={e[2]},RH={e[3]}']=pd.Series(np.around(data, 2))
        if proj_num==2:
            df[f'{count}:T={e[2]},V={e[3]}']=pd.Series(np.around(data, 2))
        if proj_num==3:
            df[f'{count}:T={e[2]},V={e[3]}']=pd.Series(np.around(data, 2))
        count+=1
    del df['Dummy']
    csv = df.to_csv(index=False)
    return (csv)
