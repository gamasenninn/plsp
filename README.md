# plsp: Pythonで実装された簡単なLispインタプリタ

chatGPTで提示されたLisp処理系を評価しつつ、実装を強化していく実験。


### append、length、map
```
(append (list 1 2 3) (list 4 5 6)) ; (1 2 3 4 5 6) を出力
(length (list 1 2 3)) ; 3 を出力
(map (lambda (x) (* x 2)) (list 1 2 3)) ; (2 4 6) を出力
```