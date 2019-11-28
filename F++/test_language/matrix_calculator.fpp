int mat_1[4][4];
int mat_2[4][4];
int res[4][4];
int dimention_1, dimention_2, dimention_3, dimention_4;
int i, j, k;
int option;

function fill_mat_1(){
    consoleWrite('Fill matrix A', '%n');
    for (i = 0; i < dimention_1; i++){
        for (j = 0; j < dimention_2; j++){
            consoleWrite('Value for A[', i, '][', j, ']');
            consoleRead(mat_1[i][j]);
        }
    }
}

function print_mat_1(){
    consoleWrite('Matrix A:', '%n');
    for (i = 0; i < dimention_1; i++){
        for (j = 0; j < dimention_2; j++){
            consoleWrite(mat_1[i][j]);
        }
        consoleWrite('%n');
    }
}

function fill_mat_2(){
    consoleWrite('Fill matrix B', '%n');
    for (i = 0; i < dimention_3; i++){
        for (j = 0; j < dimention_4; j++){
            consoleWrite('Value for B[', i, '][', j, ']');
            consoleRead(mat_2[i][j]);
        }
    }
}

function print_mat_2(){
    consoleWrite('Matrix B:', '%n');
    for (i = 0; i < dimention_3; i++){
        for (j = 0; j < dimention_4; j++){
            consoleWrite(mat_2[i][j]);
        }
        consoleWrite('%n');
    }
}

function multiply(){
    for (i = 0; i < dimention_1; i++){
        for (j = 0; j < dimention_4; j++){
            res[i][j] = 0;
            for (k = 0; k < dimention_3; k++){
                res[i][j] = res[i][j] + mat_1[i][k] * mat_2[k][j];
            }
        }
    }
}

function add(){
    for(i = 0; i < dimention_1; i++){
        for(j = 0; j < dimention_4; j++){
            res[i][j] = mat_1[i][j] + mat_2[i][j];
        }
    }
}

function print_mat_result(){
    consoleWrite('%n', 'Result matrix: ', '%n');
    for (i = 0; i < dimention_1; i++){
        for (j = 0; j < dimention_4; j++){
            consoleWrite(res[i][j]);
        }
        consoleWrite('%n');
    }
}

main (){

    do {
        consoleWrite('Provide the dimentions for the first matrix: ', '%n');
        consoleWrite('i: ');
        consoleRead(dimention_1);
        consoleWrite('j: ');
        consoleRead(dimention_2);

        consoleWrite('Provide the dimentions for the second matrix: ', '%n');
        consoleWrite('i: ');
        consoleRead(dimention_3);
        consoleWrite('j: ');
        consoleRead(dimention_4);

        if (dimention_2 != dimention_3){
            consoleWrite('Dimentions not valid!', '%n');
        }
        if (dimention_1 > 5 or dimention_2 > 5 or dimention_3 > 5 or dimention_4 > 5){
            consoleWrite('Size should be less than 5!', '%n');
        }

    } while (dimention_2 != dimention_3 or dimention_1 > 5 or dimention_2 > 5 or dimention_3 > 5 or dimention_4 > 5);

    call fill_mat_1();
    consoleWrite('%n');

    call fill_mat_2();
    consoleWrite('%n');

    call print_mat_1();
    consoleWrite('%n');

    call print_mat_2();
    consoleWrite('%n');

    do {
        consoleWrite('Select 1 to multiply or 2 to sum', '%n');
        consoleRead(option);

        if (option == 1){
            call multiply();
        }
        elif (option == 2){
            call add();
        }
        else {
            consoleWrite('Not a valid option!', '%n');
        }
    } while (option != 1 and option != 2);
    
    call print_mat_result();

}