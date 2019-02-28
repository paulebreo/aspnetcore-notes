public static void Print(string s) => Console.WriteLine(s);

# FSA entrance exam workshop questions
## Utopian tree
source: https://www.hackerrank.com/challenges/utopian-tree/problem

## Utopian tree
```csharp
public static void Print(string s) => Console.WriteLine(s);

public static int Utopian(int n) {
  int height = 0;
  for(var i=0; i<=n; i++){
    if((i%2) == 0) height += 1;
    else height *= 2;
  }
  return height;
}
public static void Main (string[] args) {
  var ans = Utopian(5);
  Print(ans.ToString());
}
```

## IndexOf
```csharp
public static int IndexOf(string original, string target) {
  for(var i=0;i<original.Length;i++) {
    if(target == original[i].ToString()) {
      return i;
    }
  }
  return -1;
}

public static void Main (string[] args) {

  var ans = IndexOf("elephant", "p");
  Print(ans.ToString());

}
```

## RotateArray
Learnings:
 * Custom Extension method
 * GetRange method
 * Return IEnumerable<T>
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
//source: https://stackoverflow.com/questions/20678653/readable-c-sharp-equivalent-of-python-slice-operation
public static class MyExtension {
public static IEnumerable<T> Slice<T>(this List<T> source, int from, int to) => source.GetRange(from, to - from);
}

class MainClass {

  public static IEnumerable<int> RotateArray(List<int> arr, int n) {

    if(n >= 0) {
     var right = arr.Slice(0,n);
     var left = arr.Slice(n, arr.Count);
     return left.Union(right); 
    } else {
       var right = arr.Slice(0,arr.Count+n);
       var left = arr.Slice(arr.Count+n, arr.Count);
       return left.Union(right); 
    }
  }

  public static void Main (string[] args) {
    var arr = new List<int> {1,2,3,4};
    var ans2 = RotateArray(arr, -1);
    Print(String.Join(",", ans2));
  }
}
```

## First repeating letter
```csharp
// Returns the first letter that in repeated
// Example: "hello ear" returns "l"
public static string FirstRepeat(string s)
{
    for (int i = 0; i < s.Length; i++)
    {
        if(i < s.Length -1)
        {
            if (s[i] == s[i + 1]) return s[i].ToString();
        }
    }
    return "no repeating letters";
}

static void Main(string[] args)
{
    var ans = FirstRepeat("hello geeks");
    Print(ans.ToString());
    Console.ReadLine();
}
```

## Count number of duplicates
```csharp

 // Returns the first letter that is a duplicate
// Example: "hello ear"  returns 2
public static int CountDuplicates(string s)
{
    var dups = new List<char>();
    for (int i = 0; i < s.Length; i++)
    {
        var currentLetter = s[i];
        for (int j = i+1; j < s.Length; j++)
        {
            var nextLetter = s[j];
            if (currentLetter == nextLetter)
            {
                if (!dups.Contains(currentLetter))
                    dups.Add(s[j]);
                var ds = String.Join(",", dups);
                Print($"Found a duplicate {s[i]} - the dups is now {ds}");
            }
        }
    }
    return dups.Count;
}


static void Main(string[] args)
{
    var ans = CountDuplicates("hello geekso");
    Print(ans.ToString());
    Console.ReadLine();
}
```

## Right triangle
Learnings 
* new string() 
* Enumerable.Repeat() - https://stackoverflow.com/questions/3754582/is-there-an-easy-way-to-return-a-string-repeated-x-number-of-times

```csharp
// Given a n number of rows, it prints out stars in descending order
// E.g. n = 3
//  ***
//  **
//  *
public static string RightTriangle(int n)
{
    var ans = "";
    while(n > 0)
    {
        if (n > 1)
            ans += new string('*', n) + "\n";
        else
            ans += new string('*', n);
        n--;
    }
    return ans;
}


static void Main(string[] args)
{
    var ans = RightTriangle(3);
    Print(ans.ToString());
    Console.ReadLine();
}
```

## Palindrom check
Learnings
* new string(text.Reverse().ToArray())
```csharp
public static bool CheckPalindrome(string text)
{
    // We use reverse which returns an IEnumerable
    // but new string needs an array so we convert it to an array
    // then convert that array to a string and compare it with the original
    return text == new string(text.Reverse().ToArray());
}

static void Main(string[] args)
{
    var ans = CheckPalindrome("bob");
    Print(ans.ToString());
    Console.ReadLine();
}
```

# Sum of 2D Array
See: https://stackoverflow.com/questions/19034970/sum-multidimensional-array-c-sharp

Questions from above solutions: 
* what is yield return foo
* what is GetRow<T>
* what is parameter : T[,] array
```csharp
using System;
using System.Collections.Generic;
using System.Linq;

