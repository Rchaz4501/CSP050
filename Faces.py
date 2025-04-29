def convert(input_value):
    input_value = input_value.replace(":)", "\U0001f600")
    input_value = input_value.replace(":(", "\U0001F641")
    return input_value

def main():
    greeting = input("Hey Whatsup! ")
    greeting = convert(greeting)
    print(greeting)
    
main()


    
 


    
        
