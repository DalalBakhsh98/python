# [Exhaustive Method]: This solution should implement an algorithm that
#                      tries every possible combination of processes that can fit within the timeline then finds
#                      the combination that results in the maximum value.

# Each processor has an [id, duration, and value] that will be inputed and time limit

import time

input_Array = input("Enter Processes P:")
#split_input = input_Array.split(' ')
tuples = eval(input_Array)
input_T = input("Enter the time limit T:")
N = eval(input_T)
#hird_elements = [t[2] for t in tuples] # the tuble start from 0 so the third element of the set is 2
#print("The third elements are:", third_elements)


# this the function that will do our calculation
def Running_time(func):
    def wrap_func(*args, **kwargs):
        time_1 = time.time()
        result = func(*args, **kwargs)
        time_2 = time.time()
        msec =  (time_2 - time_1) * 1000
        print(f"The running time of {func.__name__} took {msec:f} ms.")
        return result
    return wrap_func

@Running_time
def Exhaustive_processes(processors, time_limit):
    """
    Tries every possible combination of processors that can fit within the time limit
    then finds the combination that results in the maximum value.
    Parameters:
    processors (list of tuples): List of processors, each represented as a tuple (id, duration, value).
    time_limit (int): Total time available for scheduling the processors.
    Returns:
    tuple: A tuple containing the selected processors and their total value.
    """
    max_value = 0
    selected_processors = []   # creating an empty list 

    # Try every possible combination of subsets
    for i in range(1, 2**len(processors)):
        subset = [processors[j] for j in range(len(processors)) if (i & (1<<j))]

        # Check if the subset can fit within the time limit
        total_duration = sum(p[1] for p in subset)
        if total_duration <= time_limit:
            # Compute the total value of the subset
            total_value = sum(p[2] for p in subset)
            # Update the selected processors and maximum value if necessary
            if total_value > max_value:
                max_value = total_value
                selected_processors = subset

    return selected_processors#, max_value





#p = [(1,3,21), (2,6,24), (3,2,12), (4,4,20)]
# print(schedule_processes(p,8))

print(' ')
print('Solution1:')
op_p = Exhaustive_processes(tuples,N)
print('Selected processes:',[i[0] for i in op_p])
print('total value is',sum(op_p[2] for op_p in op_p))
print('total duration is',sum(op_p[1] for op_p in op_p))
RT = Running_time(Exhaustive_processes)
#print(RT)