namespace REACTO
{
    class Program
    {
        public static void Print(string s) => Console.WriteLine(s);

         // Return the sum of a 2D array
        public static int SumMultiDim(List<List<int>> arr)
        {
            // flatten and sum
            return arr.SelectMany(i => i).ToList().Sum();
        }

        static void Main(string[] args)
        {
            var a = new List<List<int>> {
                new List<int> {1,2},
                new List<int> { 3,4}
            };
            var ans = SumMultiDim(a);
            Print(ans.ToString());
            Console.ReadLine();
        }
    }
}
```

# AlgoCasts - Stephen Grider (udemy)

## String reverse
Learnings:
* list of chars
* String.Join() list of chars
```csharp
using System;
using System.Collections.Generic;
class MainClass {
  public static void Print(string s) => Console.WriteLine(s);

  public static string ReverseString(string s) {
    var ans = new List<char>();
    for(var i=s.Length-1;i>=0;i--) {
      ans.Add(s[i]);
    }
    // return "foo";
    return String.Join("", ans);
  }
  public static void Main (string[] args) {
    var ans = ReverseString("hello");
    Print(ans);
    Console.ReadLine();
  }
}
```

## Integer reverse
Learnings:
* GetRange
* AddRange
* RemoveAt
```csharp
 public static string IntegerReverse(int n)
{
    var s = n.ToString();
    var negativeSign = "";
    var numerals = new List<char>();
    var ans = new List<char>();
    if (s[0] == '-')
    {
        numerals.AddRange(s.ToList().GetRange(1,s.Length-1));
        negativeSign = "-";
    }
    else
    {
        numerals.AddRange(s);
    }


    for (var i = numerals.Count - 1; i >= 0; i--)
    {
        ans.Add(numerals[i]);
    }

    if(ans[0] == '0')
    {
        ans.RemoveAt(0);
    }

    var tempAns = String.Join("", ans);
    return negativeSign + tempAns;
}

static void Main(string[] args)
{
    var ans = IntegerReverse(-53);
    Print(ans);
    Console.ReadLine();
}

## Maxchar
Learnings:
* printing a dictionary
* OrderyByDescending
* Dictionary initializing 
```csharp
public static void Print(string s) => Console.WriteLine(s);

public static char MaxChar(string s)
{
    //var count = new Dictionary<char, int>()
    //{
    //    {'k', 0},
    //    {'z', 1}
    //};

    //var count = new Dictionary<char, int>();
    //var c = 'a';
    //count[c] = 1;

    var count = new Dictionary<char, int>();
    for(var i=0;i<s.Length ;i++)
    {
        var letter = s[i];

        // not in count then set to 1
        if(!count.ContainsKey(letter))
        {
            count[letter] = 1;
            } 
        else if(count.ContainsKey(letter))
        {
            count[letter] += 1;
        }

        // Print out the dictionary
        var asString = string.Join(";", count);
        Print(asString);
    }
    var maxChar = count.OrderByDescending(x => x.Value).FirstOrDefault().Key;
    return maxChar;
}

static void Main(string[] args)
{
    var ans = MaxChar("hyoy");
    Print(ans.ToString());
    Console.ReadLine();
}
```
## Fibonacci
Learnings:
* print a list of numbers
```csharp
public static void Print(string s) => Console.WriteLine(s);

public static int Fib(int n)
{
    var fibNums = new List<int> { 0, 1 };
    for(var i=0; i<n;i++)
    {
        fibNums.Add(fibNums[fibNums.Count - 1] + fibNums[fibNums.Count - 2]);
        Print(String.Join(",", fibNums));
    }
    return fibNums[fibNums.Count - 2];
}

static void Main(string[] args)
{
    var ans = Fib(15);
    Print(ans.ToString());
    Console.ReadLine();
}
```

## FizzBuzz
```csharp
public static void FizzBuzz()
{
    for(var i=0;i<100 ;i++)
    {
        if(i % 15 == 0)
        {
            Print("FizzBuzz");
        } else if(i % 3 ==0 )
        {
            Print("Fizz");
        } else if(i %5 == 0)
        {
            Print("Buzz");

        } else { Print($"{i}"); }
    }

}
```

