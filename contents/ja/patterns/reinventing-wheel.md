# 車輪の再発明

## Description

「車輪の再発明」は、多くの場合には非効率的であり、オープンソースのものを使ったり、組織全体で共有リソースを増やすことが重要だとされています。
しかし、知らない誰かによってホストされているコードに依存することは、メンテンナンスにおいて問題があることがあります。依存関係の大きなライブラリやフレームワークに依存することが必要な場合は、車輪の再発明が好まれる場合があります。

このパターンは[Matt Rickard氏のブログ](https://matt-rickard.com/having-a-GitHub Copilot)にインスパイアされています。

> Prefer a little copying over a little dependency
> Instead of vendoring in left-pad as a dependency, use GitHub Copilot to generate the function. There are benefits to using battle-tested generic libraries but also benefits to bringing simple code in-tree.

## Problem

left-pad 問題をご存知でしょうか。2016年に left-pad というライブラリが npm で公開停止になったことによって、依存関係を持つ有名なライブラリが軒並み動作しなくなってしまいました。
left-padは、シンプルなJavaScriptで書かれたライブラリで、文字列の左側を指定した文字数、指定しない場合は空白で埋めるだけの実装です。
空白行を除けば10行程度しかないシンプルなコードです。

インナーソースの考え方やXPにおけるコード共有オーナーシップなど、車輪の再発明を避ける考え方は多くあります。一方で大きな影響を持つ外部のコードにも目を向ける必要があります。
提供されるコードのスコープが非常に限定的な場合、外部に依存関係を持つよりも、内部に閉じ込めた方が良い可能性があります。

## Context

GitHub Copilot は、簡単なコードを生成することに長けています。依存関係を持たない方が良いとする意見もありますが、それはビジネスロジックや実装において依存し合う関係を持つことを指しています。
ステートレスな関数や片方からしか依存されないものに関しては、GitHub Copilotを使用して作成することができます。

## Solution

依存関係の大小によって、車輪の再発明が必要かどうかを判断することができます。
小さな依存関係を持ち、影響範囲も狭い場合は、再発明を行うことが有益な場合があります。
left-pad問題などがその例です。
