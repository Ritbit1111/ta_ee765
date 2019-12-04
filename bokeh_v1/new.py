import pandas as pd
import numpy as np
df = pd.read_csv('new_list.csv')
roll = np.array(df['Roll No'])
saved_roll_list = roll
dict = {}
duplicate = 0
for i,r in enumerate(roll):
    if dict.get(r):
        duplicate += 1
        print (f'Duplicate at {i}')
    else :
        dict.update({r:i})
# print (roll)
set_list=[]
while len(roll)>7:
    new_set = np.random.choice(roll, 5, replace=False)
    roll = np.setdiff1d(roll, new_set)
    set_list.append(list(new_set))
set_list.append(list(roll))
print (set_list)
# print (saved_roll_list)

student_dict = {}
for index,set_ in enumerate(set_list):
    [student_dict.update({r:index}) for r in set_]
print (student_dict)


[['17D070060', '16D070049', '17D070051', '183074022', '16d070058'], ['15D070004', '16D070026', '193076001', 'rk', '194076011'], ['16D070024', '15D070008', '15D070051', '16D070016', '173074016'], ['yogesh', '183074002', '193071001', '15D070016', '170070049'], ['16D070023', '193070021', '193074008', '183070028', '16D070028'], ['19V972009', '17D070054', '183074009', '163079019', '194178002'], ['16D070053', '18I170013', '173074017', '17D070039', '170070048'], ['17D070061', '16D070062', 'karan', '16d070061', '170070041'], ['15D070032', '160070049', '16D070030', '16D070059', '17D070058', '194366003', 'naren']]
{'17D070060': 0, '16D070049': 0, '17D070051': 0, '183074022': 0, '16d070058': 0, '15D070004': 1, '16D070026': 1, '193076001': 1, 'rk': 1, '194076011': 1, '16D070024': 2, '15D070008': 2, '15D070051': 2, '16D070016': 2, '173074016': 2, 'yogesh': 3, '183074002': 3, '193071001': 3, '15D070016': 3, '170070049': 3, '16D070023': 4, '193070021': 4, '193074008': 4, '183070028': 4, '16D070028': 4, '19V972009': 5, '17D070054': 5, '183074009': 5, '163079019': 5, '194178002': 5, '16D070053': 6, '18I170013': 6, '173074017': 6, '17D070039': 6, '170070048': 6, '17D070061': 7, '16D070062': 7, 'karan': 7, '16d070061': 7, '170070041': 7, '15D070032': 8, '160070049': 8, '16D070030': 8, '16D070059': 8, '17D070058': 8, '194366003': 8, 'naren': 8}
