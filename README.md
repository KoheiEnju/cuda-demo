# HPC-DEMO
C++, CUDA, OpenACCの比較を行う。なおベンチマークの方法は超適当なので、適宜修正していきたい。

## タスク
- 2~3億個のint配列x, yを用意し、和の演算を行う

### コンパイラ
1. C++: g++
2. CUDA: nvcc
3. OpenACC: nvc++

### 結果
1. C++: 4.92s user 0.41s system 99% cpu 5.337 total
2. CUDA: 1.49s user 0.54s system 99% cpu 2.045 total
3. OpenACC: 1.27s user 0.50s system 98% cpu 1.791 total
