# Languages and Translators
___
Programming language designed and implemented in Python using the PLY library.
## F++ language
The language is based on C ++ and has some of its basic functionalities such as:
* int and double variable types
* arithmetic and boolean operations 
* loops (while, do while, for)
* conditionals (if, else if, else)
* functions (no params and no return value)
* arrays (uni-dimentional and bi-dimentional)
* console read and write

### F++ code snippet
```cpp
int mat[10];
int dimention, i, j, temp, option;

function fill_matrix(){
    for (i = 0; i < dimention; i++){
        consoleWrite('Value for vector[', i, ']: ','%n');
        consoleRead(mat[i]);
    }
}

function print_mat(){
    for (i = 0; i < dimention; i++){
        consoleWrite(mat[i]);
    }  
}

function sort_mat(){
    for (i = 0; i < dimention; i++){
        for (j = i + 1; j < dimention; j++){
            if (mat[i] > mat[j]){
                temp = mat[i];
                mat[i] = mat[j];
                mat[j] = temp;
            }
        }  
    }  
}

main () {
    do {
        consoleWrite('Provide the vector dimention' , '%n');
        consoleRead(dimention);
        if (dimention > 10){
            consoleWrite('Dimention should be less than 10!!', '%n');
        }
    } while (dimention > 10);

    do {
        call fill_mat();
        consoleWrite('unsorted vector: ', '%n');
        call print_mat();
        call sort_mat();
        consoleWrite('%n', 'sorted vector: ', '%n');
        call print_mat();
        consoleWrite('%n', 'Do you want to sort another vector? (1 = yes, 0 = no)', '%n');
        consoleRead(option);
    } while (option == 1);
}
```
### F++ code snippet output
```bash
Provide the vector dimention
8

Value for vector[ 0 ]: 5
Value for vector[ 1 ]: 34
Value for vector[ 2 ]: 6
Value for vector[ 3 ]: 12
Value for vector[ 4 ]: 3
Value for vector[ 5 ]: 134
Value for vector[ 6 ]: 21
Value for vector[ 7 ]: 33

unsorted vector:
5 34 6 12 3 134 21 33

sorted vector:
3 5 6 12 21 33 34 134

Do you want to sort another vector? (1 = yes, 0 = no)
0
```
### Test language
In order to test the language just add a file to the test_language folder and run:
```cmd
python F++.py test_language/your_test_file.fpp
```