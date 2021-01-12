# Go with the flow

Once again, similar to the previous three challenges, this involves buffer overflow as well. Only this time, we need to call a function after we overflow the stack.
That is the intended way to do that atleast. 

We'll use a reversing tool commonly used called [radare2](https://github.com/radareorg/radare2). To read all its commands and basic How-To's refer to [this](https://medium.com/@jacob16682/reverse-engineering-using-radare2-588775ea38d5).

We'll start by running radare2 and analyzing the binary :

