#coding: utf-8
import theano
import theano.tensor as T

x = T.dscalar('x')

# 微分される数式のシンボルを定義
y = x ** 2

# yをxに関して微分
# y'=2xになる
gy = T.grad(cost=y, wrt=x)

# 微分係数を求める関数を定義
f = theano.function(inputs=[x], outputs=gy)
print theano.pp(f.maker.fgraph.outputs[0])

# 具体的なxを与えて微分係数を求める
print f(2)
print f(3)
print f(4)
