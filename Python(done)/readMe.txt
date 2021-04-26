1. after installing the python3 you can make alias in .bash_profile: 

        alias python=python3

2. we can run python file in the repel: 

        python3 filename.py

[ATTENTION]
3. Everything in python consider an object, and an object has functions and properties

4. There are two types of number in python, integer and float

5. We can check the type of object in python by using type function: 

        type(5)

6. // is the integer division

7. scape character in python is \

8. We can get single character in python by using array notation:

        greet = 'hello'
        greet[0]

9. we can use 
    greet[0:3]

10. we can use string functions: 

    newGreet = greet.upper()
    newListGreet = greet.split(",")

11. list is just like arrays in other languages, tuples are the immutable of list, and we use () instead of []
        , set are just like list but onordered and without duplicate, we use {} for set:

    we can get certain elements:

        fibi[0:4]

12. by using + operator we can cancat two list

13. we can add to the end of list by using append() function:

        fib.append(5)

14. we can remove with pop() function:

        fib.pop()

15. we can use remove function to remove certain value: 

        fib.remove(89)    // if we have two 89 only the first one will be removed

16. comments in python is #

17. we can use standard input or output in python: 

    name = input("Tell me your name")
    print(name)

18. If we want to use operators between two types, we can use type casting: 

        (int)radius * 4

19. string formating in python:

        name = 'num 1 is {0} and num 2 is {1}'.format(num1, num2)
        name = 'num 1 is {0:.2} and num 2 is {1:.3f}'.format(num1, num2)


17. Usign F-formatting :

        print(f'num 1 id {num1:.2} and num 2 is {num2:.4f}')

18. If in the python:

        if age < 18:
                print("you are young")
        elif age < 14:
                print("")
        else:
                print()

19. for loops in python: 
        pots = ['ryu','crystal', 'yoshi']

        for ninja in ninjas:                    you can get index as well as value for index, ninja in enumerate(ninjas):
                if ninja == "yoshi"
                        break
        print(ninja)

20. While loops in python: 

        age = 25

        while num < age:
                print(num)
                num += 1

21. range in python: 

        for n in range(5):
                print(n)

        for n in range(0,20,4)
                print(n)

        burger = ['beef', 'chicken', 'veg', 'supreme', 'double']

        for n in range(len(burgers))
                print(n, burgers[n])

22. functions in python:

        def greet():
                print("hello world")
        greet()  #calling the function
        #############
        def greet(name, time):  # these parameters is required (default is by =)
                print(f"good {time} {name}, hope you are well)
        greet("shaun", "morning")
        ###########
        def area(radius):
                return 3.142 * radius * radius
        radius = int(input("enter the radius"))
        area(radius)

23. the scope of the variables in python is like js and  we can use global keyword to override the 
        global varibale:
        
        myname = "alireza"
        def greet():
                global myname
                myname = "ghasem" # you can change the global varibale

24. Dictionaries in python, it is like js object notation:
        
        ninja_belts = {
                "crystal": "red",
                "ryu": "black"
        }
        we can get it with bracket notation:
                ninja_belts["crystal"]

25. we can check for the existance of the key in dictionaries:

        "yoshi" in ninja_belts #it returns false
                or 
        ninja_belts.keys() # it returns dict_keys(['crystal', 'ryu'])
                we can type cast dict_keys
        list(ninja_belts.keys())
                we can use values just like keys
        ninja_belts.values()  # it returns dict_values(["balck", "red"])

                # we can also type cast dict_values

        vals = list(ninja_belts.values())

                # and we can use count("black") to find the count of the black in vals list
        vals.count("black")

26. we can define dictionaries in another format: 

        person = dict(name = "shaun", age = 27, height = "6ft")

27. we can cycle through the dictionary:

        for key, val in <dictionary name>.items():

28. we can use sorted function to sort the list: 

        nums = [1, 5, 4, 2, 10]

29. set(nums) remove the duplicates but remove the orders.

30. we can use set(ninjas.values())  # ninja is dictionary

31. to define class: 

        class Planet:                   # the first letter should be upper case
                def __init__(self):
                        self.name = "Hoth"
                        self.radius = 20000
                def greet(self)
                        return f'my name is {self.name}'
        
# and you can make new object like this
        hoth = Planet()

32. If you have class or function that you want to leave them empty, just add pass in it:
	
	class Employee:
		pass

33. We can use class methods, with class names, and pass the instance you want to the function.
	
	Employee.get_full_name(emp1) is equal to emp1.get_full_name()

34. You can get the namespace of the class, function, object by using __dict__:
	
	print(emp1.__dict__)

35. we can give another parameters in __init__ function: 

        class Planet:
                def __init__(self, name, radius)
                        self.name = name
                        self.radius = radius

36. We can apply class level attributes: 
        class Planet:
                shape = 'round'
                def __init__(self, name, radius)
                        self.name = name
                        self.radius = radius

        and we can access this with name of the class as well as instance of class: Planet.shape

	if you change the class level attribute for a instance, it only will be applied to that instance,
	and this attribute will be added to the namespace of the instance.

37. we can also define class level methods:
        class Planet:
                shape: 'round'
                def __init__(self, name, radius)
                        self.name = name
                        self.radius = radius
                @classmethod
                def comment(cls):
                        return f'all planets are {cls.shape}'

        and we can access this with name of the class as well as instance of class: Planet.comment()

38. We can use class methods for making alternative constructors: 
	
	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)		# here we use constructors

