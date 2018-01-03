# author
sol_g=0
num_sols=0
is_sol_g=False #I only want to know if there is or there isn't solution, so I decided to leave is_sol as a global var 
               # and in the case we find one the algorithm stops looking for others

def backTracking(position, data_set, total_sum):
    global sol_g
    global num_sols
    global is_sol_g
    #With not is_sol in the moment he found a sol with a value
    while position < len(data_set) and not is_sol_g:
        total_sum= total_sum + data_set[position]
        if(total_sum == sol_g):
            is_sol_g=True
            num_sols+=1
            print ("There is a solution")
        else: 
            backTracking(position+1, data_set, total_sum)
        total_sum= total_sum - data_set[position]
        position+=1
        
sol_g = 5
is_sol_g=False
backTracking(0,[1, 4, 3, 1, 4], 0)