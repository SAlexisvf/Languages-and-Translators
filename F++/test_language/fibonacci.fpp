int i, num, a, b, c;

function fibonacci(){
    a = 1;
    b = 1;
    c = 0;
    consoleWrite('%n','Sequence from 0 to ', num, ': ');
    if (num == 0 or num == 1){
        consoleWrite(num);
    }
    # just to test else if
    elif (num == 2){
        consoleWrite('1', ' ', '1');
    }
    else {
        consoleWrite ('1', ' ', '1');
        for(i = 1; num-1 > i; i++){
            c = a + b;
            a = b;
            b = c;
            consoleWrite(c);
        }
    }
}

main() {
    consoleWrite('Fibonacci sequence program', '%n');

    do {
        consoleWrite('Provide a positive integer: ', '%n');
        consoleRead(num);
    } while (num < 0);

    call fibonacci();

}