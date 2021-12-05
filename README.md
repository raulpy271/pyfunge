# pyfunge

An Interpreter of the language Befunge written in Python. This language is a [esoteric](https://esolangs.org/wiki/Main_Page) language which was created to demonstrate how is dificulty to create an compiller. Besides, the language is simple because it's have only a tiny set of commands, but they are a bit different of the commom languages, so the code is weird.

# Self-modification

The dificult of implementation resides in the self-modification property of the language, this means that the source-code can change itself in runtime, so, how to compile a code that only exists in runtime? It's a dificult task. See an example of code that change itself:

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

This code will prompt the user for a sequance of commands which will be placed in the X's above, when the user fill all X's the program direct the flow to the commands inserted by the user.

# Especifications

The interpreter support all commands of Befunge 93.

The original especification of Befunge-93 have a fixed limit of cells, which is 80x25. However, this interpreter don't establish a fixed limit of cells, the code can be more than 80x25, thus it's a turing complete implementation.

The especification of the language and all the commands can be found here: [Befunge-93](https://catseye.tc/view/Befunge-93/doc/Befunge-93.markdown).

