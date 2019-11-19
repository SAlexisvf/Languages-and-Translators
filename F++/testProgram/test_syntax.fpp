int a, c;
int hola123, hola456;
double b, b2;
int var1[10][10], var2[10][10];

# this is a dummy comment describing myFunc1
function myFunc1() {
    c = 13;
    consoleRead(a);
    if (a > c) {
        a = 15;
    }
    elif (a < c and a > 0){
        a = 20;
    }
    else {
        a = 25;
    }
}

# this is a dummy comment describing myFunc2
function myFunc2() {
    hola123 = 14 + (231 * 123 / 12) - (123 + (123 - 98 * 123));
    b = 1233.412 + 1234.11;
    while (a > 30) {
        for (c = 5;c <= 20; c++) {
            consoleWrite(hola123 + hola456);
            if (b == 150.5021){
                consoleWrite("dummy print");
            }
        }
        a++;
    }
}

main() {
    consoleWrite("this is the main program!");
    consoleWrite(hola123 + hola456);
    call myFunc1();
    call myFunc2();
}