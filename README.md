# セキュリティログモニタリングシステム

このプロジェクトは、AWSサービスを使用してAWSアカウントのセキュリティログを収集し、モニタリングとアラートを行うシステムです。

## 使用技術

- AWS CloudTrail
- Amazon CloudWatch
- AWS Lambda
- Amazon S3


## セットアップ手順

1. リポジトリをクローンします:
    ```
    git clone <リポジトリURL>
    cd security-log-monitoring
    ```

2. Lambda関数のデプロイ:
    - AWS Lambdaコンソールで新しい関数を作成します。
    - `lambda_function.py`のコードを関数にコピーします。
    - `boto3`ライブラリを含むLambdaレイヤーを作成して関数にアタッチします。

3. CloudTrailの設定:
    - AWS CloudTrailコンソールで新しいTrailを作成し、ログをS3バケットに配信します。

4. S3バケットの設定:
    - S3バケットを作成し、CloudTrailのログを保存するように設定します。

5. CloudWatchの設定:
    - CloudWatchコンソールで新しいロググループを作成し、Lambda関数のログを監視します。

6. SNSトピックの設定:
    - SNSコンソールで新しいトピックを作成し、アラート通知を設定します。

## 使用方法

- CloudTrailがAWSアカウントのセキュリティログをS3に保存します。
- Lambda関数がS3に保存されたログを処理し、特定のイベントに対してアラートをSNSで送信します。
- CloudWatchを使用してLambda関数のログを監視し、必要に応じて追加のアラートを設定します。




