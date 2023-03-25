function getTotalX(a,b){
    let lcm_a;
    let gcd_b;

    function gcd(x,y){
        while (y){
            let swap = x;
            x = y;
            y = swap;
            return x
        }
    }

    function lcm(x,y){
        return parseInt(x * y / gcd(x,y))
    }

    for(let i=1; i<a.length; i++){
        lcm_a = lcm(lcm_a,a[i]);
    }

    for(let i=1; i<b.length; i++){
        gcd_b = gcd(gcd_b,b[i])
    }

    let count = 0;
    let multiple_of_lcm = lcm_a;
    while (multiple_of_lcm < gcd_b){
        if((gcd_b % multiple_of_lcm) === 0){
            count +=1
        }
    }
}