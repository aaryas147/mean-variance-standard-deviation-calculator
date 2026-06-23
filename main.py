import numpy as np
def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    new_list = np.array(lst).reshape(3, 3)
    return {
        'mean':[np.mean(new_list,axis=0).tolist(),np.mean(new_list,axis=1).tolist(),np.mean(new_list).tolist()],
        'variance': [np.var(new_list,axis=0).tolist(),np.var(new_list,axis=1).tolist(),np.var(new_list).tolist()],
        'standard deviation': [np.std(new_list,axis=0).tolist(),np.std(new_list,axis=1).tolist(),np.std(new_list).tolist()]
    }
result=calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (result)