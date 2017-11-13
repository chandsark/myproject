def welcome_message(name):
#Prints out a personalised welcome message
    return "Welcome to this Python script, " + name + "!"

def print_snakes(numsnakes):
    how_many_snakes = numsnakes
    snake_string = """
    Welcome to Python3!
    
                 ____
                / . .\\
                \  ---<
                 \  /
       __________/ /
    -=:___________/

    <3, Philip and Charlie
    """
    print(snake_string * how_many_snakes)

#Call the welcome message function with the input "Udacity Student" 
#and print the output
print(welcome_message("Udacity Student"))
print_snakes(2)