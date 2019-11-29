int i, y, fac, option, power_res;
double sum, x;

function factorial(){
    fac = 1;
    for (i = 1; i <= x; i++){
        fac = fac * i;
    }
}

function power(){
    power_res = 1;
    for (i = 1; i <= y; i++){
        power_res = power_res * x;
    }
}

function taylor(){
    sum = 1.0;
    for (i = 10 - 1; i > 0; i--){
        sum = 1 + x * sum / i;
    }
}

main() {
    do {
        consoleWrite('select an option', '%n');
        consoleWrite('1) calculate X!', '%n');
        consoleWrite('2) calculate X^Y', '%n');
        consoleWrite('3) calculate Taylor series', '%n');
        consoleWrite('4) exit', '%n');

        consoleRead(option);

        if (option != 4){

            consoleWrite('Provide X');
            consoleRead(x);
            
            if (option == 1){
                call factorial();
                consoleWrite(x, '! = ', fac, '%n');
            }

            if (option == 2){
                consoleWrite('%n', 'Provide Y', '%n');
                consoleRead(y);
                call power();
                consoleWrite(x, '^', y, '=', power_res, '%n');
            }

            if (option == 3){
                call taylor();
                consoleWrite('e^', x, '=', sum, '%n');
            }
        }

    } while (option != 4);
}