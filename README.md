# plsp: Pythonで実装された簡単なLispインタプリタ

chatGPTで提示されたLisp処理系を評価しつつ、実装を強化していく実験。

plspは、簡単なLispインタプリタで、基本的なリスト操作、関数定義などが実装されています。

## 1. プロジェクトのインストール

GitHubリポジトリから直接プロジェクトをインストールするには、次のコマンドを使用します。

```arduino
pip install git+https://github.com/gamasenninn/plsp.git
```



これにより、最新のバージョンの`plsp`パッケージがインストールされます。
## 2. プロジェクトのアップグレード

プロジェクトをアップグレードするには、次のコマンドを使用します。

```
pip install --upgrade --no-cache-dir git+https://github.com/gamasenninn/plsp.git
```
このコマンドでは、キャッシュを無効にしてGitHubリポジトリから最新の変更を取得し、`plsp`パッケージをアップグレードします。

もし、これによって更新がされない場合は、一度アンインストールして、再度リポジトリから新たにイントールしてください。

```
pip uninstall plsp
pip install git+https://github.com/gamasenninn/plsp.git
```

## 3. plspの実行

プロジェクトが正常にインストールされていれば、コマンドラインから`plsp`コマンドを使用して実行できます。

```
>plsp
```

また、pythonモジュールとして実行したい場合は
```
>python -m plsp
```
として実行できます。


いずれも、プロンプトが表示されたら、Lisp式を入力して評価します。

## 4.基本的な操作

以下に、plspで利用できる基本的な操作の例を示します。

### 数値演算
```
(+ 2 3) ; 2 + 3 = 5 を出力
(- 10 4) ; 10 - 4 = 6 を出力
(* 3 4) ; 3 * 4 = 12 を出力
(/ 9 3) ; 9 / 3 = 3 を出力
```

### 比較演算
```
(< 2 3) ; 2 < 3 は真であるため、True を出力
(> 5 3) ; 5 > 3 は真であるため、True を出力
(= 4 4) ; 4 = 4 は真であるため、True を出力
```

### 変数定義
```
(define x 10) ; x という変数に 10 を割り当てる
(define y 20) ; y という変数に 20 を割り当てる
(+ x y) ; 10 + 20 = 30 を出力
```

### 関数定義
```
(defunc add (a b) (+ a b)) ; add 関数を定義
(add 5 7) ; 5 + 7 = 12 を出力
```
### ラムダ関数
```
((lambda (x y) (+ x y)) 3 4) ; 3 + 4 = 7 を出力
(define add (lambda (x y) (+ x y))) ; add ラムダ関数を定義
(add 8 2) ; 8 + 2 = 10 を出力
```

### 条件分岐 (if)
```
(if (< 3 4) 1 0) ; 3 < 4 は真であるため、1 を出力
(if (> 10 20) 1 0) ; 10 > 20 は偽であるため、0 を出力
```

### リスト操作

plspでは、基本的なリスト操作もサポートされています。以下にいくつかの例を示します。

### car、cdr、cons
```
(car (list 1 2 3)) ; 1 を出力
(cdr (list 1 2 3)) ; (2 3) を出力
(cons 1 (list 2 3)) ; (1 2 3) を出力
```

### append、length、map
```
(append (list 1 2 3) (list 4 5 6)) ; (1 2 3 4 5 6) を出力
(length (list 1 2 3)) ; 3 を出力
(map (lambda (x) (* x 2)) (list 1 2 3)) ; (2 4 6) を出力
```

### 再帰関数のサンプル
階乗関数を定義
```
(defunc factorial (n) (if (<= n 1) 1 (* n (factorial (- n 1)))))

```
```
(factorial 1) ; 1 を出力
(factorial 5) ; 120 を出力
(factorial 10) ; 3628800 を出力
```
  
フィボナッチ関数を定義
```
(defunc fibonacci (n) (if (< n 2) n (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))
```
```
(fibonacci 0) ; 0 を出力
(fibonacci 1) ; 1 を出力
(fibonacci 5) ; 5 を出力
(fibonacci 10) ; 55 を出力
```
