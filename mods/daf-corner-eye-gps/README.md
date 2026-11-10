# DAF CornerEye GPS

対象は DAF XG+ 左ハンドル・4×2、標準Argenta内装、純正CornerEye装着車です。

公式Archive Packerで `dlc_daf_2021.scs` を作業フォルダーへ展開し、このディレクトリから実行します。

```powershell
python build_daf_probe.py "C:/path/to/extracted/daf" daf_xgplus_corner_probe.scs
```

生成したMODをETS2ユーザーデータの `mod` フォルダーに置き、検証プロフィールで有効化します。電装をオンにし、CornerEyeとナビの映像が走行に合わせて更新されるか比較してください。対象内装では地図表示をカメラ試験画面に置き換えます。
