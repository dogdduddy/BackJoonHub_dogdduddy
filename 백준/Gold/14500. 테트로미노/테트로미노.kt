import kotlin.math.max
import kotlin.properties.Delegates

var dx = arrayOf(1,0,-1,0)
var dy = arrayOf(0,1,0,-1)
var cnt = 0
lateinit var map:Array<IntArray>
lateinit var visited:Array<IntArray>
var n:Int = 0
var m:Int = 0

fun dfs(x:Int, y:Int, num:Int, total:Int) {
    if(num == 4){
        cnt = max(total, cnt)
        return
    }
    for(i in 0 until 4) {
        var nx = x + dx[i]
        var ny = y + dy[i]
        if(nx>=0 && nx<m && ny>=0 && ny<n && visited[ny][nx]==0) {
            if(num==2) {
                visited[ny][nx] = 1
                dfs(x, y, num+1, total+map[ny][nx])
                visited[ny][nx] = 0
            }
            visited[ny][nx] = 1
            dfs(nx, ny, num+1,total+map[ny][nx])
            visited[ny][nx] = 0
        }
    }
}

fun main() {
    var temp = readLine()!!.split(" ").map { it.toInt() }
    n = temp[0]
    m = temp[1]
    map = Array<IntArray>(n){IntArray(m)}

    for(i in 0 until n) {
        var temp = IntArray(m)
        readLine()!!.split(" ").mapIndexed { index, v -> temp[index] = v.toInt() }
        map[i] = temp
    }
    visited = Array(n){IntArray(m)}
    for(i in 0 until n) {
        for (j in 0 until m) {
            visited[i][j] = 1
            dfs(j, i, 1,map[i][j])
            visited[i][j] = 0
        }
    }
    print(cnt)
}