39. we can also define static methods, static methods, don't have access to class and self: 

        class Planet:
                shape: 'round'
                def __init__(self, name, radius)
                        self.name = name
                        self.radius = radius
                @classmethod
                def comment(cls):
                        return f'all planets are {cls.shape}'
                @staticmethod
                def spin(speed = '2000 miles'):
                        return f'the planet is spins with {speed}'

        and we can access this with name of the class as well as instance of class: Planet.comment(1000)

40. We can use help function to see the details and namespaces of class or object or function: 

                print(help(Employee))

41. we can call base class constructor in python in two way:
        
        class Developer(Employee):
                def __init__(self, first, last, pay, prog_lang):
                        super().__init__(first, pay, prog_lang)                 or Employee.__init__(self, first, last, pay)

42. there are two built in funcitons in the python that we can use:

        isinstance(<object>, <class>)
        issubclass(<class>, <class>)

43. we use __repr__ function to print out the object, a good rule of thumb is use this to return something that we 
        can use to copy in python code: 

                def __repr__(self):
                        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

44. __str__ is just like __repr__ function but it is readable for end users:
        
                def __str__(self):
                        return '{} - {}'.format(self.fullname(), self.email)

[ATTENTION]
45. when you have __repr__ and __str__ at the same time, the print funciton will use __str__ function, but you can 
        use <object>.__repr__() and <object>.__str__() to access them directly.

46. when you add to int together in pyton for example print(1+2) you actually use a dunder method of int class, 

        print(int.__add__(1, 2))

47. you can use this __add__ function in your classes:

        def __add__(self, other):
                return self.pay + other.pay

48. There are many methods for Emulating numeric types, and you can see them in documentation.

49. len method is another type of dunder method:
        len('test')     or      'test'.__len__()

        and we can use this dunder funciton in our class: 

                def __len__(self):
                        return len(self.fullname())

50. in fact getters and setters is the way to use funcitons just like attrubutes: 

getter:

        @property
        def email(self):
                return "{}.{}@email.com".format(self.first, self.last)

        @property
        def fullname(self):
                return "{} {}".format(self.first, self.last)

        then we can use it just like attributes:

                print(emp.email)
                print(emp.fullname)
setter:

        @fulname.setter
        def fullname(self, name):
                first, last = name.split(' ')
                self.first = first
                self.last = last

        then we can give value to fullname:

                fullname = 'alireza rezaei'

deleter:

        @fullname.deleter
        def fullname(self):
                print('delete name')
                self.first = None
                self.last = None

        every time a attributes delete, it will run: 

                del emp.fullname

51. we can use modules and packages(collection of modules) in python: 

        from <file name> import <thing you want to import>
        from classes import Planet
[ATTENTION]
        from <filename> import *  (in this way you can import everything)

