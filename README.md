# pyfunge

An Interpreter of the language Befunge written in Python. This language is an [esoteric](https://esolangs.org/wiki/Main_Page) language that was created to demonstrate the difficulty of creating a compiller. Also, the language is simple because it only has a small set of commands, but they are a bit different from commom languages, so the code is weird.

The language is made up of a stack, so you don't store values in variables, you push/pop values into a global stack. In commom language each command has an order and you run the commands one after the other, in a single order. But in Befunge, the code are placed in a 2D grid, so you have four different execution flows, from left to right, from right to left, bottom to top and top to bottom. The below program prints `1` using the normal flow and then prints `2` following the top to down flow.

```bf
1 . v
    2
    .
    @
```

If you want to know how the language work and how to program on it, see the following documentations:

- [Befunge - Esolang](https://esolangs.org/wiki/Befunge)
- [Befunge - Specification](https://catseye.tc/view/Befunge-93/doc/Befunge-93.markdown)

# Execution



# Self-modification

The dificult of implementation lies in the self-modification property of the language, this means that the source-code can change itself in runtime, so how to compile a code that only exists in runtime? It's a dificult task. Here's an example of code that change itself:

```
$ cat examples/self_changing_code.bf 

2  v                         
v  <                      
>> 1+: ~ \ 7p : 28*1+ `v                
                       !    
 ^                     _$v     
v                        <   
   @@@@@@@@@@@@@@@@@   
>#@XXXXXXXXXXXXXXXX@  
   @@@@@@@@@@@@@@@@@   


The X's will be replaced by the commands inserted by the user in runtime.
```

This code will ask the user for a sequence of commands that will be placed in the X's above, when the user fills all X's the program will direct the flow to the commands entered by the user.

# Specifications

The interpreter support all commands of Befunge 93.

The original specification of Befunge-93 have a fixed limit of cells, which is 80x25. However, this interpreter don't establish a fixed limit of cells, the code can be more than 80x25, thus it's a turing complete implementation.

The language specification and all the commands can be found here: [Befunge-93](https://catseye.tc/view/Befunge-93/doc/Befunge-93.markdown).
