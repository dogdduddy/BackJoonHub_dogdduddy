fun main() {
    val t = readLine()!!.toInt()

    repeat(t) {
        val temp = readLine()!!.split(" ").map { it.toInt() }
        val m = temp[0]; val n = temp[1]; val x = temp[2]; val y = temp[3]
        var check = false

        for(i in x .. m*n/gcd(m,n) step m) {
            if((if(i%n==0) n else i%n)==y) {
                println(i)
                check = true
                break
            }
        }
        if(!check)
            println(-1)
    }
}

fun gcd(a:Int, b:Int):Int = if(b==0) a else gcd(b,a%b)