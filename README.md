# ETS2 Mods by XENO LUCUS

**Euro Truck Simulator 2向けの車内表示MODと、車両検証を助けるツール。**  
Designed and built by **XENO LUCUS**.

車内ナビをカメラモニターとして使う試作と、その表示を複数の車両で試すための検証環境づくりから始めています。

## MOD一覧

| MOD | できること | 現在の状態 |
| --- | --- | --- |
| [DAF CornerEye GPS](mods/daf-corner-eye-gps/) | DAF XG+の純正CornerEye映像を車内ナビに表示する試作 | 1.62.1.0sの純正定義でビルド確認済み。ゲーム内の映像更新は未確認 |
| [Test Fleet Bootstrap](mods/test-fleet-bootstrap/) | ガレージの購入・拡張費用を下げ、検証用の資金とXPを増やす | 1.62.1.0sの純正定義でビルド確認済み。ゲーム内反映は未確認 |

## はじめ方

各MODのページから対象車両、ビルド手順、ゲーム内での確認項目を参照できます。Windows、Python 3.12、[SCS Game Archive Packer](https://modding.scssoft.com/wiki/Documentation/Tools/Game_Archive_Packer)を使い、お手元のETS2の定義から `.scs` を生成します。

## 今後の検証

- **カメラ** — まずナビ上のライブ更新を確認し、前後左右の切り替え、上方視点、複数映像の俯瞰合成、操舵連動ガイド線を順に調べます。
- **車両テスト** — 1台での表示確認後に、内装やミラー構成が異なる車両へ広げます。全ガレージの一括所有とマップ踏破率100%は未実装です。

動作結果を共有する場合は、ETS2のバージョン、車種・内装、表示された内容を添えてください。スクリーンショットやエラー行があると再現しやすくなります。

## 作者とライセンス

**XENO LUCUS** · [GitHub](https://github.com/xenolucus)

自作のビルドスクリプトと文書は [MIT License](LICENSE) です。ETS2の純正定義や素材の権利は各権利者に帰属します。純正アーカイブや生成済みの `.scs` はリポジトリに含めません。
