import dto
import yam

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


def get_table_list(dto_list):
    unique_list = []
    for d in dto_list:
        if d.dbt_test_table not in unique_list:
            unique_list.append(d.dbt_test_table)
    return unique_list


def get_column_list(dto_list, tab):
    unique_list = []
    for d in dto_list:
        if d.dbt_test_table == tab and d.dbt_test_column not in unique_list:
            unique_list.append(d.dbt_test_column)
    return unique_list


def get_test_list(dto_list, tab, colm):
    unique_list = []
    for d in dto_list:
        if d.dbt_test_table == tab and d.dbt_test_column == colm and d.dbt_test_name not in unique_list:
            unique_list.append(d.dbt_test_name)
    return unique_list


all_tables = get_table_list(dtos)

#print(all_tables)

yml_columns = []

for table in all_tables:
    for dto in dtos:
        if dto.dbt_test_table == table:
            cols = get_column_list(dtos, table)
            yml_columns.clear()
            for col in cols:
                tests = get_test_list(dtos, table, col)
                yml_tests = yam.get_tests_yaml(tests)

                yml_columns.append(yam.get_column_yaml(col, "Defined in DB", yml_tests))

            tab = yam.get_table_yaml(table, yml_columns)

    final = yam.get_source_yaml("public", "homedb", "public", [tab])

    print(final)
