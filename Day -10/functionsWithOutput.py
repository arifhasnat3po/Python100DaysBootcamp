# def format_name():
#   f_name = input("what is your first name? : ").capitalize()
#   l_name = input("what is your last name? : ").capitalize()
#   print(f_name +" "+ l_name) 

# format_name()

# def format_name(f_name , l_name):
#   print(f_name.title())
#   print(l_name.title())

# format_name("arif","aRiF")

def format_name(f_name, l_name):
      """Take a firstname and lastname and format it to return the title case version of the name"""
      if f_name =="" or l_name=="":
            return "You didn't provide a valid name."
          
      formatted_f_name = f_name.title()
      formatted_l_name = l_name.title()
      return f"Result: {formatted_f_name} {formatted_l_name}"
    

  
  
  
print(format_name(input("What is your first name? "),input("What is your last name? ")))

# format_name()


  