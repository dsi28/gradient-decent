# f(x) = x^2 - 4x + 3

def J_fn(x):
    return (x**2) - (4*x) + 3

# J_fun'()
def J_fn_derivative(x):
    return (2*x) - 4


def gradient_descent(J, x, alpha, num_iters):
    """
    Performs Gradient Descent to optimize the cost function J(theta).

    Arguments:
    - J(theta): cost function.ex) J(x) = x2 - 4x + 3
    - x: initial parameter value (scalar)
    alpha -- learning rate (scalar)
    num_iters -- the number of iterations to run Gradient Descent (scalar)

    Returns:
    x_final -- optimized parameter value 
    J_history -- vector of cost function values for each iteration (num_iters x 1)
    """

    """
    steps:
    step 1: set up parameters
    step 2: complete the gradient
    step 3: update the parameters
    step 4: repleat steps 2-3 until convergence
    """

    """
    step 1:
    - choose initial value (x)
    - set history variable
    """
    x_final = x # x_final is x initial
    J_history = []


    
    for i in range(num_iters):
        """
        step 2:
        - compute gradient of J(x) with respect to x
        - to do this plug x into J_fn'() (derivative of J function)
        """
        gradient = J_fn_derivative(x_final)


        """
        step 3 (part 1):
        - update parameters
        - update x_final using gradient decent (weight update rule formula):
        x_new = x_old - learning_rate * J_fn'(x_old)
        """
        x_final = x_final - alpha * gradient

        """
        step 3 (part 2):
        - update parameters
        - compute the cost function. cost function formula:
        cost_fn = J_fn(x_new)
        - update j_history
        """
        cost_fn = J_fn(x_final)
        J_history.append(cost_fn)

        """
        step 4:
        - repeat the steps until you reach convergence. 
        - in this case convergence depends on number of iterations
        number of steps, num_iters variable
        """

    return x_final, J_history