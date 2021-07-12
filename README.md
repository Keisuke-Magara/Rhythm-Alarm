# Rhythm Alarm!
**コナミの大人気リズムゲーム "jubeat" のような、パネルクリック型のリズムゲームをクリアするまでミュージックが止まらないアラームです。**

## **How to Use**
    以下のライブラリを pip などでインストールし、 Rhythm_Alarm.py を実行してください。
     - mugen
     - numpy
     - Pillow
     - pygame
     - tkinter
    
    ディレクトリ内のファイル構成を変更すると起動しなくなる可能性があります。
    移動する際は、 The-Rythm-Alarm ディレクトリごと移動してください。

## **製作者**
    
## **フォルダ構造**

## **クラス図**

## **Score maker for Rhythm Alarm**

## **Pyinstallerによるexeファイル化**
    Pyinstaller ライブラリを使用してexeファイル化する場合、以下の点に注意してください。
     - exeファイル化の副作用として、パネルのGIFアニメーションの表示が速くなります。
        => Panel.py 14行目 fps の値を 14fps (元のフレーム28fpsの半分) に設定することで改善します。
        => delay を 636ms くらいに設定するとパネルのアニメーションとミュージックのタイミングが同期します。
    
     - exeファイル化によって、assetsフォルダや設定ファイルなどが失われてしまうため、復元してから起動してください。
        => assets フォルダ と music_names.txt, setting.txt を完成した Rhythm_Alarm.exe と同階層のディレクトリにコピーしてください。