52. to make a package in python you have to make new folder and make __init__.py file in it,
        then you can make any python file (modules) in it:

        from <package name>.<module name> import <thing you want to import>

        you can separate the modules that you want to import with ,


53. List comprehension in python lists: 

        prizes = [5, 10, 100, 50]

        db_prizes = [ prize*2 for prize in prizes ]

        # db_prizes = [10, 20, 200, 100]

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        new_nums = [num**2 for num in nums if (num**2) % 2 == 0]

54. map functions in python:

        from random import shuffle

        def jumble(word):
                anagram = list(word)   # it make the string, list of characters
                shuffle(anagram)
                return ''.join(anagram) #'' is the spacer between letters
        words = ['beetroot', 'carrots', 'potatos']
        anagrams = []
        # we can use for loops or map function: 
        for word in words:
                anagrams.append(jumble(word))
        
        # or use map function: 
        print(list(map(jumble, words)))

        # or using list comprehension
        print([jumble(word) for word in words])

55. Filters in python:
        grades = ['A', 'B', 'F', 'C', 'D']

        def remove_fails(grade):
                return grade != 'F'

        print(list(filter(remove_fails, grades)))

56. lambdas: 
        lambda in python is one line functions: 

        nums = [1, 2, 3, 4, 5]

        print(list(map(lambda: n: n*n, nums)))

57. decoraters are the way to give additional behaviors to functions:

        def cough_dec(func):
                def func_wrapper():        #this name is optional
                        #code before function
                        print('cough')
                        func()
                        print('cough')
                return func_wrapper

        @cough_dec
        def question():
                print('can you give me a discount on that')


58. Generators in python is the way store variables, but not all of them:
	
	def squre_number(nums):
		for I in nums:
			yeild(I*I)

	my_nums = square_number([1, 2, 3, 4])

	for num in my_nums:
		print num

59. You can create generators just like list comprehension but instead of [] use ():
	my_nums = (x*x for x in [1, 2, 3, 4])

60. You can change generators to list:
	my_nums = list(my_nums)

61. read files in python: 

        ipsum_file = open('fiels/ipsum.txt')    #store the file in the list of string for each line

        for line in ipsum_file:
                print(line.rstrip())            #rstrip() removes the white spaces between lines

        ipsum_file.seek(0)                      # get back the pointer to the first char

        lines = ipsum_file.readlines()          # get the list of strings(each line is the list element)

        ipsum_file.seek(50)

        file_text = ipsum_file.read(100)        # read 100 char in strign grom ipsum_file

        ipsum_file.close()

# we can use another approach, and in the newer approach if we forget to close the file, the file will be colsed automatically:
        
        def sequence_filter(line):
                return '>' not in line

        with open('files/dna_sequence') as dna_files:
                lines = dna_files.readlines()
                filtered_lines = list(filter(sequence_filter, lines))
                print(filtered_lines)

62. Context manager is a protocol that is good for resource manager, and we can use 
	this protocol in python to make easy to understand and easy to maintain code: 

#this example is useless because open function already uses context manager protocol, but
	this example is for the sake of showing:

	class ManagedFile:
		def __init__(self, name):
			self.name = name
		
		def __enter__(self):
			self.file = open(self.name, 'w')
			return self.file
		def __exit__(self, exc_type, exc_val, exc_tb):
			if self.file:
				self.file.close()

With ManagedFile('hello.txt') as f:		# when we use class constructor in with statement the enter function will be called
	f.write('salam')			# and at the end the exit function will be called



63. __name__ is the special variable in python that when we run the module directly it is set to 
	__main__, but if you import the module and run it in other file, the names will be the name 
	of the module

64. So if __name__ == "__main__" means that a files run directly else, it is as same as file name

65. we can use sys module to get the list of locations that python check for the 
        existence of a module: 
        
        import sys
        print(sys.path)

the first element in this list, is the current directory, and the second element is the standard library, 
        you can add to second location, and move the standard library to third location:

        export PYHTONPATH="your new address"

66. you can add path to the sys.path:   (sys.path is just the list) but this is temporary
        
        import sys
        sys.path.append('the address of your module')



