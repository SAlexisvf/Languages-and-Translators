int num;

main(){
    do {
        consoleWrite('Give me a number between 0-7', '%n');
        consoleRead(num);

        if (num == 0){
            consoleWrite('Cero!', '%n');
        }
        elif (num == 1){
            consoleWrite('Uno!', '%n');
        }
        elif (num == 2){
            consoleWrite('Dos!', '%n');
        }
        elif (num == 3){
            consoleWrite('Tres!', '%n');
        }
        elif (num == 4){
            consoleWrite('Cuatro!', '%n');
        }
        elif (num == 5){
            consoleWrite('Cinco!', '%n');
        }
        elif (num == 6){
            consoleWrite('Seis!', '%n');
        }
        elif (num == 7){
            consoleWrite('Siete!', '%n');
        }
        else {
            consoleWrite('Invalid number! Try again.', '%n');
        }
    } while (num > 7 or num < 0);
}