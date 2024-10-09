from numpy import sin, cos, pi
from scipy.integrate import solve_ivp
from sys import argv

g = 9.81
l1 = 1.0
l2 = 1.0
m1 = 1.0
m2 = 1.0

ROUND = 16


def equations(t, y):

    theta1, theta2, omega1, omega2 = y
    delta_theta = theta1 - theta2

    d_omega1 = (-g*(2*m1+m2)*sin(theta1) - m2*g*sin(theta1-2*theta2)
               - 2*sin(delta_theta)*m2*((omega2**2)*l2+(omega1**2)*l1*cos(delta_theta)))/\
               (l1*(2*m1+m2-m2*cos(2*theta1-2*theta2)))

    d_omega2 = (2*sin(delta_theta)*((omega1**2)*l1*(m1+m2)+g*(m1+m2)*cos(theta1)
               +(omega2**2)*l1*cos(delta_theta)))/(l2*(2*m1+m2-m2*cos(2*theta1-2*theta2)))

    return [omega1, omega2, d_omega1, d_omega2]

def eval(theta1_0, theta2_0):

    #theta1_0 = pi / 2
    #theta2_0 = pi / 2
    omega1_0 = 0.0
    omega2_0 = 0.0

    t_span = (0, 10)
    y0 = [theta1_0, theta2_0, omega1_0, omega2_0]

    solution = solve_ivp(equations, t_span, y0, t_eval=[0, 10])

    omega1 = solution.y[0][-1]
    omega2 = solution.y[1][-1]
    #d_omega1 = solution.y[2]
    #d_omega2 = solution.y[3]
    #t = solution.t

    return omega1 + omega2


def dphfsum(string, debug=False):

    sum1 = sum([ord(c) for c in string[0:int(len(string)/2)]])
    sum2 = sum([ord(c) for c in string[int(len(string)/2):]])

    evl = eval(sum1, sum2)*33
    evl2 = int(round((evl - int(evl)), ROUND)*10**ROUND)

    if debug:
        print("######################")
        print(f"Original string: {string}")
        print(f"Sums: {sum1} and {sum2}")
        print(f"Evaluates to: {evl}")
        print(f"And becomes: {evl2}")
        print(f"Length: {len(str(evl2))}")

    while len(str(evl2)) < ROUND:
        evl2 *= 10

    return evl2


if __name__ == "__main__":

    try:
        string = argv[1]
    except IndexError:
        string = "Test string"

    print(dphfsum(string))
