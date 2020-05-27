# cds-ifttt-alart
光センサから値を読み取り、Google SpreadSheetに送信し、IFTTT経由でスマホに通知をしてくれます。

# 使用ツール
光センサ
ラズベリーパイゼロ

# 回路図
![circle](https://user-images.githubusercontent.com/43441878/82989167-33bda980-a035-11ea-8d35-094eda97cf9d.jpg)
# IFTTTとの連携
- 始めに
今回ははじめてiftttを使ってみたのでここは自分のためにも備忘録として記します。
- IFTTTとは
If This Then Thatの頭文字を取ったもので、ThisとThatの所につなぎたいデバイスやアプリなどを設定してあげると、
簡単に異なるサービス同士を連携してくれるよと言うものです。
今回はThisに[webhooks]にThat[spreadsheet]と[notification]を設定しました。

- spreadsheetの画面

![spreadsheet](https://user-images.githubusercontent.com/43441878/82989466-b6deff80-a035-11ea-9d2c-1a135b04fcbf.png)

- スマホにalartで通知


![alart](https://user-images.githubusercontent.com/43441878/82989513-c9593900-a035-11ea-9ffb-d305834b610f.png)



# スマホに通知
