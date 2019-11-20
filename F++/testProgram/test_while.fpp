int a, b, c;

function my_func1 () {
    a = 15;
    b = 10;
}

main() {

    c = 15;
    consoleRead(a);
    b = 30;

    for (a = 1; a < 10; a++){
        for (b = 1; b < 10; b++){
            c = 15 * 8;
        }
        if (b == 30){
            call my_func1();
        }
        elif (b == 25 and a > 4){
            b = 45;
        }
        else {
            consoleWrite("F");
        }
        
    }
    b = 15;
}