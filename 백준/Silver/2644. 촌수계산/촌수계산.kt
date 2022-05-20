var target:Int = 0
var start:Int = 0
var cnt = 0
var check = false
lateinit var visited:IntArray
lateinit var arr:Array<MutableList<Int>>

fun main() {
    val n = readln().toInt()
    arr = Array<MutableList<Int>>(n+1) {i -> mutableListOf() }
    var temp = readln().split(" ").map { it.toInt() }

    visited = IntArray(n+1){0}

    start = temp[0]; target = temp[1]
    visited[start] = 1

    for(i in 0 until readln().toInt()) {
        temp = readln().split(" ").map { it.toInt()}
        arr[temp[0]].add(temp[1])
        arr[temp[1]].add(temp[0])
    }
    DFS(start, target, 0)
    if(check) {
        print(cnt)
    }
    else {
        print(-1)
    }
}

fun DFS(s:Int, t:Int, num:Int) {
    if(s==t) {
        cnt = num
        check = true
        return
    }
    for(i in arr[s]) {
        if(visited[i]==0 && !check){
            start = i
            visited[i] = 1
            DFS(i, t, num+1)
        }
    }
}