67. the second element in sys.path is the standard library, and we can import some modules from this library: 

        import random, math, datetime, calender, os

        print(os.getcwd())  # get the current directory

68. os module is one of the modules in standard library, and you can use it to get some of the underlying os features.

69. you can use built in dir() funciton when you are working with new modules to see the features of this module.

        print(dir(os))

70. some of the features of os module: 

                import os
                
                os.chdir("addrees")            # changes the current working directory

                print(os.getcwd())              
                print(os.listdir())             # list the files and folders in the current directory

                os.mkdir('folder name')         # make the folder only in one level
                os.makedirs('sdfa/fads')        # if you want you can make several level folder
                os.rmdir('fa/dfas')             # delete the last dir
                os.removedirs('dfas/fads')      # delete recursively
                os.rename('original file name', 'new file name')        # to rename file or folders

                os.walk()                       is generator that yeild a three valued tuples when it traverse the directory

                for dirpath, dirnames, filenames is os.walk('address'):


                file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

                there are many other functions in os.path and you can see them, print(dir(os.path))

///////////////////////// Python and Operating system /////////////////
to see which python you are using:
        which python3
        type python (this even shows the aliases)

71. you can see the directories that your machine looks for the terminal command (see your os environment variables):
        echo $PATH

72. you can add to this $PATH variables in .bash_profile

        export PATH = "<address>:${PATH}"               # this way add to the first section of PATH variable

73. to see all your environment variables: 

        env 

74. you can make alias for python in .bash_profile or just simply run alias python=python3 in terminal, but if you restart your 
        terminal this alias will be removed so, you need to add this to your .bash_profile file:

        alias python=python3
        alias pip=pip3.8

75. if you have lot of virtual environment, and in every environment you have same python, so you can't understand which python your are 
        running, so you have to import sys:

                print(sys.executable)

76. When you use pip install, the pip will install the package in the directory that pip is located, but when you use python to import the 
        package the python will use the python directory, see if the pip that is running and the python that is runnig is not in the same 
        directory you will have problem for importing the package.
        

77. you can see all your python global packages:
        pip list

78. if you run pip freeze you get all the global packages beside local packages in the environment:

        pip freeze --local > requirements.txt

79. you can install all the packages in the requirements.txt file: 
        pip install -r requirements.txt


80. to run the flask app First, make sure virtualenv is installed
    $ pip3 install virtualenv

81. Then create a directory for your new Flask project
    $ mkdir MyNewFlaskApp

82. Navigate to your newly created directory
    $ cd MyNewFlaskApp

83. Create your virtual environment with venv name
    $ virtualenv venv --system-site-packages        #venv is the name

    (you can also specify the python version in virtual env: virtualenv -p /usr/bin/python2 <env name>)

84. Activate the virtual environment
    $ source venv/bin/activate                      #vene is the name of environment variable

    (you can type deactivate to deactive the environment)
    (then you can delete the environment rm -rf <env name folder>)

85. you can also use venv to make virtual env:

        python -m vene <virtual name>

        to activate it create new terminal or:
        source <env full absoulute address>

//////////////////// Conda package manager  /////////////////

85. conda is a package manager in anaconda, you can use it to install python packages, and other packages that is not 
        on python.

        conda list      (you can see the conda packages)

86. you can create virtual environment with conda, and you can path some starting packages:
        
        conda create --name my_app flask sqlalchemy

        conda create --prefix=yourEnvName

then you have to activate it:

        conda activate my_app

87. all the conda environments store in the /Users/mac/miniconda3/envs/ folder:
        you can see all the conda environmet:

                conda env list

88. you can delete the conda environment:

        conda remove --name <env name> --all


/////////////////////   PIP package manager     ////////////////////

89. you can search for a package with pip:

        pip search <package name>

90. then you can install it: 

        pip install <package name>

91. you can see the installed packages: 

        pip list

92. you can see the outdated packages using -o or --outdated:

        pip list -o     (--outdated)

93. you can upgrade the package with pip:

        pip install -U <package name>

94. you can save the required packages: 

        pip freeze > requirements.txt

95. to install the requirements packages:

        pip install -r <requirement file name>