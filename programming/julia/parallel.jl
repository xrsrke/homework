# function thread_test()
#     Threads.@threads for i in 1:6
#         id = Threads.threadid()
#         println("Thread ID: ", id, " | i: ", i)
#     end
# end

# thread_test()

function serialsum(xs)
    r = 0
    for i in xs
        r += i
    end
    return r
end

function threadsum(xs)
    r = zeros(Threads.nthreads())
    Threads.@threads for i in xs
        # Each thread has it's own "sum bucket" to accumulate
        # bits and pieces of xs -- we'll add these buckets together
        # at the end.
        r[Threads.threadid()] += i
    end
    return sum(r)
end

# values = randn(100_000_000);

# using BenchmarkTools
# @time serialsum(values)

# @time threadsum(values)
# @time randn(100_000_000_0)

# Threads.@threads for i in 1:1000
#     xs = []
#     push!(xs, i) # Add i to the end of xs
# end

# println(length(xs))

# xs = []

# xslock = Threads.ReentrantLock()
# Threads.@threads for i in 1:1000
#     lock(xslock) do
#         push!(xs, i)
#     end
# end

# print(length(xs))

for i in 1:5
    println(i)
end

# Make the loop run in multi-thread

Threads.@threads for i in 1:5
    println(i)
end