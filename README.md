## All-Interval Series (AIS)

- <http://www.csplib.org/Problems/prob007/>

### 利用方法

```
./als.py [options] n
```

- `n` : AISの要素の個数
- `-m` : 制約モデルの番号を指定する
    - `-m0` : Sugarのalldifferentを使用
    - `-m1` : alldifferentに大野の方法を使用 (未実装)
- `-t` : 自明な解を除去する
    - 最初および最後の差が1でない解を探す
- `--bc=` : ブール基数制約の符号化方法を指定する
    - `sugar` : Sugarの式
    - `sinz` : SinzのSequential Counter法
    - `sinz2` : SinzのSequential Counter法を改良
- `-v` : Sugarの解の検証

### 実行例

```
# CSPの作成
./als.py -m0 --bc=sinz 10 >/tmp/als.csp
# Sugarの実行
sugar /tmp/als.csp >/tmp/als.log
# 結果の検証
./als.py -v 10 </tmp/als.log
```

## Queen Domination Problem (QDP)

- <https://oeis.org/A075458>
- <https://mathworld.wolfram.com/QueenGraph.html>
- <https://mathworld.wolfram.com/DominationNumber.html>

### 利用方法

```
./qdp.py [options] n d
```

- `n` : クイーングラフのサイズ ($n\times n$)
- `d` : クイーンの個数の上限
- `-m` : 制約モデルの番号を指定する
    - `-m0` : 補助変数なし
    - `-m1` : 各行，各列，各対角線でのクイーンの有無を表す補助変数を利用 (未実装)
- `--bc=` : ブール基数制約の符号化方法を指定する
    - `sugar` : Sugarの式
    - `sinz` : SinzのSequential Counter法
    - `sinz2` : SinzのSequential Counter法を改良
- `-v` : Sugarの解の検証

### 実行例

```
# CSPの作成
./qdp.py -m0 --bc=sinz 8 5 >/tmp/qdp.csp
# Sugarの実行
sugar /tmp/qdp.csp >/tmp/qdp.log
# 結果の検証
./qdp.py -v 8 5 </tmp/qdp.log
```

## N-Queens Problem

- <http://www.csplib.org/Problems/prob054/>
- <https://mathworld.wolfram.com/QueensProblem.html>


### 利用方法

```
./nqueens.py [options] n
```

- `n` : AISの要素の個数
- `-m` : 制約モデルの番号を指定する (`0`, `1`)
- `--bc=` : ブール基数制約の符号化方法を指定する (`sugar`, `sinz`, `sinz2`)
- `-v` : Sugarの解の検証

### 実行例

```
# CSPの作成
./nqueens.py -m0 --bc=sinz 8 >/tmp/nqueens.csp
# Sugarの実行
sugar /tmp/nqueens.csp >/tmp/nqueens.log
# 結果の検証
./nqueens.py -v 8 </tmp/nqueens.log
```

## Queen Graph Coloring Problem (QGCP)

- <https://mathworld.wolfram.com/QueenGraph.html>
- <https://mathworld.wolfram.com/VertexColoring.html>

### 利用方法

```
./qgcp.py [options] n
```

- `n` : AISの要素の個数
- `-m` : 制約モデルの番号を指定する
    - `-m0` : Sugarのalldifferentを使用
    - `-m1` : alldifferentに大野の方法を使用
- `-x` : 対称性を除去する (最初の行の色を指定する)
- `--bc=` : ブール基数制約の符号化方法を指定する (`sugar`, `sinz`, `sinz2`)
- `-v` : Sugarの解の検証

### 実行例

```
# CSPの作成
./qgcp.py -m0 --bc=sinz 5 >/tmp/qgcp.csp
# Sugarの実行
sugar /tmp/qgcp.csp >/tmp/qgcp.log
# 結果の検証
./qgcp.py -v 5 </tmp/qgcp.log
```

## Costas Array Problem

- <http://www.csplib.org/Problems/prob076/>
- <https://en.wikipedia.org/wiki/Costas_array>

### 利用方法

```
./costasarray.py [options] n
```

- `n` : AISの要素の個数
- `-m` : 制約モデルの番号を指定する
    - `-m0` : Sugarのalldifferentを使用
    - `-m1` : alldifferentに大野の方法を使用 (未実装)
- `--bc=` : ブール基数制約の符号化方法を指定する (`sugar`, `sinz`, `sinz2`)
- `-v` : Sugarの解の検証

### 実行例

```
# CSPの作成
./costasarray.py -m0 5 >/tmp/costasarray.csp
# Sugarの実行
sugar /tmp/costasarray.csp >/tmp/costasarray.log
# 結果の検証
./costasarray.py -v 5 </tmp/costasarray.log
```

