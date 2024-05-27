from dataclasses import dataclass


@dataclass
class DtbDataObj:
    canonical_rule_id: str
    canonical_rule_desc: str
    dbt_test_id: int
    dbt_test_name: str
    dbt_test_param: str
    dbt_test_table: str
    dbt_test_column: str
    dbt_test_level: str
