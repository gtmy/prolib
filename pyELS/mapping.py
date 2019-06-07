# coding:utf-8

from elasticsearch import Elasticsearch

class MappingELS(object):
    """mappingを作成するクラス

    Args:
        index (str): インデックス名
        host (str): ホスト名
        port (str): ポート名
    """

    def __init__(self, index, host, port):
        """

        Vars:
            self.index (str): インデックス名
            self.els (Elasticsearch): elasticsearchのインスタンス
            self.json (dict): テーブル定義を格納する辞書
        """

        self.index = index
        self.els = Elasticsearch(host=host, port=port)
        self.json = {"mappings": {}}

    def data_mapping(self):
        """example mapping
        data用のmappingの作成と登録
        """

        table = {
            # サンプルデータ
            "sample1": (
                ("id", "long"),
                ("name", "text"),
            ),
            "sample2": (
                ("id", "long"),
                ("value", "float"),
            ),
        }

        self.create(table=table)

    def create(self, table):
        """self.jsonにテーブル定義を追記する

        Args:
            table (dict): テーブル定義を行う，カラムとタイプの辞書
        """

        for doc_type, column_list in table.items():
            self.json["mappings"][doc_type] = {"properties": {}}
            for cname, ctype in column_list:
                column = {}
                if ctype == "long":
                    column = {"type": "long"}
                elif ctype == "float":
                    column = {"type": "float"}
                else:
                    column = {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    }
                self.json["mappings"][doc_type]["properties"][cname] = column

    def register(self):
        """indexにmappingを登録する
        """

        self.els.indices.delete(index=self.index, params={"ignore": 404})
        self.els.indices.create(index=self.index, body=self.json)