## ChunkArray
Learnings:
* print json string
* using NewtonSoft.Json
Dependency
```
dotnet add package NewtonSoft.Json
```
the code:
```csharp

using NewtonSoft.Json;

public static void Print(string s) => Console.WriteLine(s);

public static List<List<int>> Chunk(List<int> arr, int n)
{
    var q = new Queue<int>(arr);
    var ans = new List<List<int>>();
    while (q.Any())
    {
        var temp = new List<int>();
        for(var i=0; (i<n && q.Any()) ;i++)
        {
            var current = q.Dequeue();
            temp.Add(current);
        }
        ans.Add(temp);
    }
    return ans;
}


static void Main(string[] args)
{
    var d = new List<int> { 3, 4, 5 };
    var ans = Chunk(d, 2);
   
    Print(
    JsonConvert.SerializeObject(ans)
        );
}
```

## Chunk Array - soln#2
Learnings
* try + catch + AurgumentOutOfRangeException
* using null values
```csharp
using NewtonSoft.Json;


public static void Print(string s) => Console.WriteLine(s);

public static List<List<int>> Chunk(List<int> arr, int chunkSize)
{
    List<List<int>> outerArr = new List<List<int>>();
    List<int> currentInner = null;

    foreach(var element in arr) 
    {
        try
        {
            currentInner = outerArr[outerArr.Count - 1];
        }
        catch (ArgumentOutOfRangeException)
        {
            currentInner = null;
        }

        // Create a new inner array
        // If either the currentInner does not exists
        // or the size of the currentInner is the max inner size
        if((currentInner == null) || (currentInner.Count == chunkSize))
        {
            outerArr.Add(new List<int> { element });
        }
        else
        {
            currentInner.Add(element);
        }
    }
    return outerArr;

}


static void Main(string[] args)
{
    var d = new List<int> { 3, 4, 5 };
    var ans = Chunk(d, 2);
   
    Print(
    JsonConvert.SerializeObject(ans)
        );
}
```

## Chunk Array - soln #3
Learnings:
* ArgumentException
* GetRange
```csharp
using NewtonSoft.Json;
public static void Print(string s) => Console.WriteLine(s);

public static List<List<int>> Chunk(List<int> arr, int chunkSize)
{
    List<List<int>> outerArr = new List<List<int>>();
    var index = 0;
    while(index < arr.Count)
    {
        try
        {
            // similar to slice
            outerArr.Add( arr.GetRange(index, chunkSize) );
        }
        catch (ArgumentException)
        {
            outerArr.Add( arr.GetRange(index, arr.Count-index) );
        }
        index += chunkSize;
    }

    return outerArr;
}


static void Main(string[] args)
{
    var d = new List<int> { 3, 4, 5, 6, 7, 8, 9};
    var ans = Chunk(d, 1);
   
    Print(
    JsonConvert.SerializeObject(ans)
        );
}
```

## Pyramid - soln#1
Learnings:
* Reverse list
* Concat string using plus operator
```csharp
       public static void Print(string s) => Console.WriteLine(s);

        public static void Pyramid(int n)
        {
            int reps;
            List<string> ans = new List<string>();
            int spaces = 0;
             while(n>0)
            {
                reps = 2*(n - 1) + 1;
                ans.Add(new string(' ', spaces) + new string('#', reps));
                n--;
                spaces++;
            }
            ans.Reverse();
            foreach (var l in ans)
            {
                Print(l);
            }
            Print(
            JsonConvert.SerializeObject(ans)
            );

        }


        static void Main(string[] args)
        {

            Pyramid(4);
            //var ans = Chunk(d, 1);

            //Print(
            //JsonConvert.SerializeObject(ans)
            //);
            Console.ReadLine();
        }
```

## Count Vowels
```csharp
using System.Linq;
public static void Print(string s) => Console.WriteLine(s);

public static int CountVowels(string s)
{
    int count = 0;
    char[] vowels = new char[] { 'a', 'e', 'i', 'o', 'u' };
    for(var i=0; i<s.Length; i++)
    {
        if ( vowels.Contains(s[i])  ) count++;
    }
    return count;
}


static void Main(string[] args)
{

    var ans = CountVowels("hello there");
    Console.WriteLine("the number of vowels {0}", ans.ToString());
    //Print(
    //JsonConvert.SerializeObject(ans)
    //);
    Console.ReadLine();
}
```

