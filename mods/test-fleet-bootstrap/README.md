# Test Fleet Bootstrap

検証用プロフィール向けの経済設定です。ガレージの購入・拡張を各€1に設定し、配送の固定報酬と経験値を増やします。

公式Archive Packerで `def.scs` を作業フォルダーへ展開し、このディレクトリから実行します。

```powershell
python build_test_fleet_bootstrap.py "C:/path/to/extracted/def" ets2_test_fleet_bootstrap.scs
```

生成したMODをETS2ユーザーデータの `mod` フォルダーに置き、検証プロフィールで有効化します。配送を手動駐車で完了してXPと報酬を確認し、ガレージはゲーム内で購入・拡張します。
