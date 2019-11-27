int a[10];
double b[5];
int x[4][4];
int i, j, k;

function myfunc(){
    for (i = 0; i < 10;i++){
        a[i] = i * 2;
    }
    i = 0;
    while (i < 10){
        consoleWrite(a[i]);
        i = i + 1;
    }
}

main (){
    k = 0;
    for (i = 0; i < 4; i++){
        for (j = 0; j < 4; j++){
            consoleWrite('Give me [',i,']','[',j,']', '%n');
            consoleRead(x[i][j]);
        }
    }

    for (i = 0; i < 4; i++){
        for (j = 0; j < 4; j++){
            consoleWrite(x[i][j]);
        }
        consoleWrite('%n');
    }

}