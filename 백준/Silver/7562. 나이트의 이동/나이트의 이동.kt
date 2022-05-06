import java.lang.Math.min

var bfs= mutableListOf<Array<Int>>()
var l = 0
var cnt = 10000
lateinit var visited:Array<Array<Int>>
val dx = arrayOf(-2, -1, 1, 2, 2, 1, -1, -2)
val dy = arrayOf(1, 2, 2, 1, -1, -2, -2, -1)

fun BFS(tx:Int, ty:Int){
    var x:Int; var y:Int; var num:Int
    while(!bfs.isEmpty()) {
        x = bfs[0][0]; y = bfs[0][1]; num = bfs[0][2]
        bfs.removeFirst()

        if(x==tx && y==ty) {
            cnt = min(cnt, num)
        }

        for(i in 0 until 8) {
            var nx = x + dx[i]
            var ny = y + dy[i]
            if(0<=nx&&nx<l&&0<=ny&&ny<l&&visited[ny][nx]==0) {
                visited[ny][nx] = 1
                bfs.add(arrayOf(nx, ny, num+1))
            }
        }
    }
}

fun main() {
    var t = readLine()!!.toInt()


    for(i in 0 until t){
        l = readLine()!!.toInt()
        visited = Array<Array<Int>>(l){ Array<Int>(l){0} }

        var temp = readLine()!!.split(" ").map{ it.toInt() }
        var x = temp[0]; var y = temp[1]

        temp = readLine()!!.split(" ").map{ it.toInt() }
        var tx = temp[0]; var ty = temp[1]

        visited[y][x] = 1
        bfs.add(arrayOf(x,y,0))
        cnt = 10000
        BFS(tx, ty)
        println(cnt)
    }
}