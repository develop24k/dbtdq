import dto


def get_tests_yaml(tests):
    buffer = "tests:\n"
    for x in tests:
        buffer += "              - " + x + "\n"

    return buffer


def get_column_yaml(name, desc, tests):
    buffer = "          - name: " + name + "\n"
    buffer += "            description: " + desc + "\n"
    buffer += "            " + tests
    return buffer


def get_table_yaml(name, cols):
    buffer = "      - name: " + name + "\n"
    buffer += "        columns:" + "\n"

    for c in cols:
        buffer += c + "\n"

    return buffer


def get_source_yaml(name, database, schema, tables):
    buffer = "version: 2\n"
    buffer += "sources:\n"
    buffer += "  - name: " + name + "\n"
    buffer += "    database: " + database + "\n"
    buffer += "    schema: " + schema + "\n"
    buffer += "    tables:\n"

    for t in tables:
        buffer += t + "\n"

    return buffer


# print(get_tests_yaml(["unique", "not_null", "dbt_expectations.expect_column_to_exist"]))


col1 = get_column_yaml("id", "Primary key of the table",
                       (get_tests_yaml(["unique", "not_null", "dbt_expectations.expect_column_to_exist"])))

col2 = get_column_yaml("title", "Primary key of the table",
                       (get_tests_yaml(["dbt_expectations.expect_column_to_exist"])))

tab = get_table_yaml("movies", [col1, col2])

final = get_source_yaml("public", "homedb", "public", [tab])

#print(final)

#f = open("c:\\temp\\demofile3.txt", "w")
#f.write(final)
#f.close()
