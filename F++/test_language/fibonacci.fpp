int i, num, a, b, c;

function recurive(){
    c = a + b;
    a = b;
    b = c;
    consoleWrite(c);
    i = i + 1;
    if (num - 1 > i){
        call recurive();
    }
}

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
        i = 1;
        call recurive();
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