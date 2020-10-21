# t2020

## All-Interval Series (AIS)

- <http://www.csplib.org/Problems/prob007/>

### 利用方法

```
./als.py [options] n
```

- `n` : AISの要素の個数 $n$
- `-m` : 制約モデルの番号を指定する
- `-t` : 自明な解を除去する
    - 最初および最後の差が1でない解を探す
- `--bc=` : ブール基数制約の符号化方法を指定する
    - `sugar` : Sugarの式
    - `sinz` : SinzのSequential Counter法
    - `sinz2` : SinzのSequential Counter法を改良
- `-v` : Sugarの解の検証

### 実行例

```
./als.py -m0 --bc=sinz 10 >/tmp/als.csp
sugar /tmp/als.csp >/tmp/als.log
./als.py -v 10 </tmp/als.log
```

