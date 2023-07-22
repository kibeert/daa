import time 

start_time = time.time()
def quadratic_function(a, b, c, x):
    return a * x * 2 + b * x + c

def bisection_method(a, b, c, left, right, tolerance=1e-6, max_iterations=1000):
    if quadratic_function(a, b, c, left) * quadratic_function(a, b, c, right) >= 0:
        print("The roots are not bracketed in the given interval.")
        return None

    for iteration in range(max_iterations):
        midpoint = (left + right) / 2
        f_midpoint = quadratic_function(a, b, c, midpoint)

        if abs(f_midpoint) < tolerance:
            return midpoint

        if quadratic_function(a, b, c, left) * f_midpoint < 0:
            right = midpoint
        else:
            left = midpoint

        if right - left < tolerance:
            # The interval is sufficiently small, so return the midpoint as an approximate root
            return midpoint

    print("Bisection method reached the maximum number of iterations.")
    return None


a = 1
b = -3
c = 2

left_endpoint = -10
right_endpoint = 10

root = bisection_method(a, b, c, left_endpoint, right_endpoint)

if root is not None:
    print(f"The root of the quadratic equation is approximately: {root}")
else:
    print("No root found within the given interval.")
end_time= time.time()
elapsed_time = end_time-start_time
print("elapsed time:{}seconds").format(elapsed_time)