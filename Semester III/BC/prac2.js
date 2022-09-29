class AjlistNode
{
constructor(id)
{
this.id = id; this.next = null;
}
}
class Vertices
{
constructor(data)
{
this.data = data; this.next = null; this.last = null;
}
}
class Graph
{
constructor(size)
{
this.size = size;
this.node = Array(size).fill(null); this.setData();
} 
setData()
{
if (this.size <= 0)
{
console.log("\nEmpty Graph");
}
else
{
for (var index = 0; index < this.size; index++)
{
this.node[index] = new Vertices(index);
}
}
}
connection(start, last)
{
var edge = new AjlistNode(last); if (this.node[start].next == null)
 
{
this.node[start].next = edge;
}
else
{
this.node[start].last.next = edge;
}
this.node[start].last = edge;
} 
addEdge(start, last)
{
if (start >= 0 && start < this.size &&
last >= 0 && last < this.size)
{
this.connection(start, last);
}
else
{
console.log("\nHere Something Wrong");
}
}
printGraph()
{
if (this.size > 0)
{
for (var index = 0; index < this.size; ++index)
{
process.stdout.write("\nAdjacency list of vertex " +index + " :"); 
var edge = this.node[index].next; 
while (edge != null)
{ 
process.stdout.write(" " + this.node[edge.id].data); 
edge = edge.next;
}
}
}
}
findIndegree(indegree)
{
if (this.size <= 0)
{
return;
}
var edge = null;
for (var i = 0; i < this.size; ++i)
{
edge = this.node[i].next; 
while (edge != null)
{

indegree[edge.id]++;
 
edge = edge.next;
}
}
}
findSequence(indegree, visit, index, result)
{
if (index == this.size)
{
// Display result 
process.stdout.write("\n"); var j = 0;
while (j < this.size)
{
process.stdout.write(" " + result[j]); 
j++;
}
return;
}
var edge = null; var i = 0;
while (i < this.size)
{
if (indegree[i] == 0 && visit[i] == false)
{
visit[i] = true;
result[index] = i;
// Get node edge
edge = this.node[i].next;
// Reduce indegree 
while (edge != null)
{
indegree[edge.id]--;
edge = edge.next;
}
this.findSequence(indegree,visit, index + 1, result);
visit[i] = false;
edge = this.node[i].next;
// Increase indegree 
while (edge != null)
{
indegree[edge.id]++; 
edge = edge.next;
}
}
i++;
}
}
topologicalSort()
{
if (this.size <= 0)
{
return;
}
// Use to track node
var visit = Array(this.size).fill(false);
// Store indegree of node edges
var indegree = Array(this.size).fill(0);
// Store result of topological sort
var result = Array(this.size).fill(-1);

// Find indegree of each node in graph 
this.findIndegree(indegree); 
process.stdout.write("\n"); 
this.findSequence(indegree, visit, 0, result);
}
}

var g = new Graph(6);
g.addEdge(1, 0);
g.addEdge(1, 4);
g.addEdge(1, 5);
g.addEdge(2, 0);
g.addEdge(2, 4);
g.addEdge(2, 5);
g.addEdge(3, 4);
g.addEdge(3, 5);
g.addEdge(5, 4);
g.printGraph(); 
g.topologicalSort();