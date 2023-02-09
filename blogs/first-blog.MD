# Hello, world!

____

For my first blog post it seemed fitting to pay homage to almost everyone's first programming project `Hello, World!` - continuing on from this theme, we will be taking a look at `Hello, World!` implemented in a few languages. Namely C, Java, Python, Scala, and Rust. As someone who started their programming journey with Java (and fervently defended it), it was only until I had dabbled with other languages that I began to understand the hate for Java. That being said, despite its inherent verbosity, it's the first language that I felt somewhat comfortable with.



## C
```c
#include <stdio.h>

int main() {

   printf("Hello, World!");

   return 0;

}
```

__________


## Java
```java
class HelloWorld {

    public static void main(String[] args) {

        System.out.println("Hello, World!"); 

    }
}
```

_________

## Python
```python
print("Hello, World!")
```

Or we can define a `main` entry point for our python program:

```python
if __name__ == '__main__':

    print("Hello, World!")

```

_______

## Scala
```scala
object Hello {

    def main(args: Array[String]) = {

        println("Hello, world")

    }
}
```

_______

## Rust
```rust
fn main() {

    println!("Hello World!");

}
```


__________


At the end of the day, no language is perfect in its design. There will always be oddities or quirks that turn-off a particular segment of people, whilst attracting an entirely another group. If verbosity is a dealbreaker in a language - that's okay! Selecting a language to use based off of subjective measures is perfectly valid - especially if it's for fun or a hobby. Why learn or use something that you do not enjoy? That being said, it's always best to choose a language that is appropriate for the task at hand. At the end of the day, a programming language is a tool to achieve a certain goal, task, or outcome. Some languages are better suited for particular tasks than others.