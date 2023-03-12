from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# create an array of values
values = [rank] * 10

# compute the sum of all values across all processes
global_sum = comm.allreduce(sum(values), op=MPI.SUM)

# print the result from process 0
if rank == 0:
    print("The sum is:", global_sum)
