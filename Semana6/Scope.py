def my_function(): 
    inside_variable =  "Inside funcion"
    print(inside_variable)
    my_function()



    #2, Try to access and change a global variable from withim a function 
    global_variable = 10

    def modify_global():
        global global_variable
        global_variable = 20 
        print("Inside function, global_variable=", global_variable)


        modify_global()
        print("Outside function, global_variable =", global_variable)
        

