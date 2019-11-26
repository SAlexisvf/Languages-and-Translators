int a[10];
double b[5];
int i;

main (){
    for (i = 0; i < 10;i++){
        a[i] = i * 2;
    }
    i = 0;
    while (i < 10){
        consoleWrite(a[i]);
        i = i + 1;
    }
    consoleWrite(a[1+3]);

}