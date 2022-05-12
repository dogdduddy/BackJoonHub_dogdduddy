fun GCD(a:Int, b:Int):Int {
    var a = a; var b = b; var temp:Int
    while(a%b != 0) {
        temp = a%b
        a = b
        b = temp
    }
    return b
}

fun main() {
    var t = readLine()!!.toInt()

    for(i in 0 until t) {
        var temp = readLine()!!.split(" ").map { it.toInt() }
        var gcd =  GCD(temp[0], temp[1])
        println(temp[0]*temp[1]/gcd)
    }
}