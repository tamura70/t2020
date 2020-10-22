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
./als.py -m0 10 >/tmp/als.csp
# Sugarの実行
sugar -vv /tmp/als.csp >/tmp/als.log
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
sugar -vv /tmp/qdp.csp >/tmp/qdp.log
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

- `n` : クイーングラフのサイズ ($n\times n$)，クイーンの個数 ($n$)
- `-m` : 制約モデルの番号を指定する
    - `-m0` : 各行と各列にはexact1制約，各対角線にはatmost1制約を使用
    - `-m1` : 各対角線に対しクイーンの有無を表す補助ブール変数を導入し，その和がnに等しい制約を追加
- `--bc=` : ブール基数制約の符号化方法を指定する (`sugar`, `sinz`, `sinz2`)
- `-v` : Sugarの解の検証

### 実行例

```
# CSPの作成
./nqueens.py -m0 --bc=sinz 8 >/tmp/nqueens.csp
# Sugarの実行
sugar -vv /tmp/nqueens.csp >/tmp/nqueens.log
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

- `n` : クイーングラフのサイズ ($n\times n$)，色数 ($n$)
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
sugar -vv /tmp/qgcp.csp >/tmp/qgcp.log
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

- `n` : 要素の個数
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
sugar -vv /tmp/costasarray.csp >/tmp/costasarray.log
# 結果の検証
./costasarray.py -v 5 </tmp/costasarray.log
```

## util.py

以下のようにして動作を確認できる．

```
$ python -i util.py 
>>> new_name()
'_T1'
>>> new_name()
'_T2'
>>> v("x", 1, 2)
'x_1_2'
>>> t("x", 1, 2)
'_x_1_2'
>>> c("+", 1, 2)
'(+ 1 2)'
>>> c("+", 1, c("+", 2, 3, 4))
'(+ 1 (+ 2 3 4))'
>>> atleast_1(["x1","x2","x3"])
; atleast_1 x1 x2 x3
(or (> x1 0) (> x2 0) (> x3 0))
>>> atleast_1([v("x",1),v("x",2),v("x",3)])
; atleast_1 x_1 x_2 x_3
(or (> x_1 0) (> x_2 0) (> x_3 0))
>>> atmost_1([v("x",1),v("x",2),v("x",3)])
; atmost_1 x_1 x_2 x_3
(<= (+ x_1 x_2) 1)
(<= (+ x_1 x_3) 1)
(<= (+ x_2 x_3) 1)
>>> quit()
```

## プログラムを修正する上での注意事項

#### 小さなパラメータでCSPの内容を確認

例えば以下のようにして生成されるCSPの内容を確認する．

```
./als.py -m0 -t 5 | less
```

また，Sugarで実行できるかどうかを確認する．

```
./als.py -m0 -t 5 >/tmp/als.csp
sugar -vv /tmp/als.csp
````

#### 正しい解が得られているかどうかを確認

```
./als.py -m0 -t 5 >/tmp/als.csp
sugar -vv /tmp/als.csp >/tmp/als.log 2>&1
./als.py -v 5 </tmp/als.log
```

- `2>&1` は標準エラー出力を標準出力にリダイレクトする
- `Verify OK` と表示されれば正しい解

Sugarの実行結果をコンソールにも表示したい場合は以下のようにする．

```
./als.py -m0 -t 5 >/tmp/als.csp
sugar -vv /tmp/als.csp 2>&1 | tee /tmp/als.log
./als.py -v 5 </tmp/als.log
```

#### 大きなパラメータで実行してみる

```
./als.py -m0 -t 20 >/tmp/als.csp
sugar -vv /tmp/als.csp >/tmp/als.log 2>&1 &
バックグラウンド処理が終了するまで待つ
./als.py -v 20 </tmp/als.log
```

- `&` はバックグラウンド処理
- `tail -f /tmp/als.log` で出力を確認できる (C-cで終了)．
- `jobs` でバックグラウンド処理が終了したかどうかを確認できる
- 処理を中断したければ `kill %1` などを実行する

#### その他

##### `less` の使い方

- `h` : ヘルプの表示 (qで終了)
- `q` : 終了
- `f` : 1画面進む (` `でも同じ)
- `b` : 1画面戻る
- `d` : 半画面進む
- `u` : 半画面戻る
- `/` : 前向き検索
- `?` : 後ろ向き検索
- `n` : 検索の再実行
- `&` : 検索パターンに合致する行だけ表示
- `ma` : 現在行を`a`でマーク (`a`は他の文字でも良い)
- `'a` : `a`でマークした行に移動 (`a`は他の文字でも良い)
- `F` : `tail -f`と同様の表示 (C-cで終了)
- `-N` : 行番号の表示
- `-S` : 行を折りたたまないで表示

##### 注意事項

- `top` コマンドで予期せず実行中のプログラムがないかを確認する．
    - あれば `kill` コマンドで終了させる．
- `/tmp/` が溢れないように注意する．
    - `/tmp/sugar*` の一時ファイルが大量に残っていれば削除する．

