# Code Editor, Syntax Analyzer, and Interpreter
This project combines a code editor, a syntax and semantic analyzer, and an interpreter for a custom programming language. It allows users to write, analyze, and execute code within a single integrated environment.

## Features
### Code Editor
* Intuitive text editor for writing and editing source code.
* Built-in menu with examples of correct and incorrect code for testing.

### Lexer, Syntax and Semantic Analyzer
* Lexer Analysis: Reviews the code tokens and classifies them.
* Syntax Parsing: Validates code structure against a formal grammar.
* Semantic Analysis: Checks proper usage of identifiers, types, and operations.

### Interpreter
* Executes the code directly within the application.
* Displays output, including any errors.

### Output Logs
* Parser Results: Indicates whether the code is syntactically correct.
* Code Results: Displays as output the outputs that have been indicated in the code
* Reduction Steps: Details the sequence of grammar reductions.
* Symbol Table Updates: Logs changes made to variables during the execution phase.
* Lexer result: The result of lexical analysis
* Events: Displays the main events during code execution

## Setup and Execution
### Requirements
Ensure you have the following installed:
* Python 3.10.4
* tkinter == 8.6
* ply == 3.11

### Execution Steps
1. Navigate to the App Directory: navigate to the app folder.
2. Run the Main Script: Execute the script main.py to launch the editor, analyzer, and interpreter.


## How to Use
1. Type or paste your code into the editor, or upload the file wherever it is stored.
2. Run the code or a file to perform the analysis and display the output
3. View detailed results in the "Últimas salidas" menu or outputs folder:
* SymbolTable_Updates.txt: Stores updates to variables, recording their creation and changes to the values ​​they store.
* Reductions_List.txt: Displays a log of how the reduction order was when creating the tree for syntactic analysis.
* Advertisements.txt: Displays a log of certain relevant events, such as variable declaration and assignment, operations, closing if structures, among others.
* Token_Count.txt: Displays a count of the code tokens, showing them according to their classification, including those that are not valid for the language.


# Documentación del Lenguaje de Programación: CPY
### Index:
* Introduction
* Basic syntax
* Data types
* Declaration and assignment
* Operators
* Flow control
* Comparison Operators
* Functions

## Introduction
Briefly describe your language: The CPY language is made to work with the interpreter of the current project, it has some basic functions and is based on the characteristics of some others, such as c or python.
It is made by team 05 of the compiler course.

## Basic Syntax
Example:
```
int a = 1;
int b = 5;
int c = 6;
float x;
int decision = 1;

if (decision == 1) {
    x = (-b + sqr((exp(b 2) - 4*a*c))) / (2 * a);
    printf("Primer valor de de la variable 'X':");
} else {
    x = (-b - sqr((exp(b 2) - 4*a*c))) / (2 * a);
    printf("Segundo valor de de la variable 'X':");
}


printf(x);
```

## Data types
There are 2 types of data that can be operated on:

* Integers (int): Numbers without decimals.
* Floats (float): Numbers with decimals.

## Declaration and assignment:
### Declaration
To declare a variable the following structure is used:
```
Data_Type identifier;
```
When declaring a variable, it can also be assigned a provisional value:
```
Data_Type identifier = value;
```
Example:
```
int a;
float b = a;
int c = 4; 
```
### Assignment
To assign a value to a variable, the following structure is used:
```
Identifier = value;
```
> [!NOTE]
> You can assign the result of arithmetic operations or the value of other variables

Example:
```
a = 4;
a = 2 + 3
a = c; 
```

## Operators
The following operators exist:
| Operator | Description | Example |
| ------------- | ------------- | --- |
| +  | Plus | a + b |
| -  | Minus | a - b |
| *  | Times |  a * b |
| /  | Divide |  a / b |

> [!NOTE]
> Operations can be performed with numbers, variables or with the result of other operations.

## Flow control

### Conditionals
The if structure allows you to control the flow of the program, executing certain sections of the code depending on whether a condition is met.
Use the following structure:
```
if (condition)
{
 Code to execute
}
```
You can also add a code to execute in case the condition is not met.
```
if (condition)
{
 Code to execute
}
else
{
 Code to execute otherwise
}
```
Example:
```
int a = 5;
if (a >= 3){
 printf("El número es mayor o igual que 3");
}
else {
 printf("El número es menor que 3");
}
```

## Comparison operators
The following comparison operators exist:
| Operator | Description | Example |
| ------------- | ------------- | --- |
| < | Less than | a < b |
| > | Greater than | a > b |
| <= | Less or equals than |  a <= b |
| >= | Greater or equals than |  a >= b |
| == | Equal to |  a == b |

These are used to compare the numerical values ​​of 2 numbers, arithmetic operations or variables.

## Functions

### Print on output
This function is responsible for displaying as output of the code what the user wants, this can be a value or a text string.
To use it you must have the following structure
```
printf(value);
printf("Text string");
```
Example: 
```
printf("The result is");
printf(result);
printf("The result of a + b * 5 is");
printf(a + b *5);
```

### Raise to power
In this function you enter a value and the power to which you want to raise it, and it returns the result.
Follow the following structure:
```
exp (base exponente)
```
Example:
```
a = exp (3 2);
```
> [!WARNING]
> The exponent can only be a number
>
> If you want the base to be an operation, make sure it is encapsulated in parentheses.

### Take square root
In this function you enter a value and it returns its square root.
Follow the following structure:
```
sqr (Value)
```
Example:
```
a = sqr( 36 );
```
> [!WARNING]
> If you want to calculate the square root of an operation, make sure it is encapsulated within a pair of parentheses in addition to those of the function.
