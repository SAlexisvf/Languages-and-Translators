int a, b;
double c, d;

function myfunc(){
   for(a = 1;a < 10;a++){
       consoleWrite(a);
   }
}

main() {
    consoleWrite('give me a:');
    consoleRead(a);
    if (a > 60){
        consoleWrite('your value is greater that 60');
    }
    else {
        b = a * 2;
        if(b > 60 or b == 67.99){
            call myfunc();
        }
    }
}