## Matrix Spiral - soln in python
Learnings
* subsequent for loops
* conditions
Source: https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
```python
def spiral2(rend, cend, a):
  rstart = 0; cstart = 0

  '''
  rstart - starting row IndexError
  rend - ending row index

  cstart - starting column
  cend - ending column
  '''
  count = 1
  while(rstart < rend and cstart < cend):
    
    for i in range(cstart, cend):
      a[rstart][i] = count
      count += 1

    rstart += 1

    for i in range(rstart, rend):
      a[i][cend-1] = count
      count += 1

    cend -= 1

    if(rstart < rend):
      for i in range(cend-1, (cstart-1), -1):
         a[rend-1][i] = count
         count += 1
      rend -= 1
   

    if(cstart < cend):
      for i in range(rend-1, rstart-1, -1):
        a[i][cstart] = count
        count += 1
      cstart += 1
      
  return a

a = []
for i in range(0, 4):
  temp = []
  for j in range(0, 4):
    temp.append(0)
  a.append(temp)

R = 4; C = 4
b = spiral2(R, C, a) 

for i in range(0, 4):
  print(b[i])
```

## Matrix Array - soln #2 - C#
See Python code above for simplified algorithm
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;

namespace REACTO
{
    class Program
    {
        public static void Print(string s) => Console.WriteLine(s);

        public static List<List<int>> Spiral(int n)
        {
            // create empty array
            var a = new List<List<int>>();
            for(var i=0;i<n;i++)
            {
                var temp = new List<int>();
                for (var j = 0; j < n; j++)
                    temp.Add(0);
                a.Add(temp);
            }

            // create row start and column start variables
            var rstart = 0;
            var rend = n;
            var cstart = 0;
            var cend = n;
            var count = 1;
            while(rstart < n && cstart < n)
            {
                // left
                for(int i = cstart; i < cend ;i++)
                {
                    a[rstart][i] = count;
                    count += 1;
                }
                // shift-left
                rstart += 1;

                // down
                for(int i=rstart; i < rend-1 ;i++)
                {
                    a[i][cend - 1] = count;
                    count += 1;
                }
                // shift-up
                cend -= 1;

                // up
                if(rstart < rend)
                {
                    for(int i=cend; i>cstart; i--){
                        a[rend - 1][i] = count;
                        count += 1;
                    }
                    // shift-right
                    rend -= 1;
                }
                // right
                if(cstart < cend)
                {
                    for(int i = rend; i >= rstart; i--)
                    {
                        a[i][cstart] = count;
                        count += 1;
                    }
                    // shift-down
                    cstart += 1;
                }
            }
            return a;
        }

        static void Main(string[] args)
        {

            var ans = Spiral(10);
            //Console.WriteLine("the number of vowels {0}", ans.ToString());
            //Print(
            //JsonConvert.SerializeObject(ans)
            //);

            for (var i = 0; i < ans.Count; i++)
            {
                Print(String.Join(",", ans[i]));
            }
            Console.ReadLine();
        }
    }
}
```

## Breadth First Search - Tree (not BST)
Learnings
* Queue and Dequeue
* initializing a Queue using an array 
* Delegates (passing a method as a parameter)
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using Newtonsoft.Json;

namespace REACTO
{
    class Program
    {

        public static void Print(string s) => Console.WriteLine(s);

        public class Tree
        {
            public Node root { get; set; }

            public Tree(Node r) => this.root = r;

            public void TraverseBF(PrintNodeDelegate fn)
            {
                // initialize queue
                var queue = new Queue<Node>(new Node[] { this.root });
                while (queue.Count > 0)
                {
                    var node = queue.Dequeue();
                    foreach (var child in node.children)
                    {
                        queue.Enqueue(child);
                    }
                    fn(node);
                   
                }
            }
        }
        public class Node
        {
            public int data { get; set; }
            public List<Node> children { get; set; } = new List<Node>();
            public Node(int data)
            {
                this.data = data;
            }
            // adds a child
            public void Add(Node node)
            {
                this.children.Add(node);
            }
            public void Remove(int data)
            {
                Print($"Removing {data}");
                this.children = this.children.Where(n => n.data != data).ToList();
            }
            public void PrintNodes()
            {
                Print(string.Join(",", this.children.Select(c => c.data)));
            }
        }
        public delegate void PrintNodeDelegate(Node node);
        static void PrintNode(Node node)
        {
            Console.WriteLine($"The node value: {node.data}");
        }
        public static void Main(string[] args)
        {
            var p = new Node(1);

            var c1 = new Node(50);
            var c2 = new Node(51);

            var d1 = new Node(100);
            var d2 = new Node(101);

            p.Add(c1);
            p.Add(c2);

            c1.Add(d1);
            c2.Add(d2);

            var tree = new Tree(p);
            tree.TraverseBF(PrintNode);

            Console.ReadLine();

        }
    }
}

```