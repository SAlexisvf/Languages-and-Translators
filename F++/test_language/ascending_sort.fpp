int mat[10];
int dimention, i, j, temp, option;

function fill_mat(){
    for (i = 0; i < dimention; i++){
        consoleWrite('Value for vector[', i, ']: ');
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