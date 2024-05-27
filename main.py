from typing import List, Optional
# from yamlable import yaml_info, YamlAble
import yaml
import dto


from typing import List


class Column:
    name: str
    description: str
    tests: List[str]

    def __init__(self, name: str, description: str, tests: List[str]) -> None:
        self.name = name
        self.description = description
        self.tests = tests


class Table:
    name: str
    columns: List[Column]

    def __init__(self, name: str, columns: List[Column]) -> None:
        self.name = name
        self.columns = columns


class Source:
    name: str
    database: str
    schema: str
    tables: List[Table]

    def __init__(self, name: str, database: str, schema: str, tables: List[Table]) -> None:
        self.name = name
        self.database = database
        self.schema = schema
        self.tables = tables


# @yaml_info(yaml_tag_ns='com.yamlable.example')
class Welcome4:
    version: int
    sources: Source

    def __init__(self, version: int, sources: Source) -> None:
        self.version = version
        self.sources = sources


test1 = ["unique", "not_null", "dbt_expectations.expect_column_to_exist"]
test2 = ["unique", "not_null", "dbt_expectations.expect_column_to_exist"]

column1 = Column("id", "Primary key of the table", test1)
column2 = Column("title", "Primary key of the table", test2)

columns = [column1, column2]

table1 = Table("movies", columns)

table2 = Table("movies2", columns)

tables = [table1, table2]

source = Source("public", "homedb", "public", tables)

welcome = Welcome4(2, source)

print(yaml.dump(welcome))

f = open("c:\\temp\\demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

dto1 = dto.DtbDataObj("C_Rule_1", "is unique", 1, "unique", "", "movies", "id", "C")
dto2 = dto.DtbDataObj("C_Rule_2", "is not_null", 2, "not_null", "", "movies", "id", "C")
dto3 = dto.DtbDataObj("C_Rule_3", "does column exist", 3, "dbt_expectations.expect_column_to_exist", "", "movies", "id",
                      "C")
dto4 = dto.DtbDataObj("C_Rule_1", "is unique", 1, "unique", "", "movies", "title", "C")
dto5 = dto.DtbDataObj("C_Rule_2", "is not_null", 2, "not_null", "", "movies", "title", "C")
dto6 = dto.DtbDataObj("C_Rule_3", "does column exist", 3, "dbt_expectations.expect_column_to_exist", "", "movies",
                      "title", "C")

dto7 = dto.DtbDataObj("C_Rule_1", "is unique", 1, "unique", "", "movies2", "id", "C")
dto8 = dto.DtbDataObj("C_Rule_2", "is not_null", 2, "not_null", "", "movies2", "id", "C")
dto9 = dto.DtbDataObj("C_Rule_3", "does column exist", 3, "dbt_expectations.expect_column_to_exist", "", "movies2",
                      "id", "C")
dto10 = dto.DtbDataObj("C_Rule_1", "is unique", 1, "unique", "", "movies2", "title", "C")
dto11 = dto.DtbDataObj("C_Rule_2", "is not_null", 2, "not_null", "", "movies2", "title", "C")
dto12 = dto.DtbDataObj("C_Rule_3", "does column exist", 3, "dbt_expectations.expect_column_to_exist", "", "movies2",
                       "title", "C")

dtos = [dto1, dto2, dto3, dto4, dto5, dto6, dto7, dto8, dto9, dto10, dto11, dto12]
